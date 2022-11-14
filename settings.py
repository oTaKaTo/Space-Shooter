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
pop = pygame.mixer.Sound("sound/pop.mp3")
level_up = pygame.mixer.Sound("sound/levelup.wav")
home = pygame.mixer.music.load("sound/home.wav")
game_over_sound = pygame.mixer.Sound("sound/game_over_edited.wav")

change_movement = pygame.mixer.Sound("sound/change_movement.wav")
click_sound = pygame.mixer.Sound("sound/click_sound.wav")

heavy_item = pygame.mixer.Sound("sound/heavy_item.wav")
heavy_shoot = pygame.mixer.Sound("sound/heavy_shoot.wav")

laser_item = pygame.mixer.Sound("sound/laser_item_metal_slug.wav")

plasma_item = pygame.mixer.Sound("sound/plasma_item_edited.wav")
plasma_shoot = pygame.mixer.Sound("sound/plasma_pew.wav")

rapid_item = pygame.mixer.Sound("sound/power_item.mp3")
heal = pygame.mixer.Sound("sound/heal.wav")
xpboostsound = pygame.mixer.Sound("sound/xpboost.mp3")

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

how_to_play = pygame.image.load("pic/how to play new.png")
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

# Items
Rapid = pygame.image.load("pic/item/Buffs/attack_speed_boost.png")
Hpotion = pygame.image.load("pic/item/Red Potions/1.png")
lasergun = pygame.image.load("pic/item/WeaponPack/lasergun.png")
plasmaball = pygame.image.load("pic/item/WeaponPack/plasmaball.png")
heavybull = pygame.image.load("pic/item/WeaponPack/heavybull.png")
xpboost = pygame.image.load("pic/item/Buffs/exp_boost.png")


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
