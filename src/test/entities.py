import pygame
import os


class Ball:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(os.path.join('res','ball.png'))
        self.rect = self.get_area()

    def get_area(self):
        return self.image.get_rect()

    def move(self, x, y):
        self.rect = self.rect.move(x, y)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect, 0)


class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self,screen,color):
        pygame.draw.rect(screen, color, self.rect, 0)
