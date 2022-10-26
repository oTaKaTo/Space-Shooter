from settings import *

class Score:
    def __init__(self):
        self.score_value = 0

    def show_score(self):
        self.score_text = font.render("Score : " + str(self.score_value), True, (255, 255, 255))
        screen.blit(self.score_text, (600, 10))
