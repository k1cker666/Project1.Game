import menu
import pygame
from engine.board import board 
from enum import Enum, auto
import config
from engine.entity import player

class StateManager(Enum):
    in_menu = auto()
    game_process = auto()
    
class GameManager:
    clock = pygame.time.Clock()
    game_state = StateManager.in_menu
    num = 0
    
    def __init__(self):
        self.FPS = config.get_value('FPS')
        level_name = self.change_level(self.num)
        self.board = board.Board(level_name)
        start_cell_px, start_cell_py = self.board.find_start_cell()
        self.player = player.Player(start_cell_px, start_cell_py)
                
    def run(self, screen):
        while True:
            if self.game_state == StateManager.in_menu:
                screen.fill((180, 20, 204))
                menu.print_menu(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.game_state = StateManager.game_process
                        if event.key == pygame.K_3:
                            return 
            if self.game_state == StateManager.game_process:
                background = pygame.image.load('./images/testbg.png')
                screen.blit(background, (0, 0))
                self.board.draw(screen)
                self.player.draw(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.player.moving_right(screen)
                        if event.key == pygame.K_ESCAPE:
                            self.game_state = StateManager.in_menu
            pygame.display.flip()
            self.clock.tick(self.FPS)

    def change_level(self, num):
        level_list = config.get_value('levels')
        level_name = level_list[num]['map_file']
        self.num +=1
        return level_name
        

    