import pygame

pygame.init()

screen = pygame.display.set_mode((600, 650))
pygame.display.set_caption("Smart Dots")

# img = pygame.image.load('gfg_image.jpg')

# Set image as icon
# pygame.display.set_icon(img)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,255,255))
    pygame.display.update()

pygame.quit()