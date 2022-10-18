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
# 1 = menu, 2 = leaderboard, 3 = game
game_state = 3

while running:
    clock.tick(60)
    # font
    font = pygame.font.Font('font/8Bit.ttf', 20)
    main_font = pygame.font.Font('font/8-BITWONDER.ttf' , 54)

    # RGB = Red ,Green ,Blue
    # Clear Screen
    screen.fill((0, 0, 0))
    # Draw Background
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if game_state == 1:
        m.draw(font,main_font)

    if  game_state == 2:
        print("D")
    if game_state == 3:
        b.run(p.x, p.y)
        p.run(e.rect, e.numbers)
        e.run(p.rect, b.hitbox , p.x , p.y)






    pygame.display.update()