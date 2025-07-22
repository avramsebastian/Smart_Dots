import pygame
from population import Population
from goal import Goal
from settings import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smart Dots")

    # img = pygame.image.load('gfg_image.jpg')
    # pygame.display.set_icon(img)

    clock = pygame.time.Clock()
    Pop = Population()
    goal = Goal()

    running = True
    while running:
        screen.fill(WHITE)

        goal.show(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if Pop.check_all_dots_dead():
            Pop.new_generation(goal)
        else:
            Pop.update(goal)
            Pop.show(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()