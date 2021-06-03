import pygame, os, random # imports

BLACK = (0, 0, 0) # RGB black

class Roadster(pygame.sprite.Sprite):
    """Roadster sprite class as a subclass of pygame Sprite class"""
    def __init__(self, settings):
        global ai_settings # retrieve ai_settings object from spaceZ.py
        ai_settings = settings
        pygame.sprite.Sprite.__init__(self)
        # Load the image of a Roadster and set it as the image for this sprite (Based of practical)
        self.image = pygame.image.load(os.path.join('media', 'roadster.png'))
        # Handle the black background of the sprite (so we don't see it) (Based of practical)
        self.image.set_colorkey(BLACK)
        # Get the sprite's rect
        self.rect = self.image.get_rect()
        self.reset() # Set fixed x and random y position and random velocity between (1,10)

    def update(self):
        """Method to Control Movment"""
        self.rect.x -= self.velocity
        if self.rect.right < 0:
            self.reset() # reset velocity and position if goes off to left of screen
    
    def reset(self):
        """Method to set attributes"""
        self.rect.y = random.randrange(ai_settings.screen_height - self.rect.height) # Start on random y postion between height of sceen and heigh of sprite  
        self.rect.x = ai_settings.screen_width # Start left of the screen
        self.velocity = random.randint(1,10) # random int between 1 and 10

