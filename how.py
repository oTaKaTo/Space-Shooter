from button import *

class How:
    def __init__(self):
        self.run = 1
        self.play = 0
        self.back = 0

    def draw(self):
        play = Button((625, 820, 120, 60), white, "PLAY", 24, screen,
                       border_color=white, border_width=4)
        back = Button((625, 890, 120, 60), white, "BACK", 24, screen,
                      border_color=white, border_width=4)
        screen.blit(how_to_play, (0, 0))
        play.run()
        back.run()
        if play.clicked:
            click_sound.play()
            self.play = 1
            play.clicked = 0
        if back.clicked:
            click_sound.play()
            self.back = 1
            back.clicked = 0

