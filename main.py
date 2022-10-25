from enemy import *
from settings import *
from bullet import *
from player import *
from menu import *



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

    if p.gameover == 1 :
        game_state = 1

    if m.start == 1:
        game_state = 3

        p = Player()
        b = Bullet()
        e = Enemy()


    if game_state == 1:
        m.draw(font, main_font)

    if  game_state == 2:
        print("Score")
    if game_state == 3:
        #b.run(p.x, p.y)
        p.run(e.rect, e.numbers ,e.bullets)
        e.run(p.rect, p.bullets , p.x , p.y)

    clock.tick(60)



    pygame.display.update()