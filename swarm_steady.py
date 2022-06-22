from time import sleep
import sys
import pygame

from ship_steady import Ship

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Test Game")
        self.bg_color = (230,230,0)

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
                print(event)
            if event.type == pygame.KEYUP:
                self._keyup(event)

    def _keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def update(self):
        self.screen.fill(self.bg_color)
        self.ship.draw_ship()
        pygame.display.flip()

if __name__ == "__main__":
    play = Game()
    play.loop()