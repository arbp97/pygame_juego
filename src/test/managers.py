import pygame
import os
import sys
# pylint: disable=no-name-in-module
from entities import Character, Wall


class Control:
    def __init__(self, screen_width, screen_height):
        self.display = pygame.display.set_mode((screen_width, screen_height))
        self.fpsClock = pygame.time.Clock()
        self.char = Character(0, 510, 6, self.load_image(
            "adventurer/adventurer-idle-00.png", -1))
        self.wall_list = [Wall(0, 500, screen_width+300, 100)]
        self.background = pygame.Surface(self.display.get_size())
        self.background = pygame.image.load("res/background.png")
        self.background = self.background.convert()
        self.sprites = pygame.sprite.RenderPlain(self.char)

    def check_events(self):
        # pylint: disable=no-member
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if(keys[pygame.K_LEFT]):
            self.char.going_right = False
            self.char.going_left = True
            self.char.view = False
            self.char.move(-self.char.speed, 0)
            self.check_collisions(-self.char.speed, 0)
            self.char.walk_count += 0.5

        elif(keys[pygame.K_RIGHT]):
            self.char.going_left = False
            self.char.going_right = True
            self.char.view = True
            self.char.move(self.char.speed, 0)
            self.check_collisions(self.char.speed, 0)
            self.char.walk_count += 0.5

        else:
            self.char.going_right = False
            self.char.going_left = False
            self.char.idle_count += 0.5

        if(keys[pygame.K_SPACE]):
            self.char.jump()
            self.check_collisions(0, self.char.jump_speed)
            self.char.walk_count = 0
            self.char.jump_count += 0.5
        # pylint: enable=no-member

    def check_collisions(self, x, y):

        for wall in self.wall_list:
            if self.char.rect.colliderect(wall.rect):
                if x != 0:
                    if x > 0:
                        self.char.rect.right = wall.rect.left
                    else:
                        self.char.rect.left = wall.rect.right

                if y != 0:
                    self.char.jump_speed = 0
                    if y > 0:
                        self.char.rect.bottom = wall.rect.top
                        self.char.is_jumping = False
                    else:
                        self.char.rect.top = wall.rect.bottom

    def load_image(self, name, colorkey=None):
        fullname = os.path.join("res", name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error:
            print("Cannot load image:", fullname)
            raise SystemExit()
        image = image.convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image, image.get_rect()

    def main_loop(self):

        while 1:

            self.fpsClock.tick(30)

            self.check_events()

            self.char.update()
            self.check_collisions(0, self.char.jump_speed)

            # self.display.fill((0,0,0))
            self.display.blit(self.background, (0, 0))

            self.sprites.draw(self.display)
            # self.display.blit(self.char.image,(self.char.rect.x,self.char.rect.y))

            for wall in self.wall_list:
                wall.draw(self.display, (100, 100, 100))

            pygame.display.update()
