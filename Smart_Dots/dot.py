import pygame
import random
from brain import Brain
from obstacles import Obstacles
from goal import Goal
from settings import HEIGHT, WIDTH, CYAN, BRAIN_SIZE, GREEN

obstacles = Obstacles()
goal = Goal()

class Dot :
    def __init__(self) :
        self.pos = pygame.Vector2(WIDTH // 2, 600)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.color = CYAN
        self.size = 3
        self.Brain = Brain()
        self.rect = pygame.Rect(self.pos[0] - self.size, self.pos[1] - self.size, self.size * 2, self.size * 2)
        self.dead = False
        self.fitness = 0
        self.reach_goal = False
        self.champion = False
        self.passed_obstacles = set()

    def show(self, screen) :
        if self.champion:
            self.color = GREEN
            self.size = 4
        else:
            self.color = CYAN
            self.size = 3
        pygame.draw.circle(screen,self.color,(self.pos[0],self.pos[1]),self.size)

    def reset(self):
        self.pos = pygame.Vector2(WIDTH // 2, 600)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.dead = False
        self.fitness = 0
        self.reach_goal = False
        self.Brain.step = 0
        self.rect = pygame.Rect(self.pos[0] - self.size, self.pos[1] - self.size, self.size * 2, self.size * 2)
        self.passed_obstacles.clear()

    def move(self):
        if len(self.Brain.directions) > self.Brain.step :
            self.acc = pygame.Vector2(self.Brain.directions[self.Brain.step])
            self.Brain.step += 1
        else :
            self.dead = True
        self.vel += self.acc
        self.vel.clamp_magnitude_ip(5)
        self.pos += self.vel

    def update(self):
        if not self.dead and not self.reach_goal:
            self.move()
            for i, obs in enumerate(obstacles.obs_list):
                if self.pos[1] < obs.top:
                    self.passed_obstacles.add(i)
            self.rect.center = (int(self.pos[0]), int(self.pos[1]))
            if self.pos[0] < 2 or self.pos[1] < 2 or self.pos[0] > WIDTH - 2 or self.pos[1] > HEIGHT - 2 :
                self.dead = True
            elif any(self.rect.colliderect(obs) for obs in obstacles.obs_list):
                self.dead = True 
            else:
                distance_to_goal = self.pos.distance_to(goal.pos)
                if distance_to_goal < 7 :
                    self.reach_goal = True

    def calculate_fitness(self):
        distance_to_goal = self.pos.distance_to(goal.pos)
        reward = len(self.passed_obstacles) * 5.0
        if self.reach_goal:
            self.fitness = 10000.0 / (self.Brain.step + 1) + reward
        else:
            self.fitness = (10.0 / (distance_to_goal + 1)) + (self.Brain.step / BRAIN_SIZE) + reward
        
    def two_point_crossover(self, parent_b):
      start = random.randint(0, BRAIN_SIZE - 1)
      end = random.randint(0, BRAIN_SIZE - 1)
      if start > end:
        start, end = end, start 
      child1 = (self.Brain.directions[:start] + parent_b.Brain.directions[start:end] + self.Brain.directions[end:])
      child2 = (parent_b.Brain.directions[:start] + self.Brain.directions[start:end] + parent_b.Brain.directions[end:])
      return child1, child2