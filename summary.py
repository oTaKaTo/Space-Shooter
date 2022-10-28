import json

import pygame
from operator import itemgetter
from text import *
from settings import *

class Summary:
    def __init__(self, score = 0,level = 1):
        self.score = str(score)
        self.level = str(level)
        self.text = ""

        self.decor1 = Text((WIDTH/2, 150, WIDTH/2,HEIGHT/2),centered=True,fontsize=50) # Score
        self.playerScore = Text((WIDTH/2,250,WIDTH/2,HEIGHT/2),centered=True,fontsize=100)
        self.decor2 = Text((WIDTH/2,360,WIDTH/2,HEIGHT/2),centered=True,fontsize=50) # LEVEL
        self.playerLevel = Text((WIDTH/2,450,WIDTH/2,HEIGHT/2),centered=True,fontsize=50)
        self.decor3 = Text((WIDTH / 2, 600, WIDTH / 2, HEIGHT / 2), centered=True, fontsize=30)  # Enter your name
        self.playerName = Text((WIDTH/2,700,WIDTH/2,HEIGHT/2),centered=True, fontsize=30)

        self.id = "summary"
        self.click = 0

        self.coolDownTime = 0.08
        self.isCooldown = False
        self.startDel = 0

    def update(self):
        self.decor1.update("SCORE")
        self.decor2.update("LEVEL")
        self.decor3.update("Enter your name")
        self.playerName.update(self.text)
        self.playerScore.update(self.score)
        self.playerLevel.update(self.level)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.click = 1
                    if self.text.replace(" ","") ==  "":
                        self.text = "Unknown"
                    with open('score.json', 'r') as file:
                        playerScore = json.load(file)

                    playerScore.append([self.text,int(self.level),int(self.score)])
                    playerScore = sorted(playerScore,reverse= True, key=itemgetter(2))
                    if len(playerScore) > 5:
                        playerScore.pop()

                    with open('score.json', 'w+') as file:
                        json.dump(playerScore,file,indent=4)

                elif not event.key == pygame.K_BACKSPACE:
                    self.text += event.unicode
                    print(event)


        if pygame.key.get_pressed()[pygame.K_BACKSPACE] and not self.isCooldown:
            self.isCooldown = True
            self.startDel = pygame.time.get_ticks()
            if len(self.text) <= 1:
                self.text = ""
            else:
                self.text = self.text[:-1]

        if len(self.text) > 15:
            self.text = self.text[:15]

        if (pygame.time.get_ticks() - self.startDel)/1000 >= self.coolDownTime and self.isCooldown:
            self.isCooldown = False

    def run(self):
        self.click = 0
        self.update()
        self.decor1.run()
        self.decor2.run()
        self.decor3.run()
        self.playerLevel.run()
        self.playerName.run()
        self.playerScore.run()