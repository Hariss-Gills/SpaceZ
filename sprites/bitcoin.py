import pygame, os, random, math # imports 

BLACK = (0, 0, 0) # RGB black

class Bitcoin(pygame.sprite.Sprite):
    """Bitcoin sprite class as a subclass of pygame Sprite class"""
    def __init__(self, x, y, settings):
        global ai_settings # retrieve ai_settings object from spaceZ.py
        ai_settings = settings
        pygame.sprite.Sprite.__init__(self)
        # Load the image of a coin and set it as the image for this sprite (Based of practical)
        self.image = pygame.image.load(os.path.join('media', 'bitcoin.png'))
        # Handle the black background of the sprite (so we don't see it) (Based of practical)
        self.image.set_colorkey(BLACK)
        # Get the sprite's rect
        self.rect = self.image.get_rect()
        #Set position and speed
        self.rect.bottom = y
        self.rect.centerx = x
        self.velocity_x = 10

    def update(self):
        """Method to Control Movment"""
        self.rect.x += self.velocity_x
        # kill if it moves off the top of the screen
        if self.rect.x > ai_settings.screen_width:
            self.kill()
      
class Dogecoin(Bitcoin,pygame.sprite.Sprite): # Based on https://www.programmersought.com/article/68131128566/
    """coin sprite class as a subclass of Bitcoin"""
    def __init__(self, x, y, settings):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x, y, settings)
        self.image = pygame.image.load(os.path.join('media', 'dogecoin-doge-logo.png'))
        self.reset_angle() # Set angle of movement
        self.velocity_y = 10 # Set velocity along vertical axis

    def update(self):
        """Method to Control Movment"""
        # Updated postion based on angle
        self.rect.x += self.velocity_x * math.cos(self.angle)
        self.rect.y += self.velocity_y * math.sin(self.angle)
        # kill if it moves off the screen
        if self.rect.x > ai_settings.screen_width or self.rect.x < 0:
            self.kill()
        if self.rect.y > ai_settings.screen_height or self.rect.y < 0:
            self.kill()
    
    def reset_angle(self):
        """Method to Set Angle"""
        self.angle = math.pi * (random.randint(0, 359) / 180) # angle between [0-359]