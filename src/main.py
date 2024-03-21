import config
import pygame
import sys
from engine import game_manager

def init_game():
    pygame.mixer.pre_init(44100, -16, 1, 512)
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

def init_sound(file):
    sound = pygame.mixer.Sound(file)
    sound.set_volume(0.3)
    return sound

screen = init_game()
sounds = {
    'food': init_sound('./sounds/food.wav'),
    'enemy_attack': init_sound('./sounds/enemyattack.wav'),
    'level_up': init_sound('./sounds/levelup.wav')
}
game_manager = game_manager.GameManager(sounds)
game_manager.run(screen)
quit_game()