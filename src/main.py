import config
import menu
import pygame
import sys

def init_game():
    pygame.init()
    config.init()
    width = config.get_value('screen_width')
    height = config.get_value('screen_height')
    game_name = config.get_value('game_name')
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(game_name)
    screen.fill((180, 20, 204))
    icon = pygame.image.load('./images/ghost.png')
    pygame.display.set_icon(icon)
    return screen

def quit_game():
    config.save()
    pygame.quit()
    sys.exit()

screen = init_game()

while True:
    menu.print_menu(screen)
    pygame.display.flip()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                screen.fill((236, 253, 0))
            elif event.key == pygame.K_3:
                quit_game()