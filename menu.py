import pygame

from settings import *
from button import *
class Menu:
    def __init__(self):
        self.run = 1
        self.game_state = 0
        self.start = 0

    def draw(self, font, label_font):

        #start = font.render("START", True,(255,255,255))
        label = label_font.render("SPACE SHOOTER", 1, (255, 255, 255))

        start = Button((WIDTH/3, HEIGHT/2,120,60),white,"START",24,screen,border_color=white,border_width=4)
        screen.blit(label, (WIDTH / 2 - label.get_width() / 2, 250))
        name = font.render("65010373 Takdanai Deephuak", 1, (255, 255, 255))
        screen.blit(name, (10, HEIGHT-30))
        pos = [-100,-100]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.run = False
            if keys[pygame.K_BACKSPACE]:
                self.run = False
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
        start.run(pos)
        if start.clicked:
            print("Clicked")
            self.game_state = 1
            self.start = 1





