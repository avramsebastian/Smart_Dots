import pygame
import random
from brain import Brain
from settings import HEIGHT, WIDTH, BLACK, BRAIN_SIZE, GREEN

class Dot :
    def __init__(self) :
        self.pos = pygame.Vector2(WIDTH // 2, 600)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.color = BLACK
        self.size = 3
        self.Brain = Brain()
        self.dead = False
        self.fitness = 0
        self.reach_goal = False
        self.champion = False

    def show(self, screen) :
        if self.champion is True:
            self.color = GREEN
        else:
            self.color = BLACK
        pygame.draw.circle(screen,self.color,(self.pos[0],self.pos[1]),self.size)

    def reset(self):
        self.pos = pygame.Vector2(WIDTH // 2, 600)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.dead = False
        self.fitness = 0
        self.reach_goal = False
        self.Brain.step = 0

    def move(self):
        if len(self.Brain.directions) > self.Brain.step :
            self.acc = pygame.Vector2(self.Brain.directions[self.Brain.step])
            self.Brain.step += 1
        else :
            self.dead = True
        self.vel += self.acc
        self.vel.clamp_magnitude_ip(5)
        self.pos += self.vel

    def update(self, goal):
        if self.dead is False and self.reach_goal is False:
            self.move()
            if self.pos[0] < 2 or self.pos[1] < 2 or self.pos[0] > WIDTH - 2 or self.pos[1] > HEIGHT - 2 :
                self.dead = True
            else:
                distance_to_goal = self.pos.distance_to(goal.pos)
                if distance_to_goal < 7 :
                    self.reach_goal = True

    def calculate_fitness(self, goal):
        if self.reach_goal is True:
            self.fitness = 1.0 + 10000.0 / (self.Brain.step ** 2)
        else :
            distance_to_goal = self.pos.distance_to(goal.pos)
            self.fitness = 1.0 / (distance_to_goal + 1)
        
    def two_point_crossover(self, parent_b):
      start = random.randint(0, BRAIN_SIZE - 1)
      end = random.randint(0, BRAIN_SIZE - 1)
      if start > end:
        start, end = end, start 
      child1 = (self.Brain.directions[:start] + parent_b.Brain.directions[start:end] + self.Brain.directions[end:])
      child2 = (parent_b.Brain.directions[:start] + self.Brain.directions[start:end] + parent_b.Brain.directions[end:])
      return child1, child2