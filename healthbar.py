from settings import *

class Healthbar (pygame.sprite.Sprite):

    def __init__(self, maxhp , curhp):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill((240, 240, 240))
        self.rect = self.image.get_rect(center=(400, 400))
        self.max_HP = maxhp
        self.cur_HP = curhp
        self.target_HP = curhp

        self.health_bar_length = 400
        self.health_ratio = self.max_HP / self.health_bar_length
        self.health_change_speed = 1

    def update(self,Max_HP,curHP):
        self.basic_health(Max_HP,curHP)
        #self.advanced_health(Max_HP,curHP)

    def get_damage(self,amount):
        if self.target_HP > 0:
            self.target_HP -= amount
        if self.target_HP <= 0:
            self.target_HP = 0

    def get_health(self, amount):
        if self.target_HP < self.max_HP:
            self.target_HP += amount
        if self.target_HP >= self.max_HP:
            self.target_HP = self.max_HP

    def basic_health(self,Max_HP,curHP):
        self.max_HP = Max_HP
        self.cur_HP = curHP
        self.health_ratio = self.max_HP / self.health_bar_length
        pygame.draw.rect(screen, (255,0,0), (10, 10, self.target_HP/self.health_ratio , 25))
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, self.health_bar_length, 25),4)

    def advanced_health(self,Max_HP,curHP):
        self.max_HP = Max_HP
        self.cur_HP = curHP
        transition_width = 0
        transition_color = (255,0,0)

        if self.cur_HP < self.target_HP:
            self.cur_HP += self.health_change_speed
            transition_width = int((self.target_HP - self.cur_HP)/self.health_ratio)
            transition_color = lime
        if self.cur_HP > self.target_HP:
            self.cur_HP -= self.health_change_speed
            transition_width = int((self.cur_HP - self.target_HP)/self.health_ratio)
            transition_color = yellow

        health_bar_rect = pygame.Rect(10,10,self.cur_HP / self.health_ratio, 25)
        transition_bar_rect = pygame.Rect(health_bar_rect.right, 10, transition_width , 25)

        pygame.draw.rect(screen, transition_color, transition_bar_rect)
        pygame.draw.rect(screen, (255,0,0), health_bar_rect)
        pygame.draw.rect(screen, (255,255,255), (10,10,self.health_bar_length,25), 4)
