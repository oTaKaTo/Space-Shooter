from enemy import *
from settings import *
from bullet import *
from player import *
from menu import *
import random

# initialize pygame
pygame.init()

# class setup
p = Player()
b = Bullet()
e = Enemy()
m = Menu()

# Game Loop
running = True
menu_state = 0
game_state = 1

while running:
    clock.tick(60)
    # font
    font = pygame.font.Font('font/8Bit.ttf', 20)

    # RGB = Red ,Green ,Blue
    # Clear Screen
    screen.fill((0, 0, 0))
    # Draw Background
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if menu_state == 0:
        m.draw(font)
    if game_state == 1:
        b.run(p.x, p.y)
        p.run(e.rect, e.numbers)
        e.run(p.rect, b.hitbox)






    pygame.display.update()