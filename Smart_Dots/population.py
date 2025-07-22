import random
from dot import Dot
from settings import POPULATION_SIZE, BRAIN_SIZE, MUTATION_CHANCE

class Population:
   def __init__ (self):
      self.Dots = [Dot() for _ in range(POPULATION_SIZE)]

   def reset(self):
      for dot in self.Dots:
         dot.reset()

   def show(self,screen):
      for dot in self.Dots:
          dot.show(screen)

   def update(self, goal):
      for dot in self.Dots:
         dot.update(goal)
   
   def calculate_fitness(self, goal):
      for dot in self.Dots:
         dot.calculate_fitness(goal)
   
   def check_all_dots_dead(self):
      for dot in self.Dots:
         if dot.dead is False and dot.reach_goal is False:
            return False
      return True
   
   def tournament_selection(self):
      survivors = []
      random.shuffle(self.Dots)
      half = len(self.Dots) // 2
      for i in range(half):
         survivors.append(self.Dots[i] if self.Dots[i].fitness > self.Dots[i + half].fitness else self.Dots[i + half])
      return survivors
   
   def mutation(self):
      for dot in self.Dots:
         if random.random() < MUTATION_CHANCE:
            dot.Brain.mutation()

   def new_generation(self, goal):
      self.calculate_fitness(goal)
      newgen = []
      newgen.extend(self.tournament_selection())
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
      self.mutation()
      self.reset()