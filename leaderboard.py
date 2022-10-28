from settings import *
import json
from button import *
from text import *

class Leaderboard:
    def __init__(self):

        self.decor1 = Text((WIDTH / 2, 100, WIDTH / 2, HEIGHT / 2), centered=True, fontsize=50)
        self.decor2 = Text((157, 200, WIDTH / 2, HEIGHT / 2), centered=True, fontsize=32)
        self.decor3 = Text((110+360, 200, WIDTH / 2, HEIGHT / 2), centered=True, fontsize=32)
        self.decor4 = Text((110+550, 200, WIDTH / 2, HEIGHT / 2), centered=True, fontsize=32)

        self.run = 1
        self.back = 0

        self.id = "score"
    def draw(self):
        back = Button(((WIDTH - 120)/2, (HEIGHT*8.5/10 -60/2),120,60),white,"BACK",24,screen,border_color=white,border_width=4)
        back.run()
        if back.clicked:
            self.back = 1
    def update(self):

        self.decor1.update("LEADERBOARD")
        self.decor2.update("Name")
        self.decor3.update("Level")
        self.decor4.update("Score")
        with open('score.json', 'r') as file:
            self.playerScore = json.load(file)


        self.alltext = []
        for i,score in enumerate(self.playerScore):
            name = Text((110, 280+75*i, WIDTH / 2, HEIGHT / 2), fontsize=24)
            level = Text((110+340, 280+75*i, WIDTH / 2, HEIGHT / 2), fontsize=24)
            score = Text((110+500, 280+75*i, WIDTH / 2, HEIGHT / 2), fontsize=24)
            self.alltext.append([name,level,score])

    def runner(self):
        backButton = Button(((WIDTH - 120) / 2, (HEIGHT * 8.5 / 10 - 60 / 2), 120, 60), white, "BACK", 24, screen,
                                 border_color=white, border_width=4)
        self.update()
        self.decor1.run()
        self.decor2.run()
        self.decor3.run()
        self.decor4.run()
        for text,label in zip(self.playerScore,self.alltext):
            label[0].update(text[0])
            label[1].update(str(text[1]))
            label[2].update(str(text[2]))
            label[0].run()
            label[1].run()
            label[2].run()
        backButton.run()
        if backButton.clicked:
            self.back = 1