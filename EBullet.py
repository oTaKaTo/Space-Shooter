from settings import *

class New_bullet:
    def __init__(self, x, y , etype):
        self.damage = 10
        self.hitable = 1
        if etype == 0:
            self.x = x + 18
            self.y = y + 2
        elif etype == 1:
            self.x = x + 24
            self.y = y + 2
        elif etype == 2:
            self.x = x + 34
            self.y = y + 2
        self.speed = 1000
        # self.state = False
        self.type = 3 # 0 laser  1 cannon  2 ball   3 enemy
        self.value = 0

        # Animation change time
        self.totaltime = 0
        self.change_time = 50/1000
        self.hitbox = pygame.Rect(self.x+20 ,self.y,64, 64)

        self.laser = laser
        self.cannon = cannon
        self.ball = ball


    def update(self,prect):
        self.totaltime += dt
        if self.type == 0:
            self.speed = 3000 * dt
            if self.value >= len(self.laser):
                self.value = 0
            self.bulletImg = self.laser[self.value]
            self.bulletImg = pygame.transform.scale(self.bulletImg, (64, 64))

        if self.type == 1:
            self.speed = 2000 * dt
            if self.value >= len(self.cannon):
                self.value = 0
            self.bulletImg = self.cannon[self.value]
            self.bulletImg = pygame.transform.scale(self.bulletImg, (64, 64))

        if self.type == 2:
            self.speed = 1000 * dt
            if self.value >= len(self.ball):
                self.value = 0
            self.bulletImg = self.ball[self.value]
            self.bulletImg = pygame.transform.scale(self.bulletImg, (64, 64))

        if self.type == 3:
            self.speed = 1000 * dt
            self.bulletImg = enemy_bullet
            self.bulletImg = pygame.transform.scale(self.bulletImg, (12, 32))
        # key = pygame.key.get_pressed()
        # if key[pygame.K_SPACE] and self.state == False or pygame.mouse.get_pressed()[0] and self.state == False :
        #     self.state = True
        #     self.x = x + 2
        #     self.y = y + 10
        # if self.state:
        self.y += self.speed
        if self.totaltime >= self.change_time:
            self.value += 1
            self.totaltime = 0
        if self.y >= HEIGHT + 100:
            del self


    def draw(self):
        screen.blit(self.bulletImg, (self.x, self.y))
        if self.type == 1 :
            self.hitbox = pygame.Rect(self.x+19 , self.y+12, 26, 30)
        elif self.type == 0 :
            self.hitbox = pygame.Rect(self.x + 24, self.y, 16, 64)
        elif self.type == 2:
            self.hitbox = pygame.Rect(self.x+16 , self.y+16, 32, 32)
        else :
            self.hitbox = pygame.Rect(self.x , self.y, 12, 32)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def run(self,prect):
        self.update(prect)
        if self.hitable:
            self.draw()