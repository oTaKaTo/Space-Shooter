import pygame

from settings import *

class Player:
    def __init__(self):
        self.HP = 100
        self.XP = 0
        self.level = 1
        self.x = 370
        self.y = 850
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        self.speed = 500 * dt
        self.playerImg = pygame.image.load("pic/player/ship/base/png/full_hp.png")
        self.playerImg = pygame.transform.scale(self.playerImg, (64, 64))
        self.rect = self.playerImg.get_rect()

    def update(self, erect , enum):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.x -= self.speed
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.x += self.speed
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.y -= self.speed
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.y += self.speed

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
            for i in range(enum):
                if self.rect.colliderect(erect[i]):
                    print("D A M A G E")

    def draw(self):
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        screen.blit(self.playerImg, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def run(self, erect, enum):
        self.update(erect, enum)
        self.draw()
