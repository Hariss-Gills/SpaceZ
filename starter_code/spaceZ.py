import pygame, os, sys
# .path hack to import modules from sprite folder from sibling directory
path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(path)
# COMPLETE FILE PROVIDED IN STARTER CODE
from settings import Settings

# PARTIAL FILE PROVIDED IN STARTER CODE
import game_functions as gf
# import all the sprites 
from sprites.aliens import Roadster
from sprites.ship import Starship
import sprites.bitcoin

def handle_star_road_collison(ship, hit_roadsters, ai_settings):
    """handles collison between starship and roadsters"""
    for roadster in hit_roadsters:
        ai_settings.boom_sound.play() # play boom for each hit roadster
        ship.damage += 10 # increase by 10 for each roadster
        roadster.reset() # reset postion and speed of each roadster

def handle_coin_road_collison(hit_roadsters_with_coins, hit_coin_with_roadsters, ai_settings):
    """handles collison between coins and roadsters"""
    for coin in hit_coin_with_roadsters:
        if type(coin) == sprites.bitcoin.Bitcoin:
            coin.kill() #if bitcoin hits, destroy itself
        else:
            coin.reset_angle() #if Dogecoin hits, reset angle
    for roadster in hit_roadsters_with_coins:
        ai_settings.boom_sound.play() # play boom for each hit roadster
        ai_settings.score += 10 # increase by 10 for each roadster
        roadster.reset() # reset postion and speed of each roadster
            
def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    pygame.mixer.init()
    # Set keys to repeat if held down.
    pygame.key.set_repeat(5,5)
    
    # Create settings object containing game settings
    ai_settings = Settings()
    
    # Create the main game screen
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.blit(ai_settings.screen_backgrnd, (0, 0))
    
    # Create a main window caption
    pygame.display.set_caption("Space Z - Mars Flight")

    while ai_settings.lives > 0:
        # Create Groups
        sprites = pygame.sprite.Group()
        roadster_sprites = pygame.sprite.Group()
        coin_sprites = pygame.sprite.Group()
        
        # Create Sprites and add then in their groups
        for i in range(ai_settings.aliens):
            r = Roadster(ai_settings)
            sprites.add(r)
            roadster_sprites.add(r)
            sprites.add(r)
        ship = Starship(ai_settings)
        sprites.add(ship)

        # Refresh the background
        screen.blit(ai_settings.screen_backgrnd, (0, 0))
        sprites.clear(screen, ai_settings.screen_backgrnd)
        
        # Start the main loop for the game.
        while ship.damage < 100:
            pygame.display.update()
            screen.blit(ai_settings.screen_backgrnd, (0, 0))
            
            if ship.bitcoin_miner < 100:
                ship.bitcoin_miner += 1
            # Watch for keyboard events.
            gf.check_events(screen, ship, sprites, coin_sprites)
            # Tell all the sprites to update their status
            sprites.update()

            # Get list of hit roadsters from roadster_sprites group ship sprite collisons and handle them
            hit_roadsters = pygame.sprite.spritecollide(ship, roadster_sprites, False)
            handle_star_road_collison(ship, hit_roadsters, ai_settings)

            # Get list of hit roadsters and coins from roadster_sprites and coin_sprites collison groups and handle them
            hit_roadsters_with_coins = pygame.sprite.groupcollide(roadster_sprites, coin_sprites, False, False)
            hit_coin_with_roadsters = pygame.sprite.groupcollide(coin_sprites, roadster_sprites, False, False)
            handle_coin_road_collison(hit_roadsters_with_coins, hit_coin_with_roadsters,ai_settings)

            # Now update the sprites, etc. on the screen
            gf.update_screen(sprites, ai_settings, screen, ship)
            
        # Wait for a keypress to continue
        null_event = pygame.event.wait() 
        # Remove a life
        ai_settings.lives -= 1

    # GAME ENDS 

# Call the main method to start the game
if __name__ == "__main__":        
    run_game()
