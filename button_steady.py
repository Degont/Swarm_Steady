import pygame.font

class Button:

    def __init__(self,ai_game, msg):
        """Initialize buttom attributes"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Set the dimensions and properties of the button
        self.width, self.height = self.settings.button_width, self.settings.button_height
        self.button_color = (0,0,0)  # Black
        self.text_color = (230,230,230) # White
        self.font = pygame.font.SysFont(None,48)

        # Build the button's rect object
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.topleft = self.screen_rect.topleft

        # Prep the buttons message
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """Turn msg into a rendered image and center text on button"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color) # font render takes a text and turns it into
        self.msg_image_rect = self.msg_image.get_rect()                               # a surface, takes the message then a bollean
        self.msg_image_rect.center = self.rect.center                                 # representing smoothing of text, then text color
                                                                                      # and text background color
    def draw_button(self):
        # Draw Blank Button and then draw message
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)