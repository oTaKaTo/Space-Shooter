import pygame.mixer_music
from leaderboard import *
from enemy import *
from settings import *
from bullet import *
from player import *
from menu import *

music_play = 1

# class setup
p = Player()
b = Bullet()
e = Enemy()
m = Menu()
l = Leaderboard()

# Game Loop
running = True
# 1 = menu, 2 = leaderboard, 3 = game
game_state = 1

while running:


    # RGB = Red ,Green ,Blue
    # Clear Screen
    screen.fill((0, 0, 0))
    # Draw Background
    for i in range(panels):
        screen.blit(bg, (0, i * bg_height + scroll - bg_height))
    scroll += 1
    if abs(scroll) > bg_height:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ending State !
    if p.gameover == 1 :
        game_state = 1
        del p
        del e
        del b
        del m
        p = Player()
        e = Enemy()
        b = Bullet()
        m = Menu()



    if game_state == 1:
        pygame.mouse.set_visible(True)
        if music_play:
            pygame.mixer.music.load("sound/home.wav")
            pygame.mixer.music.play(-1)
            music_play = 0
        m.draw(font, main_font)
        # If mouse click start
        if m.game_state:
            game_state = 3
        if m.score_state:
            game_state = 2
        if m.quit:
            running = False
    print(m.game_state)
    print(m.score_state)
    print(game_state)
    print("----------")
    if game_state == 2:
        l.draw()
        # If mouse click start
        if l.back:
            m.score_state = 0
            game_state = 1
            l.back = 0






    if game_state == 3:
        pygame.mouse.set_visible(False)
        if music_play == 0:
            pygame.mixer.music.unload()
            pygame.mixer.music.load("sound/aggravate_bgm2.wav")
            pygame.mixer.music.play(-1)
            music_play = 1
        #b.run(p.x, p.y)
        e.run(p.rect, p.bullets , p.x , p.y)
        p.run(e.rect, e.numbers ,e.bullets,e.KP)

    clock.tick(60)



    pygame.display.update()