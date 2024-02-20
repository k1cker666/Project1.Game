import config
import pygame
import sys
from engine import game_manager

def init_game():
    pygame.init()
    config.init()
    width = config.get_value('screen_width')
    height = config.get_value('screen_height')
    game_name = config.get_value('game_name')
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(game_name)
    icon = pygame.image.load('./images/ghost.png')
    pygame.display.set_icon(icon)
    return screen

def quit_game():
    config.save()
    pygame.quit()
    sys.exit()

screen = init_game()
game_manager = game_manager.GameManager()
game_manager.run(screen)
quit_game()