import pygame
import math

class Ship():
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/rocket.bmp")
        self.image = pygame.transform.scale(self.image,(60,48))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center
        self.speed = 0.5

        self.x = float(self.image_rect.x)
        self.y = float(self.image_rect.y)

        #Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #movement counter
        self.movement_counter = False

    def update_pos(self):
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.image_rect.left > self.screen_rect.left:
            self.x -= self.speed
        if self.moving_up and self.image_rect.top > self.screen_rect.top:
            self.y -= self.speed
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        self.image_rect.x = self.x
        self.image_rect.y = self.y


    def _rotate_ship(self):
        # rotating ship to stay facing the center of the screen
        """the angle that Im looking for is the tan theta of the opposite over adjacent, rotating to that angle should allow me always feel that force"""

        # Variables

        val = 0
        if val == 1:
            center = pygame.mouse.get_pos()
        else:
            center = self.screen_rect.center

        vertical_line = center[0] - self.image_rect.center[0]  # this is the magnitude of the vertical line
        horizontal_line = center[1] - self.image_rect.center[1]  # this is the magnitude of the horizontal line

        try:
            if self.image_rect[1] < center[1]:
                inverter = 180
            else:
                inverter = 0

            angle = math.atan(vertical_line / horizontal_line) * (180 / math.pi)

            rotated_image = pygame.transform.rotate(self.image, angle + inverter)

            rotated_image_rect = rotated_image.get_rect()
            rotated_image_rect.center = self.image_rect.center

            #self.x = float(self.image_rect.x)
            #self.y = float(self.image_rect.y)


        except ZeroDivisionError:
            if inverter == 180:
                rotated_image = self.image
                rotated_image_rect = rotated_image.get_rect()
            else:
                rotated_image = pygame.transform.rotate(self.image, 180)
                rotated_image_rect = rotated_image.get_rect()
            pass

        return rotated_image, rotated_image_rect


    def draw_ship(self):

        # actual drawing
        state = 1
        if state == 1:
            rotated_image = self._rotate_ship()
            self.screen.fill((0, 0, 0,), rotated_image[1])
            self.screen.fill((0, 0, 255,), self.image_rect)
            #self.screen.blit(rotated_image[0], self.image_rect)
            pygame.draw.circle(self.screen,(255,0,0),rotated_image[1].midtop,10)

        else:
            rotated_image = self.image
            self.screen.blit(rotated_image, self.image_rect)

        pygame.draw.line(self.screen,(0,0,0),self.image_rect.midtop,self.screen_rect.center,1)
        pygame.draw.line(self.screen,(0,0,255,),self.screen_rect.center,(600,self.image_rect.top),1)  # vertical
        pygame.draw.line(self.screen, (255, 0, 0,), self.image_rect.midtop, (600, self.image_rect.top), 1)  # horizontal


    def junk(self):
        left_corner_x = self.image_rect.topleft[0] + math.cos(math.radians(angle))
        left_corner_y = self.image_rect.topleft[1] + math.sin(math.radians(angle))
        right_corner_x = self.image_rect.topright[0] + math.cos(math.radians(angle))
        right_corner_y = self.image_rect.topright[1] + math.sin(math.radians(angle))
        pygame.draw.line(self.screen, (255, 0, 0), (left_corner_x, left_corner_y), (right_corner_x, right_corner_y), 1)