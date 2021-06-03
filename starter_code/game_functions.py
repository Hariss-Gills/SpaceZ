import sys, pygame # imports

pygame.font.init() # initalize font module


RED = (252, 3, 3) # RGB red 
# Font that will be used to display stats
FONT_NAME = pygame.font.match_font('arial')

def check_events(screen, ship, sprites, coin_sprites):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship right.
                ship.right()
            elif event.key == pygame.K_LEFT:
                # Move ship left.
                ship.left()
            elif event.key == pygame.K_q:
                # Move ship up.
                ship.up()
            elif event.key == pygame.K_a:
                # Move ship down.
                ship.down()
            if event.key == pygame.K_SPACE and ship.bitcoin_miner >= 100:
                ship.shoot(sprites, coin_sprites)
                # Shoot coins and add them to the groups sprites and coin_sprites


def update_screen(sprites, ai_settings, screen, ship):
    """Update sprites & messages on the screen.""" 

    sprites.draw(screen)
    draw_stat(screen, ship, ai_settings) # draw stats to the screen
    
    if ship.damage >= 100: # draw 'You have crashed' once damage = 100
        draw_text(screen, "You Have Crashed!", 70, ai_settings.screen_width//2, ai_settings.screen_height//2)
        ship.reset_pos() # reset ship's position to the start 
             
    
    # Update the background region.
    pygame.display.update()


def draw_stat(screen, ship, ai_settings):
    """draw each individual stat to screen detailing size and postion"""
    zerofy_stat(screen, ship.damage, 15, 110, 14)
    zerofy_stat(screen, ai_settings.lives, 15, 245, 14)
    zerofy_stat(screen, ai_settings.score, 15, 110, 40)
    zerofy_stat(screen, ship.bitcoin_miner, 15, 350, 38)


def zerofy_stat(screen, stat, size, x, y):
    """print to screen with 3 digits"""
    if stat >= 10 and stat < 100:
        draw_text(screen, "0" + str(stat) , size, x, y) # 2 digits - add one zero
    elif stat >= 100:
        draw_text(screen, str(stat) , size, x, y) # already 3 digits
    else:
        draw_text(screen, 2 * "0" + str(stat) , size, x, y) # 1 digit - add 2 zeros


def draw_text(surf, text, size, x, y): # Based on http://kidscancode.org/blog/2016/08/pygame_shmup_part_7/
    """function to draw any text to screen"""
    font = pygame.font.Font(FONT_NAME, size) # Indicate we are using 'arial'
    text_surface = font.render(text, True, RED) # With anti-alising 
    text_rect = text_surface.get_rect() 
    text_rect.midtop = (x, y) # Set midtop attribute 
    surf.blit(text_surface, text_rect) # blit the text to screen
        