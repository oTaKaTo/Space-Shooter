import pygame
from button import *
from PBullet import Pbullet
from xpbar import *
from healthbar import *
from enemy import *
from settings import *

class Player:
    def __init__(self):
        self.x = 370
        self.y = 850

        self.gameover = 0

        self.XP = 0
        self.Max_XP = 10
        self.level = 1
        self.last_xp = 0
        self.diff_xp = 0
        self.cur_xp = 0
        self.level_text = ""

        self.Max_HP = 100
        self.HP = 100
        # invisible after be hit
        self.invisible_time = 0.2
        self.invis_cooldown = 0
        self.invis_timer = 0

        # rapid item
        self.rapid = 1
        self.rapid_duration = 2
        self.rapid_timer = 0

        #xp boost item
        self.xp_boost = 1
        self.xp_boost_timer = 0
        self.xp_boost_duration = 3


        # bullet systems
        self.bullets = []
        self.delay = 0.1 * self.rapid
        self.count_time = 0
        self.type = 0
        self.weapon_change_cooldown = 0
        self.weapon_change_timer = 0
        self.weapon_change_time = 5

        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        self.speed = 1000 * dt
        self.playerImg = pygame.image.load("pic/player/ship/base/png/full_hp.png")
        self.playerImg = pygame.transform.scale(self.playerImg, (64, 64))
        self.rect = self.playerImg.get_rect()
        # Health , xp bar class
        self.hb = Healthbar(self.Max_HP, self.HP)
        self.xp = XPbar(self.Max_XP, self.XP)
    def create_bullets(self, x, y,type,plevel):
        self.bullets.append(Pbullet(x, y,type,plevel))

    def stop_sound(self):
        plasma_shoot.stop()
        pshoot.stop()
        heavy_shoot.stop()


    def show_level(self):
        self.level_text = font.render("level : " + str(self.level), True, (255, 255, 255))
        screen.blit(self.level_text, (600, 40))

    def update(self, erect, enum , ebull , KP , items):

        if self.type == 0:
            self.delay = 0.07 * self.rapid
        elif self.type == 1:
            if self.level <= 10:
                self.delay = 0.3
            else:
                self.delay = (0.3 / (self.level/10)) * self.rapid
        elif self.type == 2:
            self.delay = 0.4 * self.rapid



        # Level system
        self.Max_HP = 100 + ((self.level - 1) * 5)

        self.last_xp = self.XP
        self.XP = KP
        self.diff_xp = (self.XP - self.last_xp) * self.xp_boost
        if self.diff_xp >= 1 :
            self.xp.get_xp(self.diff_xp)
            self.cur_xp += self.diff_xp
            self.diff_xp = 0

        # level up
        if self.cur_xp >= self.Max_XP :
            self.level += 1
            self.HP += 10
            self.hb.get_health(10)
            if self.HP >= self.Max_HP:
                self.HP = self.Max_HP
            level_up.play()
            self.cur_xp = 0
            self.xp.get_damage(self.Max_XP)
            self.Max_XP += 5 * int(self.level/2)

        invictimer = 0
        self.count_time += dt
        if  pygame.mouse.get_focused():
            self.x, self.y = pygame.mouse.get_pos()
            self.x -= 28
            self.y -= 22
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
             self.x -= self.speed
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
             self.x += self.speed
        if key[pygame.K_w] or key[pygame.K_UP]:
             self.y -= self.speed
        if key[pygame.K_s] or key[pygame.K_DOWN]:
             self.y += self.speed

        if key[pygame.K_SPACE] and self.count_time >= self.delay or pygame.mouse.get_pressed()[0] and self.count_time >= self.delay :
            self.count_time = 0
            if self.type == 0:
                self.stop_sound()
                pshoot.play()
            elif self.type == 1:
                self.stop_sound()
                heavy_shoot.play()
            elif self.type == 2:
                self.stop_sound()
                plasma_shoot.play()
            self.create_bullets(self.x, self.y,self.type , self.level)

        # Bullet type change
        #if key[pygame.K_z] and self.weapon_change_cooldown == 0:
        #    self.type = 0
        #    self.weapon_change_cooldown = 1
        #if key[pygame.K_x] and self.weapon_change_cooldown == 0:
        #    self.type = 1
        #    self.weapon_change_cooldown = 1
        #if key[pygame.K_c] and self.weapon_change_cooldown == 0:
        #    self.type = 2
        #    self.weapon_change_cooldown = 1
        #if self.weapon_change_cooldown == 1:
        #    self.weapon_change_timer += dt
        #    if self.weapon_change_timer >= self.weapon_change_time:
        #        self.weapon_change_cooldown = 0
        #        self.weapon_change_timer = 0

        # Level test
        #if key[pygame.K_UP]:
        #    self.level = 50

        # hp test
        #if key[pygame.K_UP]:
        #    self.HP += 10
        #    self.hb.get_health(10)
        #    if self.HP >= self.Max_HP:
        #        self.HP = self.Max_HP
        #if key[pygame.K_DOWN]:
        #    self.HP -= 10
        #    self.hb.get_damage(10)


        # Check bullet out of vision to del from self.bullets
        for i, bullet in enumerate(self.bullets):
            bullet.run()
            if bullet.y <= -64:
                del self.bullets[i]
                break

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

            # Enemy bullet collision
        for ebullet in ebull:
            if ebullet.hitbox.colliderect(self.hitbox):
                if ebullet.hitable:
                    if self.invis_cooldown == 0:
                        ebullet.hitable = 0
                        self.HP -= 10
                        self.hb.get_damage(10)
                        self.stop_sound()
                        phit.play()
                        self.invis_cooldown = 1

        # Enemy crash collision
        if len(erect) >= 1:

            for i in range(enum):

                if self.rect.colliderect(erect[i]):
                    if self.invis_cooldown == 0:
                        self.HP -= 10
                        self.hb.get_damage(10)
                        self.stop_sound()
                        phit.play()
                        self.invis_cooldown = 1



        for item in items:
            if item.hitbox.colliderect(self.hitbox):
                if item.hitable:
                    item.hitable = 0
                    # Check type of items
                    ''' 1 = Lasergun 2 = Heavybullet 3 = Plasmaball 4 = HP potion 5 = Rapidfire '''
                    if item.type == 1:
                        self.type = 0
                        self.stop_sound()
                        laser_item.play()
                    elif item.type == 2:
                        self.type = 1
                        self.stop_sound()
                        heavy_item.play()
                    elif item.type == 3:
                        self.type = 2
                        self.stop_sound()
                        plasma_item.play()
                    elif item.type == 4:
                        self.HP += 20 + (self.level // 3)
                        self.stop_sound()
                        heal.play()
                        if self.HP >= self.Max_HP:
                            self.HP = self.Max_HP
                        self.hb.get_health(20 + (self.level // 3))
                    elif item.type == 5:
                        self.stop_sound()
                        rapid_item.play()
                        self.rapid_timer = 0
                        self.rapid = 0.3
                    elif item.type == 6:
                        self.stop_sound()
                        xpboostsound.play()
                        multiplier =  1 + (self.level // 10)
                        self.xp_boost = 2 * multiplier
                        self.xp_boost_timer = 0

        if self.invis_cooldown == 1:
            self.invis_timer += dt
            if self.invis_timer >= self.invisible_time :
                self.invis_timer = 0
                self.invis_cooldown = 0

        if self.rapid != 1:
            rapidimg = pygame.transform.scale(Rapid, (48, 48))
            screen.blit(rapidimg,(10,60))
            self.rapid_timer += dt
            if self.rapid_timer >= self.rapid_duration:
                self.rapid = 1
                self.rapid_timer = 0

        if self.xp_boost != 1:
            xpboostimg = pygame.transform.scale(xpboost, (48, 48))
            screen.blit(xpboostimg, (60, 60))
            self.xp_boost_timer += dt
            if self.xp_boost_timer >= self.xp_boost_duration:
                self.xp_boost = 1
                self.xp_boost_timer = 0

        if self.HP <= 0 :
            game_over_sound.play()
            self.gameover = 1
        if key[pygame.K_ESCAPE]:
            game_over_sound.play()
            self.gameover = 1


    def draw_gui(self):
        self.hb.update(self.Max_HP,self.HP)
        self.xp.update(self.Max_XP , self.cur_xp,self.xp_boost)
        self.show_level()
    def draw_player(self):
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        screen.blit(self.playerImg, (self.x , self.y))
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def run(self, erect, enum , ebull,eKP, items):
        self.update(erect, enum , ebull,eKP, items)
        self.draw_player()
        self.draw_gui()
