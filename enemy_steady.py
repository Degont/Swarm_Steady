import pygame
from pygame.sprite import Sprite
import math
from random import randint

class Enemy(Sprite):
    def __init__(self, game,spawn_location,trajectory):
        super().__init__()
        self.game = game
        self.screen = self.game.screen
        self.settings = self.game.settings

        # Rect building
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = spawn_location

        # storing bullet position as a float
        self.trajectory = trajectory
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        # Movement Flag
        self.move_style = 2

    def _trajectory(self,target):


        end_point = target


        # magnitudes
        vert_mag = end_point[1] - self.rect.center[1]  # Negative if enemy is below the ship
        hori_mag = end_point[0] - self.rect.center[0]  # Negative if enemy is to the right

        # slope Calc
        if hori_mag == 0:
            slope_x = 0
            if vert_mag == 0:
                slope_y = 0
            else:
                if vert_mag > 0:
                    slope_y = -1
                else:
                    slope_y = 1
        else:
            slope_y = vert_mag/abs(hori_mag)

            if hori_mag > 0:
                slope_x = 1
            else:
                slope_x = -1



        return slope_y, slope_x

    def _trajectory_2(self,target):

        end_point = target

        # magnitudes
        y_mag = end_point[1] - self.rect.center[1]
        x_mag = end_point[0] - self.rect.center[0]
        total_mag = abs(x_mag)+abs(y_mag)
        hyp_mag = math.sqrt((y_mag**2) + (x_mag**2))

        # slope stuff
        if x_mag == 0:
            x_ratio = 0
            if y_mag == 0:
                y_ratio = 0
            else:
                if y_mag > 0:
                    print("pussy")
                    y_ratio = -1
                else:
                    y_ratio = 1
        else:
            if y_mag == 0:
                y_ratio = 0
                if x_mag > 0:
                    x_ratio = 1
                else:
                    x_ratio = -1
            else:                 # where all the real shit goes now after passing zeros
                if self.move_style == 1:
                    x_ratio = x_mag/total_mag
                    y_ratio = y_mag/total_mag
                else:
                    x_ratio = (x_mag**2 / hyp_mag**2)*(x_mag/abs(x_mag))
                    y_ratio = (y_mag**2 / hyp_mag**2)*(y_mag/abs(y_mag))


        return x_ratio, y_ratio


    def update(self,target_location):
        """This is what determines the path of the bullet"""
        if self.move_style == 0:
            trajectory = self._trajectory(target_location)

            # movement stuff
            self.y += trajectory[0] * self.settings.enemy_speed
            self.x += trajectory[1] * self.settings.enemy_speed

        else:
            trajectory = self._trajectory_2(target_location)

            # movement stuff
            self.y += trajectory[1] * self.settings.enemy_speed
            self.x += trajectory[0] * self.settings.enemy_speed

        self.rect.y = self.y
        self.rect.x = self.x

    def draw_enemy(self):
        self.screen.blit(self.image,self.rect.center)
