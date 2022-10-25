import pygame

from PBullet import Pbullet
from settings import *
from healthbar import *
from enemy import *

class Player:
    def __init__(self):
        self.Max_HP = 100
        self.HP = 100
        self.XP = 0
        self.level = 1
        self.x = 370
        self.y = 850

        self.gameover = 0

        # invisible after be hit
        self.invisible_time = 0.2
        self.invis_cooldown = 0
        self.invis_timer = 0

        # bullet systems
        self.bullets = []
        self.delay = 0.1
        self.count_time = 0
        self.type = 0
        self.weapon_change_cooldown = 0
        self.weapon_change_timer = 0
        self.weapon_change_time = 5

        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        self.speed = 500 * dt
        self.playerImg = pygame.image.load("pic/player/ship/base/png/full_hp.png")
        self.playerImg = pygame.transform.scale(self.playerImg, (64, 64))
        self.rect = self.playerImg.get_rect()
        # Health bar class
        self.hb = Healthbar(self.Max_HP, self.HP)
    def create_bullets(self, x, y,type):
        self.bullets.append(Pbullet(x, y,type))

    def update(self, erect, enum , ebull):
        invictimer = 0
        self.count_time += dt
        if  pygame.mouse.get_focused():
            self.x, self.y = pygame.mouse.get_pos()
            self.x -= 28
            self.y -= 22
        key = pygame.key.get_pressed()
        # if key[pygame.K_a] or key[pygame.K_LEFT]:
        #     self.x -= self.speed
        # if key[pygame.K_d] or key[pygame.K_RIGHT]:
        #     self.x += self.speed
        # if key[pygame.K_w] or key[pygame.K_UP]:
        #     self.y -= self.speed
        # if key[pygame.K_s] or key[pygame.K_DOWN]:
        #     self.y += self.speed

        if key[pygame.K_SPACE] and self.count_time >= self.delay or pygame.mouse.get_pressed()[0] and self.count_time >= self.delay :
            self.count_time = 0
            pshoot.play()
            self.create_bullets(self.x, self.y,self.type)

        # Bullet type change
        if key[pygame.K_q] and self.weapon_change_cooldown == 0:
            self.type = 0
            self.delay = 0.1
            self.weapon_change_cooldown = 1
        if key[pygame.K_w] and self.weapon_change_cooldown == 0:
            self.type = 1
            self.delay = 0.3
            self.weapon_change_cooldown = 1
        if key[pygame.K_e] and self.weapon_change_cooldown == 0:
            self.type = 2
            self.delay = 0.3
            self.weapon_change_cooldown = 1
        if self.weapon_change_cooldown == 1:
            self.weapon_change_timer += dt
            if self.weapon_change_timer >= self.weapon_change_time:
                self.weapon_change_cooldown = 0
                self.weapon_change_timer = 0


        # hp test
        if key[pygame.K_UP]:
            self.HP += 10
            self.hb.get_health(10)
            if self.HP >= 100:
                self.HP = 100
        if key[pygame.K_DOWN]:
            self.HP -= 10
            self.hb.get_damage(10)


        for bullet in self.bullets:
            bullet.run()

        # rect update
        self.rect.x = self.x
        self.rect.y = self.y

        # boundary
        if self.x <= 0:
            self.x = 0
        if self.x >= 736:
            self.x = 736
        if self.y >= 936:
            self.y = 936
        if self.y <= 0:
            self.y = 0
        # Collision
        if len(erect) >= 1:
            # Enemy crash collision
            for i in range(enum):

                if self.rect.colliderect(erect[i]):
                    print("D A M A G E")
                    if self.invis_cooldown == 0:
                        self.HP -= 10
                        self.hb.get_damage(10)
                        phit.play()
                        self.invis_cooldown = 1

            # Enemy bullet collision
            for ebullet in ebull:
                if ebullet.hitbox.colliderect(self.hitbox):
                    print("Enemy Bullet collision happened !")
                    if self.invis_cooldown == 0:
                        self.HP -= 10
                        self.hb.get_damage(10)
                        phit.play()
                        self.invis_cooldown = 1

            if self.invis_cooldown == 1:
                self.invis_timer += dt
                if self.invis_timer >= self.invisible_time :
                    self.invis_timer = 0
                    self.invis_cooldown = 0

        if self.HP <= 0 :
            self.gameover = 1
    def draw_gui(self):
        self.hb.update()
    def draw_player(self):
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        screen.blit(self.playerImg, (self.x , self.y))
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def run(self, erect, enum , ebull):
        self.update(erect, enum , ebull)
        self.draw_player()
        self.draw_gui()
