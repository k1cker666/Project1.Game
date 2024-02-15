import config
from engine.board.cell import Cell
import pygame
from enum import Enum, auto
from engine import image

class PlayerState(Enum):
    stay = auto()
    right = auto()
    left = auto()
    down = auto()
    up = auto()
    
class Player(pygame.sprite.Sprite):
    images = image.Image
    move_right = [images.player_right_1, images.player_right_2, images.player_right_3, images.player_right_2, images.player_right_1]
    move_left = [images.player_left_1, images.player_left_2, images.player_left_3, images.player_left_2, images.player_left_1]
    # move_down = [(0, 120, 40, 130), (40, 120, 80, 130), (80, 120, 120, 130), (40, 120, 80, 130), (0, 120, 40, 130)]
    # move_up = [(0, 130, 40, 200), (40, 130, 80, 200), (80, 120, 120, 200), (40, 130, 80, 200), (0, 130, 40, 200)]
    
    def __init__(self, start_cell_px, start_cell_py):
        super().__init__()
        self.player_state = PlayerState.stay
        self.screen_width = config.get_value('screen_width')
        self.screen_height = config.get_value('screen_height')
        self.cell_width = self.cell_height = self.screen_height/20
        start_board_x = self.screen_width/2 - self.cell_width*15/2
        start_board_y = self.screen_height/2 - self.cell_height*15/2
        start_cell_x = start_board_x + start_cell_px*self.cell_width
        start_cell_y = start_board_y + start_cell_py*self.cell_height
        self.image = self.images.player_stay
        self.rect = self.image.get_rect()
        self.rect.x = start_cell_x
        self.rect.y = start_cell_y
        self.count = 0
        
            
    def draw(self, screen):
        if self.player_state == PlayerState.stay:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.player_state == PlayerState.right:
            if self.count >= 30:
                self.count = 0
            else:
                self.image = self.move_right[self.count // 7]
                screen.blit(self.image, (self.rect.x, self.rect.y))
                self.count += 1
                self.rect.x += 3
        if self.player_state == PlayerState.left:
            if self.count >= 30:
                self.count = 0
            else:
                self.image = self.move_left[self.count // 7]
                screen.blit(self.image, (self.rect.x, self.rect.y))
                self.count += 1
                self.rect.x -= 3