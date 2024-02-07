import menu
import pygame
from engine.board import board 
from enum import Enum, auto
import config

class StateManager(Enum):
    in_menu = auto()
    game_process = auto()
    
class GameManager:
    board = board.Board() # конструимруем объект класса Board
    game_state = StateManager.in_menu
    num = 0
    
    def __init__(self):
        level_name = GameManager.change_level(self.num) # file не нужно использовать через self
        self.board.load(level_name)
                
    def run(self, screen):
        while True:
            if GameManager.game_state == StateManager.in_menu:
                screen.fill((180, 20, 204))
                menu.print_menu(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            GameManager.game_state = StateManager.game_process
                        if event.key == pygame.K_3:
                            return 
            if GameManager.game_state == StateManager.game_process:
                background = pygame.image.load('./images/testbg.png')
                screen.blit(background, (0, 0))
                self.board.draw(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            GameManager.game_state = StateManager.in_menu
            pygame.display.flip()

    def change_level(num):
        level_list = config.get_value('levels')
        level_name = level_list[num]['map_file']
        GameManager.num +=1
        return level_name
        

    