import pygame
from population import Population
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Dots")

# img = pygame.image.load('gfg_image.jpg')

# Set image as icon
# pygame.display.set_icon(img)

clock = pygame.time.Clock()

Pop = Population()

goal = pygame.Vector2((WIDTH - 4) // 2, 50)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    Pop.update()
    Pop.show(screen)

    pygame.draw.circle(screen, RED, goal, 7)
    pygame.draw.circle(screen, BLACK, goal, 7, 2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()