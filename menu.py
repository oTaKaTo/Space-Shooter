from settings import *

class Menu:
    def __init__(self):
        self.run = 1

    def draw(self, font):

        start = font.render("START", True,(255,255,255))
        label = font.render("Press the mouse to begin...", 1, (255, 255, 255))
        screen.blit(label, (WIDTH / 2 - label.get_width() / 2, 250))
        back_key = font.render("backspace --> main menu", 1, (255, 255, 255))
        screen.blit(back_key, (WIDTH - back_key.get_width() - 10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.run = False
            if keys[pygame.K_BACKSPACE]:
                self.run = False







        screen.blit(start,(WIDTH/3, HEIGHT*2 /3))


