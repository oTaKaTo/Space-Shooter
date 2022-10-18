import pygame
import random
import pygame.key
import math

# screen

# Background
bg = pygame.image.load("pic/bg.jpg")

#RGB color


# setting windows
screen = pygame.display.set_mode((800, 1000))
WIDTH = 800
HEIGHT = 1000
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("pic/icon.png")
pygame.display.set_icon(icon)


# Clock
clock = pygame.time.Clock()
dt = clock.tick(144) /1000