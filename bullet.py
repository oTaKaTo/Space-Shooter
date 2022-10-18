import pygame

from settings import *
from player import *
from enemy import *

class Bullet:
    def __init__(self):
        self.damage = 10
        self.x = 0
        self.y = 0
        self.speed = 1000 * dt
        self.state = False
        self.type = 0 # 0 laser  1 cannon  2 ball
        self.value = 0

        # Animation change time
        self.totaltime = 0
        self.change_time = 50/1000
        self.hitbox = (self.x+20 ,self.y,64, 64)
        self.laser = [pygame.image.load("pic/bullet/laser/1.png"),
                              pygame.image.load("pic/bullet/laser/2.png"),
                              pygame.image.load("pic/bullet/laser/3.png"),
                              pygame.image.load("pic/bullet/laser/4.png"),
                              pygame.image.load("pic/bullet/laser/5.png"),
                              pygame.image.load("pic/bullet/laser/6.png"),
                              pygame.image.load("pic/bullet/laser/7.png"),
                              pygame.image.load("pic/bullet/laser/8.png")]

        self.cannon = [pygame.image.load("pic/bullet/canon/1.png"),
                       pygame.image.load("pic/bullet/canon/2.png"),
                       pygame.image.load("pic/bullet/canon/3.png"),
                       pygame.image.load("pic/bullet/canon/4.png")]

        self.ball = [pygame.image.load("pic/bullet/ball/1.png"),
                     pygame.image.load("pic/bullet/ball/2.png"),
                     pygame.image.load("pic/bullet/ball/3.png"),
                     pygame.image.load("pic/bullet/ball/4.png"),
                     pygame.image.load("pic/bullet/ball/5.png"),
                     pygame.image.load("pic/bullet/ball/6.png"),
                     pygame.image.load("pic/bullet/ball/7.png"),
                     pygame.image.load("pic/bullet/ball/8.png"),
                     pygame.image.load("pic/bullet/ball/9.png"),
                     pygame.image.load("pic/bullet/ball/10.png")]


    def update(self, x, y):
        self.totaltime += dt
        if self.type == 0:
            self.speed = 4000 * dt
            if self.value >= len(self.laser):
                self.value = 0
            self.bulletImg = self.laser[self.value]
            self.bulletImg = pygame.transform.scale(self.bulletImg, (64, 64))

        if self.type == 1:
            self.speed = 1000 * dt
            if self.value >= len(self.cannon):
                self.value = 0
            self.bulletImg = self.cannon[self.value]
            self.bulletImg = pygame.transform.scale(self.bulletImg, (64, 64))

        if self.type == 2:
            self.speed = 2500 * dt
            if self.value >= len(self.ball):
                self.value = 0
            self.bulletImg = self.ball[self.value]
            self.bulletImg = pygame.transform.scale(self.bulletImg, (64, 64))
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.state == False or pygame.mouse.get_pressed()[0] and self.state == False :
            self.state = True
            self.x = x + 2
            self.y = y + 10
        if self.state:
            self.y -= self.speed
            if self.totaltime >= self.change_time:
                self.value += 1
                self.totaltime = 0
        if self.y <= -100:
            self.state = False

    def draw(self):
        if self.state:
            screen.blit(self.bulletImg, (self.x, self.y))
            if self.type == 1 :
                self.hitbox = pygame.Rect(self.x+19 , self.y+12, 26, 30)
            elif self.type == 0 :
                self.hitbox = pygame.Rect(self.x + 24, self.y, 16, 64)
            else:
                self.hitbox = pygame.Rect(self.x+16 , self.y+16, 32, 32)
            pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def run(self,x,y):
        self.update(x, y)
        self.draw()