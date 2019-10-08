import pygame
import sys
# pylint: disable=no-name-in-module
from entities import Ball,Wall

class Control:
    def __init__(self,screen_width,screen_height):
        self.display = pygame.display.set_mode((screen_width,screen_height))
        self.ball = Ball(200,200, 5)
        self.floor = Wall(0,700,800,100)

    def check_events(self):
        # pylint: disable=no-member
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if(keys[pygame.K_LEFT]):
            self.ball.move(-self.ball.speed,0)

        if(keys[pygame.K_RIGHT]):
            self.ball.move(self.ball.speed,0)

        if(keys[pygame.K_UP]):
            self.ball.move(0,-self.ball.speed)

        if(keys[pygame.K_DOWN]):
            self.ball.move(0,self.ball.speed)
        # pylint: enable=no-member

        self.ball.move(0,0)

    def main_loop(self):

        while 1:

            self.check_events()

            self.display.fill((0,0,0))

            self.ball.draw(self.display,(0,0,0))
            self.display.blit(self.ball.image, self.ball.rect)

            self.floor.draw(self.display,(100,100,100))

            pygame.display.update()

            pygame.display.flip()