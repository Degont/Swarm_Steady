from time import sleep
import sys
import pygame
from random import randint

from settings_steady import Settings
from button_steady import Button
from ship_steady import Ship
from bullet_steady import Bullet
from enemy_steady import Enemy

class Game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Test Game")
        self.bg_color = self.settings.bg_color

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.enemy_spawn = 1

    def loop(self):
        while True:
            self.events()
            self.ship.update_pos()
            self._update_weapons()
            self._update_enemies()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.enemy_spawn *= -1
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

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self,self.ship.ship_direction_2())  # creates new bullet from our bullet class
            self.bullets.add(new_bullet)  # adds to our sprite group so we can manipulate all at once

    def _create_enemy(self):
        """Create a new enemy and add it to the enemies group"""
        if len(self.enemies) < self.settings.enemy_limit:
            spawn_location = self._spawn_location()
            new_enemy = Enemy(self,spawn_location,self.ship.ship_direction_2(spawn_location))  # creates new bullet from our bullet class
            self.enemies.add(new_enemy)  # adds to our sprite group so we can manipulate all at once

    def _spawn_location(self):

        rand_x = randint(0,self.settings.screen_height)
        rand_y = randint(0,self.settings.screen_width)

        return rand_x, rand_y

    def _update_weapons(self):
        """Update the position of projectiles and get rid of old bullets """
        self.bullets.update()  # calling update on a group auto calls update on each instance in the group
        self._check_collisions()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():  # we use copy here so we can loop through the list and remove from it,
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            elif bullet.rect.top >= 800:
                self.bullets.remove(bullet)
            elif bullet.rect.left <= 0:
                self.bullets.remove(bullet)
            elif bullet.rect.right >= 1200:
                self.bullets.remove(bullet)

    def _update_enemies(self):
        """Updates the position of the enemies"""
        if self.enemy_spawn == -1:
            if len(self.enemies) < self.settings.enemy_limit:
                self._create_enemy()

        self.enemies.update(self.ship.rect.center)

        self._check_collisions()

        for enemy in self.enemies.copy():  # we use copy here so we can loop through the list and remove from it,
            if enemy.rect.bottom <= 0:
                self.enemies.remove(enemy)
            elif enemy.rect.top >= 800:
                self.enemies.remove(enemy)
            elif enemy.rect.left <= 0:
                self.enemies.remove(enemy)
            elif enemy.rect.right >= 1200:
                self.enemies.remove(enemy)


    def _check_collisions(self):
        pygame.sprite.groupcollide(self.bullets,self.enemies,True,True,None)

        ship_hit = pygame.sprite.spritecollideany(self.ship, self.enemies)
        if ship_hit:
            self.enemies.remove(ship_hit)

        pass


    def update(self):
        self.screen.fill(self.bg_color)

        # Button
        self.button = Button(self,f"{round(self.ship.angle,2)}")
        self.button.draw_button()

        self.button_2 = Button(self,f"Y = {round(self.ship.ship_direction_2()[0],2)}")
        self.button_2.rect = pygame.Rect(0,self.button_2.height,self.button_2.width,self.button_2.height)
        self.button_2.msg_image_rect.center = self.button_2.rect.center
        self.button_2.draw_button()

        self.button_3 = Button(self, f"X = {round(self.ship.ship_direction_2()[1], 2)}")
        self.button_3.rect = pygame.Rect(0, self.button_3.height*2, self.button_3.width, self.button_3.height)
        self.button_3.msg_image_rect.center = self.button_3.rect.center
        self.button_3.draw_button()


        # Ship
        self.ship.draw_ship()

        # Bullet Shitd
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Enemy Shit
        for enemy in self.enemies.sprites():
            enemy.draw_enemy()

        # Flip
        pygame.display.flip()
        #print(self.ship.image_rect.center)

if __name__ == "__main__":
    play = Game()
    play.loop()