import pygame
import matplotlib.pyplot as plt 
import numpy as np
from population import Population
from goal import Goal
from obstacles import Obstacles
from settings import WIDTH, HEIGHT, BLACK, FPS, WHITE

def display_plots(best_steps, reached_goal, generations):
    x1points = np.array(best_steps)
    ypoints = np.array(generations)
    x2points = np.array(reached_goal)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor("black")

    ax1.set_facecolor("black")
    ax1.plot(x1points, ypoints, color = "lime")
    ax1.set_title("Steps To Reach The Goal Over Time", color = "white")
    ax1.set_xlabel("Steps", color = "white")
    ax1.set_ylabel("Generation", color = "white")
    ax1.tick_params(colors = "white")
    ax1.grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax1.invert_xaxis()

    ax2.set_facecolor("black")
    ax2.plot(x2points, ypoints, color = "lime")
    ax2.set_title("Dots That Reached The Goal Over Time", color = "white")
    ax2.set_xlabel("Dots Count", color = "white")
    ax2.set_ylabel("Generation", color = "white")
    ax2.tick_params(colors = "white")
    ax2.grid(True, color='gray', linestyle='--', linewidth=0.5)

    plt.show()

def genetic_algorithm(best_steps, reached_goal, generations):
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Smart Dots")

    # img = pygame.image.load('gfg_image.jpg')
    # pygame.display.set_icon(img)

    clock = pygame.time.Clock()
    Pop = Population()
    goal = Goal()
    obstacles = Obstacles()
    generation = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        goal.show(screen)
        obstacles.show(screen)

        if Pop.check_all_dots_dead():
            best_steps.append(Pop.max_steps)
            reached_goal.append(Pop.count_reached_goal())
            generations.append(generation)
            generation += 1
            Pop.new_generation()
        else:
            Pop.update()
            Pop.show(screen)

        font = pygame.font.SysFont("Segoe UI", 20, bold = False)
        gen_text = font.render(f"Generation: {generation}", True, WHITE) 

        text_rect = gen_text.get_rect()
        text_rect.topleft = (10, HEIGHT - text_rect.height - 10)  

        screen.blit(gen_text, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    

def main():
    best_steps = []
    reached_goal = []
    generations = []
    genetic_algorithm(best_steps, reached_goal, generations)
    display_plots(best_steps, reached_goal, generations)

if __name__ == "__main__":
    main()