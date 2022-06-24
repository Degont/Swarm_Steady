import pygame
import math

class Ship():
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/rocket.bmp")
        self.image = pygame.transform.scale(self.image,(60,48))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.midbottom
        self.image_rect.y -= 40
        self.speed = game.settings.ship_speed
        self.c_state = 1  # 1 for mouse, 0 for center of screen
        self.angle = 0

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

        # state configuration (mouse or screen center)
        if self.c_state == 1:
            center = pygame.mouse.get_pos()
        else:
            center = self.screen_rect.center


        # Calculations
        vertical_line = center[1] - self.image_rect.center[1]  # this is the magnitude of the vertical line
        horizontal_line = center[0] - self.image_rect.center[0]  # this is the magnitude of the horizontal line

        try:
            if vertical_line == 0:  # purely handles when the vertical line is zero
                if center[0] > self.image_rect.center[0]:  # means the ship is on the left of the center
                    self.rotated_image = pygame.transform.rotate(self.image,270)
                    self.rotated_image_rect = self.rotated_image.get_rect()
                    self.rotated_image_rect.center = self.image_rect.center

                else:
                    self.rotated_image = pygame.transform.rotate(self.image, 90)
                    self.rotated_image_rect = self.rotated_image.get_rect()
                    self.rotated_image_rect.center = self.image_rect.center

            else:
                if self.image_rect.center[1] < center[1]:
                    inverter = 180  # means ship is over the center point
                elif self.image_rect.center[1] > center[1]:
                    inverter = 0
                else:
                    inverter = 360

                angle = math.atan(horizontal_line / vertical_line) * (180 / math.pi)
                self.angle = angle

                self.rotated_image = pygame.transform.rotate(self.image, angle + inverter)

                self.rotated_image_rect = self.rotated_image.get_rect()
                self.rotated_image_rect.center = self.image_rect.center

        except ZeroDivisionError:
            pass

        return self.rotated_image, self.rotated_image_rect

    def ship_direction_2(self):

        # state check
        if self.c_state == 1:
            end_point = pygame.mouse.get_pos()
        else:
            end_point = self.screen_rect.center

        # magnitudes
        vert_mag = end_point[1] - self.image_rect.center[1]
        hori_mag = end_point[0] - self.image_rect.center[0]

        # Inverter
        if hori_mag > 0:  # this means ship to the left
            inverter = 1
        else:
            inverter = -1

        # slope Calc
        try:
            slope_y = vert_mag/hori_mag
            if hori_mag > 0:  # means ship is to the left
                slope_x = 1
            else:
                slope_x = -1

        except ZeroDivisionError:
            if vert_mag == 0:  # y axis are the same therefore parallel heights
                if hori_mag > 0:  # means ship is to the left
                    slope_x = 1
                    slope_y = 0
                else:
                    slope_x = -1
                    slope_y = 0
            if hori_mag == 0:
                if vert_mag > 0:
                    slope_y = -1
                    slope_x = 0
                else:
                    slope_y = 1
                    slope_x = 0

        return slope_y*inverter, slope_x



    def draw_ship(self):

        # actual drawing
        state = 1
        if state == 1:
            rotated_image = self._rotate_ship()  # this gives this function the tuple for my rotated ships
            #self.screen.fill((0, 0, 0,), rotated_image[1])
            #self.screen.fill((0, 0, 255,), self.image_rect)
            self.screen.blit(rotated_image[0], rotated_image[1])
            #pygame.draw.circle(self.screen,(255,0,0),rotated_image[1].center,10)

        else:
            rotated_image = self.image
            self.screen.blit(rotated_image, self.image_rect)


        if self.c_state == 1:
            end_point = pygame.mouse.get_pos()
        else:
            end_point = self.screen_rect.center

        pygame.draw.line(self.screen,(0,0,0),self.image_rect.center,end_point,1)
        pygame.draw.line(self.screen,(0,0,255,),(end_point[0],self.image_rect.center[1]),end_point,1)  # vertical
        pygame.draw.line(self.screen, (255, 0, 0,), self.image_rect.center, (end_point[0], self.image_rect.center[1]), 1)  # horizontal