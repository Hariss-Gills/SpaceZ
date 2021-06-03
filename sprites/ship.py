import pygame, os, sys, random # imports
from sprites.bitcoin import Bitcoin, Supercoin # import Supercoins and Bitcoins

BLACK = (0, 0, 0) # RGB black

class Starship(pygame.sprite.Sprite):
    """Startship sprite class as a subclass of pygame Sprite class"""
    def __init__(self, settings):
        global ai_settings # retrieve ai_settings object from spaceZ.py
        ai_settings = settings
        pygame.sprite.Sprite.__init__(self)
        # Load the image of a Starship and set it as the image for this sprite (Based of practical)
        self.image = pygame.image.load(os.path.join('media', 'starship.png'))
        # Handle the black background of the sprite (so we don't see it) (Based of practical)
        self.image.set_colorkey(BLACK)
        # Get the sprite's rect
        self.rect = self.image.get_rect()
        self.reset_pos() # Set position
        # Set Speed
        self.velocity_x = 5 
        self.velocity_y = 5
        # Set damage level and bitcoin miner
        self.damage = 0
        self.bitcoin_miner = 0

    def shoot(self, sprites, coin_sprites):
        """Method to handle shooting of coin"""
        self.bitcoin_miner = 0 # reset miner
        choice = random.choice([0, 1]) # 50% generation of type of coin
        if choice == 0:
            coin = Supercoin(self.rect.right, self.rect.bottom - 10, ai_settings)
        else:
            coin = Bitcoin(self.rect.right, self.rect.bottom - 10, ai_settings)
        
        sprites.add(coin)
        coin_sprites.add(coin) # add to groups
           
    # Movement based on https://github.com/techwithtim/PygameForBeginners/blob/main/main.py       
    
    def right(self):
        if self.rect.x  + self.velocity_x + self.rect.width < ai_settings.screen_width:  # RIGHT as long as not off screen
            self.rect.x += self.velocity_x

    def left(self):
        if self.rect.x - self.velocity_x > 0:  # LEFT as long as not off screen
            self.rect.x -= self.velocity_x
    def up(self):
        if self.rect.y - self.velocity_y > 0:  # UP as long as not off screen
            self.rect.y -= self.velocity_y

    def down(self):
        if self.rect.y + self.velocity_y + self.rect.height < ai_settings.screen_height:  # DOWN as long as not off screen
            self.rect.y += self.velocity_y            


    def reset_pos(self):
        self.rect.y = ai_settings.screen_height//2 # y positon in the middle
        self.rect.x = 200 # fixed x positon
