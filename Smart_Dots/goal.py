import pygame
from settings import WIDTH, RED, WHITE

class Goal:
    def __init__(self):
        self.pos = pygame.Vector2((WIDTH - 4) // 2, 50)

    def show(self, screen):
        pygame.draw.circle(screen, RED, self.pos, 7)
        pygame.draw.circle(screen, WHITE, self.pos, 7, 2)