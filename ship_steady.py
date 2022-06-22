import pygame

class Ship():
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/rocket.bmp")
        self.image = pygame.transform.scale(self.image,(60,48))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center
        self.speed = 2

        #Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #movement counter
        self.movement_counter = False

    def update_pos(self):
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.x += self.speed
            self.movement_counter = True
            t = 0

            while self.movement_counter:

                if t%40 == 0:
                    self.image

                t += 1


            self.image = pygame.transform.rotate(self.image,30)
        if self.moving_left and self.image_rect.left > self.screen_rect.left:
            self.image_rect.x -= self.speed
        if self.moving_up and self.image_rect.top > self.screen_rect.top:
            self.image_rect.y -= self.speed
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.y += self.speed


    def draw_ship(self):
        self.screen.blit(self.image,self.image_rect)