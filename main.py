from leaderboard import *
from enemy import *
from player import *
from menu import *
from summary import *
from how import *

music_play = 1

# class setup
p = Player()
e = Enemy()
m = Menu()
l = Leaderboard()
h = How()

# Game Loop
running = True
# 1 = menu, 2 = leaderboard, 3 = game 4 = Game over(summary)
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


    # Ending State !
    if p.gameover == 1 :
        pygame.mouse.set_visible(True)
        s = Summary(int(e.score.score_value),p.level)
        game_state = 4
        p.gameover = 0

    if game_state == 4:
        s.run()
        if s.click == 1:
            del p
            del e
            del m
            del s
            s = Summary()
            p = Player()
            e = Enemy()
            m = Menu()
            game_state = 1



    if game_state == 1:
        pygame.mouse.set_visible(True)
        if music_play:
            pygame.mixer.music.load("sound/home.wav")
            pygame.mixer.music.play(-1)
            music_play = 0
        m.draw(font, main_font)
        # If mouse click start
        if m.game_state:
            game_state = 5
            m.game_state = 0
        if m.score_state:
            game_state = 2
        if m.quit:
            running = False

    if game_state == 2:
        l.runner()
        # If mouse click start
        if l.back:
            m.score_state = 0
            l.back = 0
            game_state = 1

    # how to play screen
    if game_state == 5:
        h.draw()
        if h.play:
            game_state = 3
            h.play = 0
        if h.back:
            game_state = 1
            h.back = 0

    if game_state == 3:
        pygame.mouse.set_visible(False)
        if music_play == 0:
            pygame.mixer.music.unload()
            pygame.mixer.music.load("sound/aggravate_bgm2.wav")
            pygame.mixer.music.play(-1)
            music_play = 1

        e.run(p.rect, p.bullets , p.x , p.y ,p.level)
        p.run(e.rect, e.numbers ,e.bullets,e.KP,e.items)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    clock.tick(60)



    pygame.display.update()
exit()
