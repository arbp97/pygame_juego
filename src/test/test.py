import sys
import os
import pygame
# pylint: disable=no-name-in-module
from managers import Control

# pylint: disable=no-member
pygame.init()
# pylint: enable=no-member

main = Control(800,800)

main.main_loop()
