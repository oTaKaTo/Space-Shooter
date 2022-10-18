from settings import *

class Menu:
    def __init__(self):
        self.run = 1

    def draw(self, font, label_font):

        start = font.render("START", True,(255,255,255))
        label = label_font.render("SPACE SHOOTER", 1, (255, 255, 255))
        screen.blit(label, (WIDTH / 2 - label.get_width() / 2, 250))
        name = font.render("65010373 Takdanai Deephuak", 1, (255, 255, 255))
        screen.blit(name, (10, HEIGHT-30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.run = False
            if keys[pygame.K_BACKSPACE]:
                self.run = False







        screen.blit(start,(WIDTH/2 - start.get_width(), HEIGHT* 2 /3))


