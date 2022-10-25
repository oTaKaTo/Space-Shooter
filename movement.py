from settings import *

class Bounce:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice([-1, 1])

    def run(self, i, rect):
        if self.x[i] < WIDTH - rect[2] and self.direction[i] == 1:
            self.x[i] += 3 * self.direction[i]
            if self.x[i] > WIDTH - rect[2]:
                    self.direction[i] = -1

        if self.x[i] > 0 and self.direction[i] == -1:
            self.x[i] += 3 * self.direction[i]
            if self.x[i] <= 1:
                    self.direction[i] = 1
