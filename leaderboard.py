from settings import *
from button import *
class Leaderboard:
    class Scoredata:
        def __init__(self,line:list):
            self.name = line[0]
            self.level = int(line[1])
            self.score = int(line[2])

    def __init__(self):
        self.run = 1
        self.back = 0

    def draw(self):
        back = Button(((WIDTH - 120)/2, (HEIGHT*8.5/10 -60/2),120,60),white,"BACK",24,screen,border_color=white,border_width=4)
        back.run()
        if back.clicked:
            self.back = 1