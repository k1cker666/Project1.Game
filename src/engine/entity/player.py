import config
from engine.board import cell
import pygame
from enum import Enum, auto
from engine import image

class PlayerDirection(Enum):
    stay = auto()
    right = auto()
    left = auto()
    down = auto()
    up = auto()
    
class Player(pygame.sprite.Sprite):
    images = image.Image
    move_right = [images.player_right_1, images.player_right_2, images.player_right_3, images.player_right_2, images.player_right_1]
    move_left = [images.player_left_1, images.player_left_2, images.player_left_3, images.player_left_2, images.player_left_1]
    move_down = [images.player_down_1, images.player_down_2, images.player_down_3, images.player_down_2, images.player_down_1]
    move_up = [images.player_up_1, images.player_up_2, images.player_up_3, images.player_up_2, images.player_up_1]
    count = 0
    player_direction = PlayerDirection.stay
    
    def __init__(self, start_cell_px, start_cell_py):
        super().__init__()
        self.screen_width = config.get_value('screen_width')
        self.screen_height = config.get_value('screen_height')
        self.cell_width = self.cell_height = self.screen_height/20
        self.start_board_x = self.screen_width/2 - self.cell_width*15/2
        self.start_board_y = self.screen_height/2 - self.cell_height*15/2
        start_cell_x = self.start_board_x + start_cell_px*self.cell_width
        start_cell_y = self.start_board_y + start_cell_py*self.cell_height
        self.image = self.images.player_stay
        self.rect = self.image.get_rect()
        self.rect.x = start_cell_x
        self.rect.y = start_cell_y
        
            
    def draw(self, screen):
        if self.player_direction == PlayerDirection.stay:
            self.image = self.images.player_stay
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.player_direction == PlayerDirection.right:
            self.image = self.move_right[self.count // 7]
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.player_direction == PlayerDirection.left:
            self.image = self.move_left[self.count // 7]
            screen.blit(self.image, (self.rect.x, self.rect.y))        
        if self.player_direction == PlayerDirection.down:        
            self.image = self.move_down[self.count // 7]
            screen.blit(self.image, (self.rect.x, self.rect.y))    
        if self.player_direction == PlayerDirection.up:
            self.image = self.move_up[self.count // 7]
            screen.blit(self.image, (self.rect.x, self.rect.y))
                
    def move(self):
        left_board_x = self.start_board_x
        up_board_y = self.start_board_y
        right_board_x = self.screen_width-self.start_board_x
        down_board_y = self.screen_height-self.start_board_y
        if self.player_direction == PlayerDirection.right:
            if self.count >= 30:
                self.count = 0
            else:
                self.count += 1
                self.rect.x += 3
            if self.rect.x >= right_board_x-40:
                self.rect.x = left_board_x
        if self.player_direction == PlayerDirection.left:
            if self.count >= 30:
                self.count = 0
            else:    
                self.count += 1
                self.rect.x -= 3
            if self.rect.x <= left_board_x:
                self.rect.x = right_board_x-40
        if self.player_direction == PlayerDirection.down:
            if self.count >= 30:
                self.count = 0
            else:    
                self.count += 1
                self.rect.y += 3
            if self.rect.y >= down_board_y-40:
                self.rect.y = up_board_y
        if self.player_direction == PlayerDirection.up:
            if self.count >= 30:
                self.count = 0
            else:    
                self.count += 1
                self.rect.y -= 3
            if self.rect.y <= up_board_y:
                self.rect.y = down_board_y-40