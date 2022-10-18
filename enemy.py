from settings import *
from bullet import *

class Enemy:

    def __init__(self):
        self.hp = []
        self.start = 0
        #enemy health
        self.smallhp = 10
        self.medhp = 50
        self.bighp = 100
        #Hitbox size
        self.hitbox = []
        self.b = Bullet()
        self.rect = []


        self.speed = []
        self.small_speed = random.randint(200,250) * dt
        self.medium_speed = random.randint(100,150) * dt
        self.big_speed = random.randint(50,100) * dt


        self.x = []
        self.y = []
        self.type = []
        self.numbers = 5
        self.old_num = 5

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
        self.addtime = 10
    def magnetic_movement(self, px , py , i):
        if self.x[i] < px:
            self.x[i] += 1
        if self.x[i] > px:
            self.x[i] -= 1


    def big_enemy(self):
        self.hp.append(self.bighp)
        self.speed.append(random.randint(50,250) * dt)
        self.x.append(random.randint(10, 750))
        self.y.append(random.randint(-1000, -100))
        self.hitbox.append((self.x, self.y, 70, 80))
        self.big_Img = self.big[self.value]
        self.big_Img = pygame.transform.scale(self.big_Img, (80, 80))
        self.rect.append(self.big_Img.get_rect())

    def medium_enemy(self):
        self.hp.append(self.medhp)
        self.speed.append(random.randint(100,400) * dt)
        self.x.append(random.randint(10, 750))
        self.y.append(random.randint(-1000, -100))
        self.hitbox.append((self.x, self.y, 64, 64))
        self.med_Img = self.medium[self.value]
        self.med_Img = pygame.transform.scale(self.med_Img, (64, 64))
        self.rect.append(self.med_Img.get_rect())

    def small_enemy(self):
        self.hp.append(self.smallhp)
        self.speed.append(random.randint(200,800) * dt)
        self.x.append(random.randint(10, 750))
        self.y.append(random.randint(-1000, -100))
        self.hitbox.append((self.x, self.y, 48, 48))
        self.small_Img = self.small[self.value]
        self.small_Img = pygame.transform.scale(self.small_Img, (48, 48))
        self.rect.append(self.small_Img.get_rect())

    def init(self):
        for i in range(self.numbers):
            rand = random.randint(0, 20)
            # random enemy type
            if rand >= 0 and rand <= 15:
                self.type.append(0)
                self.small_enemy()
                print(self.speed[i])


            elif rand >= 16 and rand <= 18:
                self.type.append(1)
                self.medium_enemy()
            elif rand >= 19:
                self.type.append(2)
                self.big_enemy()

    def update(self,prect, brect , px ,py):
        self.counttime += dt
        self.totaltime += dt

        for i in range(self.numbers):
            if self.numbers > self.old_num:
                self.old_num = self.numbers
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

            self.y[i] += self.speed[i]
            # movement type
            if self.type[i] == 0:
                self.magnetic_movement(px,py,i)
            elif self.type[i] == 1:
                pass
            elif self.type[i] == 2:
                pass
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

            # if out of vision
            if self.y[i] >= 1000:
                self.y[i] = random.randint(-1000, -100)
                self.x[i] = random.randint(10, 750)
                # random type again
                rand = random.randint(0, 20)
                # random enemy type
                if rand >= 0 and rand <= 15:
                    self.type[i] = 0
                    self.hp[i] = self.smallhp
                    self.speed[i] = random.randint(200,800) * dt
                elif rand >= 16 and rand <= 18:
                    self.type[i] = 1
                    self.hp[i] = self.medhp
                    self.speed[i] = random.randint(100,400) * dt
                elif rand >= 19:
                    self.type[i] = 2
                    self.hp[i] = self.bighp
                    self.speed[i] = random.randint(50,250) * dt

            # change animation
            if self.counttime >= self.change_time:
                self.value += 1
                if self.value >= 2:
                    self.value = 0
                self.counttime = 0

            # Collision
            if self.rect[i].colliderect(prect):
                print("Player collision happened !")
            if self.rect[i].colliderect(brect):
                print("Bullet collision happened !")

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
                pygame.draw.rect(screen, (255, 0, 0), self.hitbox[i], 2)
            elif self.type[i] == 1:
                self.hitbox[i] = (self.x[i], self.y[i], 64, 64)
                pygame.draw.rect(screen, (255, 0, 0), self.hitbox[i], 2)
            else:
                self.hitbox[i] = (self.x[i], self.y[i], 80, 80)
                pygame.draw.rect(screen, (255, 0, 0), self.hitbox[i], 2)


    def run(self,prect, brect,px , py):
        if self.start == 0:
            self.init()
            self.start = 1
        self.update(prect, brect , px , py)
        self.draw()

