import pygame
from brain import Brain
from settings import HEIGHT, WIDTH, BLACK

class Dot :
    def __init__(self) :
        self.pos = pygame.Vector2(WIDTH // 2, HEIGHT // 2)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.color = BLACK
        self.size = 3
        self.Brain = Brain(200)
        self.dead = False

    def show(self, screen) :
        pygame.draw.circle(screen,self.color,(self.pos[0],self.pos[1]),self.size)

    def move(self):
        if len(self.Brain.directions) > self.Brain.step :
            self.acc = self.Brain.directions[self.Brain.step]
            self.Brain.step += 1
        else :
            self.dead = True

        self.vel += self.acc
        self.vel.clamp_magnitude_ip(5)
        self.pos += self.vel

    def update(self):
        if not self.dead :
            self.move()
            if self.pos[0] < 2 or self.pos[1] < 2 or self.pos[0] > WIDTH - 2 or self.pos[1] > HEIGHT - 2 :
                self.dead = True