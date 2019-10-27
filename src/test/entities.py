import pygame
import os
import math

char_idle_right = [pygame.image.load("res/adventurer/adventurer-idle-00.png"),pygame.image.load("res/adventurer/adventurer-idle-01.png"),
                    pygame.image.load("res/adventurer/adventurer-idle-02.png"),pygame.image.load("res/adventurer/adventurer-idle-03.png")]

char_idle_left = [pygame.image.load("res/adventurer/adventurer-idle-00-left.png"),pygame.image.load("res/adventurer/adventurer-idle-01-left.png"),
                    pygame.image.load("res/adventurer/adventurer-idle-02-left.png"),pygame.image.load("res/adventurer/adventurer-idle-03-left.png")]

char_right = [pygame.image.load("res/adventurer/adventurer-run-00.png"), pygame.image.load("res/adventurer/adventurer-run-01.png"),
              pygame.image.load("res/adventurer/adventurer-run-02.png"), pygame.image.load("res/adventurer/adventurer-run-03.png"),
              pygame.image.load("res/adventurer/adventurer-run-04.png"), pygame.image.load("res/adventurer/adventurer-run-05.png")]

char_left = [pygame.image.load("res/adventurer/adventurer-run-00-left.png"), pygame.image.load("res/adventurer/adventurer-run-01-left.png"),
              pygame.image.load("res/adventurer/adventurer-run-02-left.png"), pygame.image.load("res/adventurer/adventurer-run-03-left.png"),
              pygame.image.load("res/adventurer/adventurer-run-04-left.png"), pygame.image.load("res/adventurer/adventurer-run-05-left.png")]

char_jump_right = [pygame.image.load("res/adventurer/adventurer-jump-00.png"),pygame.image.load("res/adventurer/adventurer-jump-01.png"),
                    pygame.image.load("res/adventurer/adventurer-jump-02.png"),pygame.image.load("res/adventurer/adventurer-jump-03.png")]

char_jump_left = [pygame.image.load("res/adventurer/adventurer-jump-00-left.png"),pygame.image.load("res/adventurer/adventurer-jump-01-left.png"),
                    pygame.image.load("res/adventurer/adventurer-jump-02-left.png"),pygame.image.load("res/adventurer/adventurer-jump-03-left.png")]

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, img):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.jump_speed = 0
        self.is_jumping = False
        self.going_left = False
        self.going_right = False
        self.view = True # true -> right | false -> left
        self.walk_count = 0
        self.idle_count = 0
        self.jump_count = 0
        self.image, self.rect = img
        self.rect.x = x
        self.rect.y = y

    def move(self, x, y):
        self.rect = self.rect.move(x, y)

    def jump(self):
        if self.jump_speed >= 0 and not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = -12

    @DeprecationWarning
    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect, 0)

    def update(self):
        self.jump_speed += 1
        self.move(0, self.jump_speed)

        if self.is_jumping and (self.going_left or self.going_right):
            if self.jump_count > 3:
                self.jump_count = 0

            if self.view:
                self.image = char_jump_right[round(self.jump_count)]
            else:
                self.image = char_jump_left[round(self.jump_count)]

        elif self.going_right:
            if self.walk_count > 5:
                self.walk_count = 0
            self.image = char_right[round(self.walk_count)]

        elif self.going_left:
            if self.walk_count > 5:
                self.walk_count = 0
            self.image = char_left[round(self.walk_count)]

        elif self.is_jumping:
            if self.jump_count > 3:
                self.jump_count = 0

            if self.view:
                self.image = char_jump_right[round(self.jump_count)]
            else:
                self.image = char_jump_left[round(self.jump_count)]

        else:
            if self.idle_count > 3:
                self.idle_count = 0

            if self.view:
                self.image = char_idle_right[round(self.idle_count)]
            else:
                self.image = char_idle_left[round(self.idle_count)]
        #print(self.rect.x,self.rect.y)
        if self.rect.x > 900:
            self.update_position(-10,510)
        elif self.rect.x < -12:
            self.update_position(898,510)

    def update_position(self,x,y):
        self.rect.x = x
        self.rect.y = y



class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self,screen,color):
        pygame.draw.rect(screen, color, self.rect, 1)

class projectile:
    def __init__(self):
        self.x = 2 #TODO
