import pygame
import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np
from population import Population
from goal import Goal
from settings import WIDTH,HEIGHT,BLACK,FPS

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smart Dots")

    # img = pygame.image.load('gfg_image.jpg')
    # pygame.display.set_icon(img)

    clock = pygame.time.Clock()
    Pop = Population()
    goal = Goal()
    best_steps = []

    running = True
    while running:
        screen.fill(BLACK)

        goal.show(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if Pop.check_all_dots_dead():
            best_steps.append(Pop.max_steps)
            Pop.new_generation(goal)
        else:
            Pop.update(goal)
            Pop.show(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

    generations = list(range(0, len(best_steps)))
    xpoints = np.array(best_steps)
    ypoints = np.array(generations)

    fig, ax = plt.subplots()
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    ax.plot(xpoints, ypoints, color = "lime")
    ax.set_title("Steps To Reach The Goal Over Time", color = "white")
    ax.set_xlabel("Steps", color = "white")
    ax.set_ylabel("Generation", color = "white")
    ax.tick_params(colors = "white")
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5)

    plt.gca().invert_xaxis()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()