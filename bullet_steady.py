import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,game,ship_direction):
        super().__init__()
        self.game = game
        self.screen = self.game.screen
        self.settings = self.game.settings
        self.color = self.game.settings.bullet_color
        self.trajectory = ship_direction

        # Make bullet Rect
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midbottom = self.game.ship.rotated_image_rect.center

        # storing bullet position as a float
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """This is what determines the path of the bullet"""

        # movement stuff
        self.y += self.trajectory[0] * self.settings.bullet_speed
        self.rect.y = self.y
        self.x += self.trajectory[1] * self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.circle(self.screen,self.color,self.rect.center,5)