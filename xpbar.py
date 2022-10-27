from settings import *

class XPbar (pygame.sprite.Sprite):

    def __init__(self, maxxp , curxp):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill((240, 240, 240))
        self.rect = self.image.get_rect(center=(400, 400))
        self.max_xp = maxxp
        self.cur_xp = curxp
        self.target_xp = curxp

        self.xp_bar_length = 400
        self.xp_ratio = self.max_xp / self.xp_bar_length
        self.xp_change_speed = 1

    def update(self,maxxp , curxp):
        self.basic_xp(maxxp , curxp)
        #self.advanced_xp(maxxp , curxp)


    def get_damage(self,amount):
        if self.target_xp > 0:
            self.target_xp -= amount
        if self.target_xp <= 0:
            self.target_xp = 0

    def get_xp(self, amount):
        if self.target_xp < self.max_xp:
            self.target_xp += amount
        if self.target_xp >= self.max_xp:
            self.target_xp = self.max_xp

    def basic_xp(self,maxxp , curxp):
        self.max_xp = maxxp
        self.cur_xp = curxp
        self.xp_ratio = self.max_xp / self.xp_bar_length

        pygame.draw.rect(screen, yellow, (10, 40, self.target_xp/self.xp_ratio , 10))
        pygame.draw.rect(screen, white, (10, 40, self.xp_bar_length, 10),2)

    def advanced_xp(self,maxxp , curxp):
        self.max_xp = maxxp
        self.cur_xp = curxp
        self.xp_ratio = self.max_xp / self.xp_bar_length
        transition_width = 0
        transition_color = cyan

        if self.cur_xp < self.target_xp:
            self.cur_xp += self.xp_change_speed
            transition_width = int((self.target_xp - self.cur_xp)/self.xp_ratio)
            transition_color = cyan
        if self.cur_xp > self.target_xp:
            self.cur_xp -= self.xp_change_speed
            transition_width = int((self.cur_xp - self.target_xp)/self.xp_ratio)
            transition_color = red

        xp_bar_rect = pygame.Rect(10,40,self.cur_xp / self.xp_ratio, 10)
        transition_bar_rect = pygame.Rect(xp_bar_rect.right, 10, transition_width , 25)

        pygame.draw.rect(screen, transition_color, transition_bar_rect)
        pygame.draw.rect(screen, yellow, xp_bar_rect)
        pygame.draw.rect(screen, (255,255,255), (10,40,self.xp_bar_length,10), 2)
