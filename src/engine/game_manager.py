import menu
import pygame
from engine.board import board 
from enum import Enum, auto
import config

class GameManager:
    board = board.Board() # конструимруем объект класса Board
    game_state = 1
    num = 0
    
    def __init__(self):
        self.game_state = StateManager.in_menu.value
        level_name = GameManager.change_level(self.num) # file не нужно использовать через self
        self.board.load(level_name)
                
    def run(self, screen):
        running = True
        while running:
            if GameManager.game_state == StateManager.in_menu.value:
                screen.fill((180, 20, 204))
                menu.print_menu(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            GameManager.game_state = StateManager.game_process.value
                        if event.key == pygame.K_3:
                            running = False 
            if GameManager.game_state == StateManager.game_process.value:
                background = pygame.image.load('./images/testbg.png')
                screen.blit(background, (0, 0))
                self.board.draw(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            GameManager.game_state = StateManager.in_menu.value
            pygame.display.flip()

    def change_level(num):
        level_list = config.get_value('levels')
        level_name = level_list[num]['map_file']
        GameManager.num +=1
        return level_name
        
class StateManager(Enum):
    in_menu = auto()
    game_process = auto()
    