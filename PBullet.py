from settings import *

class Pbullet:
    def __init__(self, x, y,type,plevel):

        self.damage = 10
        self.level = plevel
        self.x = x + 2
        self.y = y + 10
        self.waveoffset = random.random() * 6
        self.speed = 1000 * dt
        self.hitable = 1
        # self.state = False
        self.type = type # 0 laser  1 cannon  2 ball

        # Damage
        if self.type == 1:
            self.damage = 200 * (self.level/ 5)
        elif self.type == 2:
            self.damage = (4.5 + ((self.level - 1)/6.5))
        elif self.type == 0:
            self.damage = 10 * (1 + (self.level / 1.8))

        # Animation change time
        self.totaltime = 0
        self.value = 0
        self.change_time = 75/1000

        self.laser = laser
        self.cannon = cannon
        self.ball = ball

        self.hitbox = pygame.Rect(self.x+20 ,self.y,64, 64)


    def update(self):
        self.totaltime += dt
        if self.type == 0:
            self.speed = 6500 * dt
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
        # key = pygame.key.get_pressed()
        # if key[pygame.K_SPACE] and self.state == False or pygame.mouse.get_pressed()[0] and self.state == False :
        if self.type == 2:
            self.x -= self.speed*(4*math.sin(self.y/32+self.waveoffset))
            self.y -= self.speed
        else:
            self.y -= self.speed

        if self.totaltime >= self.change_time:
            self.value += 1
            self.totaltime = 0

        # Out of vision
        if self.y <= -64:
            del self

    def draw(self):
        screen.blit(self.bulletImg, (self.x, self.y))
        if self.type == 1 :
            self.hitbox = pygame.Rect(self.x+19 , self.y+12, 26, 30)
        elif self.type == 0 :
            self.hitbox = pygame.Rect(self.x + 24, self.y, 16, 64)
        else:
            self.hitbox = pygame.Rect(self.x+16 , self.y+16, 32, 32)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def run(self):
        self.update()
        if self.hitable == 1:
            self.draw()