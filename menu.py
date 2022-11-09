from button import *
class Menu:
    def __init__(self):
        self.run = 1
        self.game_state = 0
        self.score_state = 0
        self.quit = 0


    def draw(self, font, label_font):

        start = Button(((WIDTH - 120)/2, (HEIGHT*5/10 -60/2),120,60),white,"START",24,screen,border_color=white,border_width=4)
        score = Button(((WIDTH - 200)/2, (HEIGHT*6.25/10 - 60/2),200,60),white,"SCOREBOARD",24,screen,border_color=white,border_width = 4)
        quit = Button(((WIDTH - 120)/2, (HEIGHT*7.5/10 - 60/2),120,60),white,"QUIT",24,screen,border_color=white,border_width = 4)

        label = label_font.render("SPACE SHOOTER", 1, (255, 255, 255))
        screen.blit(label, (WIDTH / 2 - label.get_width() / 2, 250))

        name = font.render("65010373 Takdanai Deephuak", 1, (255, 255, 255))
        screen.blit(name, (10, HEIGHT-30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.run = False
            if keys[pygame.K_BACKSPACE]:
                self.run = False
        start.run()
        score.run()
        quit.run()
        if start.clicked:
            click_sound.play()
            self.game_state = 1
        if score.clicked :
            self.score_state = 1
            click_sound.play()
        if quit.clicked:
            click_sound.play()
            self.quit = 1





