import pygame
from settings import WIDTH, HEIGHT, PURPLE

class Obstacles:
   def __init__(self):
      self.obs_list = []
      self.obstacle_width = int(WIDTH * 0.7)
      self.obstacle_height = 20
      self.add_obstacle()

   def add_obstacle(self):
      obstacle1_x = 0
      obstacle1_y = int(HEIGHT * 0.3)
      obstacle1 = pygame.Rect(obstacle1_x, obstacle1_y, self.obstacle_width, self.obstacle_height)
      self.obs_list.append(obstacle1)
      obstacle2_x = int(WIDTH * 0.3)
      obstacle2_y = int(HEIGHT * 0.6)
      obstacle2 = pygame.Rect(obstacle2_x, obstacle2_y, self.obstacle_width, self.obstacle_height)
      self.obs_list.append(obstacle2)
      
   def show(self, screen):
      for obstacle in self.obs_list :
         pygame.draw.rect(screen, PURPLE, obstacle)