from settings import *

class Score:
    def __init__(self):
        self.score_value = 0
        self.score_int = int(self.score_value)

    def show_score(self):
        self.score_int = int(self.score_value)
        self.score_text = font.render("Score : " + str(self.score_int), True, (255, 255, 255))
        screen.blit(self.score_text, (600, 10))
