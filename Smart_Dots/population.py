import random
import sys
from dot import Dot
from settings import POPULATION_SIZE, MUTATION_CHANCE, BRAIN_SIZE

class Population:
   def __init__ (self):
      self.Dots = [Dot() for _ in range(POPULATION_SIZE)]
      self.max_steps = BRAIN_SIZE

   def reset(self):
      for dot in self.Dots:
         dot.reset()

   def show(self,screen):
      for dot in self.Dots:
          dot.show(screen)

   def update(self, goal):
      for dot in self.Dots:
         if dot.Brain.step > self.max_steps:
            dot.dead = True
         else:
            dot.update(goal)
   
   def reset_champion(self):
      for dot in self.Dots:
         if dot.champion:
            dot.champion = False
            break

   def calculate_fitness(self, goal):
      max_fitness = 0
      min_fitness = sys.maxsize
      max_index = -1
      min_index = -1
      self.reset_champion()
      for i in range(len(self.Dots)):
         self.Dots[i].calculate_fitness(goal)
         if max_fitness < self.Dots[i].fitness:
            max_fitness = self.Dots[i].fitness
            max_index = i
         elif min_fitness > self.Dots[i].fitness:
            min_fitness = self.Dots[i].fitness
            min_index = i
      if max_index != -1:
         self.Dots[max_index].champion = True
         self.max_steps = self.Dots[max_index].Brain.step
      return max_index, min_index
   
   def check_all_dots_dead(self):
      for dot in self.Dots:
         if not dot.dead and not dot.reach_goal:
            return False
      return True

   def tournament_selection(self, strongest, weakest):
      survivors = []
      survivors.append(self.Dots[strongest])
      
      selection_pool = [dot for i, dot in enumerate(self.Dots) if i != strongest and i != weakest]

      random.shuffle(selection_pool)
      half = len(selection_pool) // 2
      for i in range(half):
         nod1 = selection_pool[i]
         nod2 = selection_pool[i + half]
         survivors.append(nod1 if nod1.fitness > nod2.fitness else nod2)

      return survivors
   
   def gaussian_mutation(self):
      for dot in self.Dots:
         if random.random() < MUTATION_CHANCE and not dot.champion:
            dot.Brain.gaussian_mutation()

   def new_generation(self, goal):
      strongest, weakest = self.calculate_fitness(goal)
      newgen = []
      newgen.extend(self.tournament_selection(strongest, weakest))
      half = len(newgen)
      for i in range(0 , half - 1, 2):
         child1_dirs, child2_dirs = newgen[i].two_point_crossover(newgen[i+1])
         child1 = Dot()
         child2 = Dot()
         child1.Brain.directions = child1_dirs
         child2.Brain.directions = child2_dirs
         newgen.append(child1)
         newgen.append(child2)
      
      random.shuffle(newgen)
      self.Dots = newgen
      self.gaussian_mutation()
      self.reset()