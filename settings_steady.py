class Settings():

    def __init__(self):
        # Screen stuff
        self.bg_color = (230,230,230)
        self.screen_width = 1200
        self.screen_height = 800

        # ship settings
        self.ship_speed = 1

        # button
        self.button_width = 200
        self.button_height = 50

        # bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 0.5
        self.bullet_color = (70,70,70)
        self.bullets_allowed = 10

        # enemy
        self.enemy_speed = 0.2
        self.enemy_limit = 10