import config
from engine.board.cell import Cell
import pygame
from enum import Enum, auto

class PlayerState(Enum):
    stay = auto()
    right = auto()
    down = auto()
    up = auto()
    
class Player(pygame.sprite.Sprite):
    move_right = [(0, 40, 40, 80), (40, 40, 80, 80), (80, 40, 120, 80), (40, 40, 80, 80), (0, 40, 40, 80)]
    move_left = [(0, 80, 40, 120), (40, 80, 80, 120), (80, 80, 120, 120), (40, 80, 80, 120), (0, 80, 40, 120)]
    move_down = [(0, 120, 40, 160), (40, 120, 80, 160), (80, 120, 120, 160), (40, 120, 80, 160), (0, 120, 40, 160)]
    move_up = [(0, 160, 40, 200), (40, 160, 80, 200), (80, 120, 120, 200), (40, 160, 80, 200), (0, 160, 40, 200)]
    
    def __init__(self, start_cell_px, start_cell_py):
        super().__init__()
        # self.start_cell_px = start_cell_px
        # self.start_cell_py = start_cell_py
        self.player_state = PlayerState.stay
        self.screen_width = config.get_value('screen_width')
        self.screen_height = config.get_value('screen_height')
        self.cell_width = self.cell_height = self.screen_height/20
        start_board_x = self.screen_width/2 - self.cell_width*15/2
        start_board_y = self.screen_height/2 - self.cell_height*15/2
        start_cell_x = start_board_x + start_cell_px*self.cell_width
        start_cell_y = start_board_y + start_cell_py*self.cell_height
        self.image = pygame.Surface((self.cell_width, self.cell_height))
        self.rect = self.image.get_rect()
        self.rect.x = start_cell_x
        self.rect.y = start_cell_y
        self.count = 0
        # self.image.set_colorkey((0, 0, 0))
        Cell.sprite_sheet.set_colorkey((0, 0, 0))
            
    def draw(self, screen): ## тут отрисовка игрока на startcell
        if self.player_state == PlayerState.stay:
            self.image.blit(Cell.sprite_sheet, (0, 0), (120, 0, 160, 40))
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.player_state == PlayerState.right:
            if self.count >= 60:
                self.count = 0
            else:
                self.image.blit(Cell.sprite_sheet, (0, 0), self.move_right[self.count // 15])
                screen.blit(self.image, (self.rect.x, self.rect.y))
                self.count += 1