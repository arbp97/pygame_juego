import pygame
import os
import math

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, img):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.jump_speed = 0
        self.is_jumping = False
        self.image, self.rect = img

    def move(self, x, y):
        self.rect = self.rect.move(x, y)

    def jump(self):
        if math.floor(self.jump_speed) != 0:
            self.is_jumping = True

        if self.is_jumping:
            self.jump_speed = -10
            self.is_jumping = True

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect, 0)

    def update(self):
        self.jump_speed += 0.4
        self.move(0, self.jump_speed)

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self,screen,color):
        pygame.draw.rect(screen, color, self.rect, 0)
