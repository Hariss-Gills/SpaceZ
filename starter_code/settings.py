import pygame

WHITE = (255, 255, 255)

class Settings():
       """A class to store all settings for the game."""
       
       def __init__(self):
           """Initialize the game's settings."""

           # Screen settings
           self.screen_width = 1200
           self.screen_height = 750

           # Background image 
           self.screen_backgrnd = pygame.image.load('media/mars_background.png')
           self.bg_color = WHITE

           # Load a sound to play on impacts between sprites
           self.boom_sound = pygame.mixer.Sound('media/boom.wav')
           
           # Game settings
           self.lives = 3
           self.score = 0
           self.aliens = 20