import pygame.draw

from settings import *
pygame.font.init()

class Text:
    def __init__(self,pos,fontsize = 32,color = (255,255,255),centered = False,font = "font/8Bit.ttf"):
        self.font = pygame.font.Font(font, fontsize)
        self.color = color
        self.centered = centered
        self.pos = pos
        self.contents = ""

    def update(self,text = ''):
        self.contents = text

    def run(self):
        text = self.font.render(self.contents,True, self.color)

        rect = (self.pos[0], self.pos[1], text.get_width(), text.get_height())
        if self.centered:
            x = self.pos[0] - text.get_width()/2
            y = self.pos[1] - text.get_height()/2
            rect = (x,y,text.get_width(),text.get_height())

        screen.blit(text, rect)