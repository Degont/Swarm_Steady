from time import sleep
import sys
import pygame

from settings_steady import Settings
from button_steady import Button
from ship_steady import Ship

class Game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Test Game")
        self.bg_color = self.settings.bg_color

        self.ship = Ship(self)

    def loop(self):
        while True:
            self.events()
            self.ship.update_pos()
            self.update()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._keydown(event)
            if event.type == pygame.KEYUP:
                self._keyup(event)

    def _keydown(self,event):
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _keyup(self,event):
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False


    def update(self):
        self.screen.fill(self.bg_color)

        # Button
        self.button = Button(self,f"{round(self.ship.angle,2)}")
        self.button.draw_button()

        # Ship
        self.ship.draw_ship()

        # Flip
        pygame.display.flip()
        #print(self.ship.image_rect.center)

if __name__ == "__main__":
    play = Game()
    play.loop()