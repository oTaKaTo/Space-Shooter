from settings import *

class Item:
    def __init__(self, x, y , etype):

        # image of items
        self.lasergun = lasergun
        self.heavybull = heavybull
        self.plasmaball = plasmaball
        self.hpotion = Hpotion
        self.rapidMode = Rapid
        self.xpboost = xpboost


        self.hitable = 1

        ''' 1 = Lasergun 2 = Heavybullet 3 = Plasmaball 4 = HP potion 5 = Rapidfire 6 = XP_boost'''
        rand_type = random.randint(1,6)
        if etype == 0:
            self.x = x + 18
            self.y = y + 2
        elif etype == 1:
            self.x = x + 24
            self.y = y + 2
        elif etype == 2:
            self.x = x + 34
            self.y = y + 2

        if rand_type == 1:
            self.type = 1
            self.image = self.lasergun
        elif rand_type == 2:
            self.type = 2
            self.image = self.heavybull
        elif rand_type == 3:
            self.type = 3
            self.image = self.plasmaball
        elif rand_type == 4:
            self.type = 4
            self.image = self.hpotion
        elif rand_type == 5:
            self.type = 5
            self.image = self.rapidMode
        elif rand_type == 6:
            self.type = 6
            self.image = self.xpboost
        self.image = pygame.transform.scale(self.image, (32, 32))


        self.speed = 1000


        self.hitbox = pygame.Rect(self.x ,self.y,32, 32)





    def update(self,prect):
        if self.type == 1:
            self.speed = 400 * dt


        if self.type == 2:
            self.speed = 400 * dt


        if self.type == 3:
            self.speed = 400 * dt


        if self.type == 4:
            self.speed = 400 * dt

        if self.type == 5:
            self.speed = 400 * dt

        if self.type == 6:
            self.speed = 400 * dt
        self.y += self.speed


    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        if self.type == 1 :
            self.hitbox = pygame.Rect(self.x, self.y, 32, 32)
        elif self.type == 2 :
            self.hitbox = pygame.Rect(self.x, self.y, 32, 32)
        elif self.type == 3:
            self.hitbox = pygame.Rect(self.x , self.y, 32, 32)
        elif self.type == 4:
            self.hitbox = pygame.Rect(self.x , self.y, 32, 32)
        elif self.type == 5:
            self.hitbox = pygame.Rect(self.x, self.y, 32, 32)
        elif self.type == 6:
            self.hitbox = pygame.Rect(self.x, self.y, 32, 32)
        #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def run(self,prect):
        self.update(prect)
        if self.hitable:
            self.draw()