import random

from settings import *
from bullet import *
from EBullet import New_bullet
from score import *
class Enemy:

    def __init__(self):
        self.score = Score()
        self.hp = []
        self.start = 0
        #enemy health
        self.smallhp = 10
        self.medhp = 200
        self.bighp = 1000
        #Hitbox size
        self.hitbox = []
        self.rect = []
        self.direction = []
        self.speed = []
        self.small_speed = random.randint(200,400) * dt
        self.medium_speed = random.randint(100,150) * dt
        self.big_speed = random.randint(50,100) * dt

        self.KP = 0


        self.x = []
        self.y = []
        self.type = []
        self.bullets = []
        self.numbers = 10
        self.old_num = 5

        # enemy bullets
        self.bullets = []
        self.shoot_timer = []

        # enemy image
        self.small = [pygame.image.load("pic/enemy/small/1.png"),
                      pygame.image.load("pic/enemy/small/2.png")]
        self.medium = [pygame.image.load("pic/enemy/medium/1.png"),
                       pygame.image.load("pic/enemy/medium/2.png")]
        self.big = [pygame.image.load("pic/enemy/big/1.png"),
                    pygame.image.load("pic/enemy/big/2.png")]
        self.value = 0
        self.small_Img = self.small[self.value]
        self.med_Img = self.medium[self.value]
        self.big_Img = self.big[self.value]



        self.counttime = 0
        self.change_time = 50 / 1000
        self.rand = []
        # add enemy time up to game runtime
        self.totaltime = 0
        self.addtime = 5

    def crash(self,x,y):
        for i in range(len(crash)):
            crashImg = crash[i]
            crashImg = pygame.transform.scale(crashImg, (48, 48))
            screen.blit(crashImg, (x+10 , y+10))




    def magnetic_movement(self, px , py , i):
        if self.x[i] < px:
            self.x[i] += 1
        if self.x[i] > px:
            self.x[i] -= 1

    def bounce_movement(self,i, rect):
        if self.x[i] < WIDTH - rect[2] and self.direction[i] == 1:
            self.x[i] += 3 * self.direction[i]
            if self.x[i] > WIDTH - rect[2]:
                self.direction[i] = -1

        if self.x[i] > 0 and self.direction[i] == -1:
            self.x[i] += 3 * self.direction[i]
            if self.x[i] <= 1:
                self.direction[i] = 1
    def wallhack_movement(self,i, rect):
        if self.direction[i] == 1:
            self.x[i] += 3 * self.direction[i]
            if self.x[i] > WIDTH + rect[2]:
                self.x[i] = 0 - rect[2]

        if self.direction[i] == -1:
            self.x[i] += 3 * self.direction[i]
            if self.x[i] <= 0 - rect[2]:
                self.x[i] = WIDTH + rect[2]
    def create_bullets(self, x, y,etype):
        self.bullets.append(New_bullet(x,y ,etype))

    def big_enemy(self):
        self.hp.append(self.bighp)
        self.speed.append(random.randint(50,250) * dt)
        self.x.append(random.randint(10, 750))
        self.y.append(random.randint(-1000, -100))
        self.hitbox.append((self.x, self.y, 70, 80))
        self.big_Img = self.big[self.value]
        self.big_Img = pygame.transform.scale(self.big_Img, (80, 80))
        self.rect.append(self.big_Img.get_rect())
        self.shoot_timer.append(pygame.time.get_ticks())
        self.direction.append(random.choice([-1, 1]))
    def big_enemy_add(self,i):
        self.hp.insert(i,self.bighp)
        self.speed.insert(i, (random.randint(50,250) * dt))
        self.x.insert(i, (random.randint(10, 750)))
        self.y.insert(i, (random.randint(-1000, -100)))
        self.hitbox.insert(i,((self.x, self.y, 70, 80)))
        self.big_Img = self.big[self.value]
        self.big_Img = pygame.transform.scale(self.big_Img, (80, 80))
        self.rect.insert(i, (self.big_Img.get_rect()))
        self.shoot_timer.insert(i, (pygame.time.get_ticks()))
        self.direction.insert(i, (random.choice([-1, 1])))
    def medium_enemy(self):
        self.hp.append(self.medhp)
        self.speed.append(random.randint(100,400) * dt)
        self.x.append(random.randint(10, 700))
        self.y.append(random.randint(-1000, -100))
        self.hitbox.append((self.x, self.y, 64, 64))
        self.med_Img = self.medium[self.value]
        self.med_Img = pygame.transform.scale(self.med_Img, (64, 64))
        self.rect.append(self.med_Img.get_rect())
        self.shoot_timer.append(pygame.time.get_ticks())
        self.direction.append(random.choice([-1, 1]))
    def medium_enemy_add(self,i):
        self.hp.insert(i,self.medhp)
        self.speed.insert(i,random.randint(100,400) * dt)
        self.x.insert(i, (random.randint(10, 700)))
        self.y.insert(i, (random.randint(-1000, -100)))
        self.hitbox.insert(i,((self.x, self.y, 64, 64)))
        self.med_Img = self.medium[self.value]
        self.med_Img = pygame.transform.scale(self.med_Img, (64, 64))
        self.rect.insert(i,(self.med_Img.get_rect()))
        self.shoot_timer.insert(i, (pygame.time.get_ticks()))
        self.direction.insert(i,(random.choice([-1, 1])))
    def small_enemy(self):
        self.hp.append(self.smallhp)
        self.speed.append(random.randint(200,800) * dt)
        self.x.append(random.randint(10, 750))
        self.y.append(random.randint(-1000, -100))
        self.hitbox.append((self.x, self.y, 48, 48))
        self.small_Img = self.small[self.value]
        self.small_Img = pygame.transform.scale(self.small_Img, (48, 48))
        self.rect.append(self.small_Img.get_rect())
        self.shoot_timer.append(pygame.time.get_ticks())
        self.direction.append(0)
    def small_enemy_add(self,i):
        self.hp.insert(i,(self.smallhp))
        self.speed.insert(i, (random.randint(200,800) * dt))
        self.x.insert(i,(random.randint(10, 750)))
        self.y.insert(i,(random.randint(-1000, -100)))
        self.hitbox.insert(i,((self.x, self.y, 48, 48)))
        self.small_Img = self.small[self.value]
        self.small_Img = pygame.transform.scale(self.small_Img, (48, 48))
        self.rect.insert(i,(self.small_Img.get_rect()))
        self.shoot_timer.insert(i,(pygame.time.get_ticks()))
        self.direction.insert(i, 0)
    def remove_enemy(self,i):
        del self.type[i]
        del self.hp[i]
        del self.speed[i]
        del self.x[i]
        del self.y[i]
        del self.hitbox[i]
        del self.rect[i]
        del self.shoot_timer[i]
        del self.direction[i]

    def init(self):
        for i in range(self.numbers):
            rand = random.randint(0, 20)
            # random enemy type
            if rand >= 0 and rand <= 15:
                self.type.append(0)
                self.small_enemy()

            elif rand >= 16 and rand <= 18:
                self.type.append(1)
                self.medium_enemy()
            elif rand >= 19:
                self.type.append(2)
                self.big_enemy()

    def update(self,prect, pbullets , px ,py):
        self.counttime += dt
        self.totaltime += dt


        for i, bullet in enumerate(self.bullets):
            bullet.run(prect)
            if bullet.y >= 1032:
                del self.bullets[i]
                break

        for i in range(self.numbers):

            self.y[i] += self.speed[i]

            # if out of vision
            if self.y[i] >= 1000:
                self.remove_enemy(i)
                # random type again
                rand = random.randint(0, 20)
                # random enemy type
                if rand >= 0 and rand <= 15:
                    self.type.insert(i, 0)
                    self.small_enemy_add(i)
                elif rand >= 16 and rand <= 18:
                    self.type.insert(i, 1)
                    self.medium_enemy_add(i)
                elif rand >= 19:
                    self.type.insert(i, 2)
                    self.big_enemy_add(i)


            # movement type
            if self.type[i] == 0:
                self.magnetic_movement(px,py,i)
            elif self.type[i] == 1:
                self.bounce_movement(i,self.rect[i])
            elif self.type[i] == 2:
                self.wallhack_movement(i,self.rect[i])
            # rect
            if self.type[i] == 0:
                self.rect[i] = self.small_Img.get_rect()
                self.rect[i].x = self.x[i]
                self.rect[i].y = self.y[i]
                self.small_Img = self.small[self.value]
                self.small_Img = pygame.transform.scale(self.small_Img, (48, 48))

            elif self.type[i] == 1:
                self.rect[i] = self.med_Img.get_rect()
                self.rect[i].x = self.x[i]
                self.rect[i].y = self.y[i]
                self.med_Img = self.medium[self.value]
                self.med_Img = pygame.transform.scale(self.med_Img, (64, 64))
            else:
                self.rect[i] = self.big_Img.get_rect()
                self.rect[i].x = self.x[i]
                self.rect[i].y = self.y[i]
                self.big_Img = self.big[self.value]
                self.big_Img = pygame.transform.scale(self.big_Img, (80, 80))



            # change animation
            if self.counttime >= self.change_time:
                self.value += 1
                if self.value >= 2:
                    self.value = 0
                self.counttime = 0
            if pygame.time.get_ticks() - self.shoot_timer[i] > 5000:
                self.shoot_timer[i] = pygame.time.get_ticks()
                self.create_bullets(self.x[i], self.y[i] ,self.type[i])

            #for ebullet in self.bullets:
            #    if ebullet.hitbox.colliderect(prect):
            #       print("Bullet collision happened !")

            # Collision
            # if self.rect[i].colliderect(prect):
            #     print("Player collision happened !")
            for pbullet in pbullets:
                if self.rect[i].colliderect(pbullet.hitbox):
                     if pbullet.hitable == 1:
                        self.hp[i] -= pbullet.damage
                     if pbullet.type != 2:
                        pbullet.hitable = 0

            if self.hp[i] <= 0 :
                # Adding Scores
                if self.type[i] == 0:
                    self.KP += 1
                    self.score.score_value += 100
                elif self.type[i] == 1:
                    self.KP += 3
                    self.score.score_value += 300
                else:
                    self.KP += 10
                    self.score.score_value += 1000
                self.crash(self.x[i],self.y[i])
                ecrash.play()
                self.remove_enemy(i)
                rand = random.randint(0, 20)
                # random enemy type
                if rand >= 0 and rand <= 15:
                    self.type.insert(i, 0)
                    self.small_enemy_add(i)
                elif rand >= 16 and rand <= 18:
                    self.type.insert(i, 1)
                    self.medium_enemy_add(i)
                elif rand >= 19:
                    self.type.insert(i, 2)
                    self.big_enemy_add(i)


        # adding more enemies
        if self.totaltime >= self.addtime:
            self.totaltime = 0
            #self.addtime += 5
            self.numbers += 1
            rand = random.randint(0, 20)
            # random enemy type
            if rand >= 0 and rand <= 15:
                self.type.append(0)
                self.small_enemy()
            elif rand >= 16 and rand <= 18:
                self.type.append(1)
                self.medium_enemy()
            elif rand >= 19:
                self.type.append(2)
                self.big_enemy()



    def draw(self):
        for i in range(self.numbers):
            if self.type[i] == 0:
                screen.blit(self.small_Img, (self.x[i], self.y[i]))
            elif self.type[i] == 1:
                screen.blit(self.med_Img, (self.x[i], self.y[i]))
            elif self.type[i] == 2:
                screen.blit(self.big_Img, (self.x[i], self.y[i]))

            # draw hitbox
            if self.type[i] == 0:
                self.hitbox[i] = (self.x[i], self.y[i], 48, 48)
                #pygame.draw.rect(screen, (255, 0, 0), self.hitbox[i], 2)
            elif self.type[i] == 1:
                self.hitbox[i] = (self.x[i], self.y[i], 64, 64)
                #pygame.draw.rect(screen, (255, 0, 0), self.hitbox[i], 2)
            else:
                self.hitbox[i] = (self.x[i], self.y[i], 80, 80)
                #pygame.draw.rect(screen, (255, 0, 0), self.hitbox[i], 2)


    def run(self,prect, pbullets,px , py):
        # initialize enemy
        if self.start == 0:
            self.init()
            self.start = 1
        # update enemy
        self.update(prect, pbullets , px , py)
        self.draw()
        self.score.show_score()



