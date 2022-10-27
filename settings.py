import pygame
import random
import pygame.key
import math
pygame.init()
# sound
pshoot = pygame.mixer.Sound("sound/pshot.wav")
phit = pygame.mixer.Sound("sound/pcrack.wav")
bgm = pygame.mixer.music.load("sound/bgm.mp3")
ecrash = pygame.mixer.Sound("sound/ecrash.wav")
level_up = pygame.mixer.Sound("sound/levelup.wav")
home = pygame.mixer.music.load("sound/home.wav")
# font
font = pygame.font.Font('font/8Bit.ttf', 20)
main_font = pygame.font.Font('font/8-BITWONDER.ttf', 54)


#RGB color
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
cyan = (0,255,255)
blue = (0,0,255)
lime = (0,255,0)
black = (0,0,0)





# setting windows
screen = pygame.display.set_mode((800, 1000))
WIDTH = 800
HEIGHT = 1000
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("pic/icon.png")
pygame.display.set_icon(icon)

# Background
bg = pygame.image.load("pic/bg.jpg")
bg_height = bg.get_height()
bg = pygame.transform.scale(bg, (WIDTH, bg_height))
bg_rect = bg.get_rect()

scroll = 0
panels = math.ceil(HEIGHT / bg_height) + 2


# Clock

clock = pygame.time.Clock()
dt = clock.tick(144)/1000
# bullets
laser = [ pygame.image.load("pic/bullet/laser/1.png"),
          pygame.image.load("pic/bullet/laser/2.png"),
          pygame.image.load("pic/bullet/laser/3.png"),
          pygame.image.load("pic/bullet/laser/4.png"),
          pygame.image.load("pic/bullet/laser/5.png"),
          pygame.image.load("pic/bullet/laser/6.png"),
          pygame.image.load("pic/bullet/laser/7.png"),
          pygame.image.load("pic/bullet/laser/8.png")]

cannon = [ pygame.image.load("pic/bullet/canon/1.png"),
           pygame.image.load("pic/bullet/canon/2.png"),
           pygame.image.load("pic/bullet/canon/3.png"),
           pygame.image.load("pic/bullet/canon/4.png")]

ball = [ pygame.image.load("pic/bullet/ball/1.png"),
         pygame.image.load("pic/bullet/ball/2.png"),
         pygame.image.load("pic/bullet/ball/3.png"),
         pygame.image.load("pic/bullet/ball/4.png"),
         pygame.image.load("pic/bullet/ball/5.png"),
         pygame.image.load("pic/bullet/ball/6.png"),
         pygame.image.load("pic/bullet/ball/7.png"),
         pygame.image.load("pic/bullet/ball/8.png"),
         pygame.image.load("pic/bullet/ball/9.png"),
         pygame.image.load("pic/bullet/ball/10.png")]

crash = [ pygame.image.load("pic/explosion/1.png"),
            pygame.image.load("pic/explosion/2.png"),
            pygame.image.load("pic/explosion/3.png"),
            pygame.image.load("pic/explosion/4.png"),
            pygame.image.load("pic/explosion/5.png")]

enemy_bullet = pygame.image.load("pic/enemy/bullet/bullet.png")
