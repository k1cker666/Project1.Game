import config
from engine.board import cell
import pygame
from enum import Enum, auto
from engine import sprites
from engine.board import board

class PlayerDirection(Enum):
    stay = auto()
    right = auto()
    left = auto()
    down = auto()
    up = auto()
    
class PlayerEventType(Enum):
    NoEvent = auto()
    FoodEvent = auto()

class PlayerEvent:
    type_event: PlayerEventType
    context: dict
    
    def __init__(self, type_event, context):
        self.type_event = type_event
        self.context = context
        
class Player(pygame.sprite.Sprite):
    sprites = sprites.Image
    move_right = [sprites.player_right_1, sprites.player_right_2, sprites.player_right_3, sprites.player_right_2, sprites.player_right_1]
    move_left = [sprites.player_left_1, sprites.player_left_2, sprites.player_left_3, sprites.player_left_2, sprites.player_left_1]
    move_down = [sprites.player_down_1, sprites.player_down_2, sprites.player_down_3, sprites.player_down_2, sprites.player_down_1]
    move_up = [sprites.player_up_1, sprites.player_up_2, sprites.player_up_3, sprites.player_up_2, sprites.player_up_1]
    count = 0
    speed = 2
    player_direction = PlayerDirection.stay
    event = PlayerEventType.NoEvent
    helthpoints = 4
    score = 0
    current_x = int
    current_y = int
    
    def __init__(self):
        super().__init__()
        self.screen_width = config.get_value('screen_width')
        self.screen_height = config.get_value('screen_height')
        self.cell_width = self.cell_height = self.screen_height/20
        self.image = self.sprites.player_stay
        self.rect = self.image.get_rect()
    
    def set_spawn_coord(self, start_cell_px, start_cell_py):
        self.start_board_x = self.screen_width/2 - self.cell_width*15/2
        self.start_board_y = self.screen_height/2 - self.cell_height*15/2 + 3*self.screen_height/32
        self.rect.x = self.start_board_x + start_cell_px*self.cell_width
        self.rect.y = self.start_board_y + start_cell_py*self.cell_height
          
    def draw(self, screen: pygame.surface.Surface):
        if self.player_direction == PlayerDirection.stay:
            self.image = self.sprites.player_stay
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.player_direction == PlayerDirection.right:
            self.image = self.move_right[self.count // 9]
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.player_direction == PlayerDirection.left:
            self.image = self.move_left[self.count // 9]
            screen.blit(self.image, (self.rect.x, self.rect.y))        
        if self.player_direction == PlayerDirection.down:        
            self.image = self.move_down[self.count // 9]
            screen.blit(self.image, (self.rect.x, self.rect.y))    
        if self.player_direction == PlayerDirection.up:
            self.image = self.move_up[self.count // 9]
            screen.blit(self.image, (self.rect.x, self.rect.y))
                
    def move(self):
        left_board_x = self.start_board_x
        up_board_y = self.start_board_y
        right_board_x = self.screen_width-left_board_x
        down_board_y = up_board_y + self.cell_height*15
        if self.player_direction == PlayerDirection.stay:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y
        if self.player_direction == PlayerDirection.right:
            if self.count >= 40:
                self.count = 0
            else:
                self.count += 1
                self.rect.x += self.speed
            if self.rect.x >= right_board_x-40:
                self.rect.x = left_board_x
        if self.player_direction == PlayerDirection.left:
            if self.count >= 40:
                self.count = 0
            else:    
                self.count += 1
                self.rect.x -= self.speed
            if self.rect.x <= left_board_x:
                self.rect.x = right_board_x-40
        if self.player_direction == PlayerDirection.down:
            if self.count >= 40:
                self.count = 0
            else:    
                self.count += 1
                self.rect.y += self.speed
            if self.rect.y >= down_board_y-40:
                self.rect.y = up_board_y
        if self.player_direction == PlayerDirection.up:
            if self.count >= 40:
                self.count = 0
            else:    
                self.count += 1
                self.rect.y -= self.speed
            if self.rect.y <= up_board_y:
                self.rect.y = down_board_y-40
                
    def get_coord(self):
        current_map_x = int((self.rect.x-self.start_board_x)//40)
        current_map_y = int((self.rect.y-self.start_board_y)//40)
        return ((current_map_x, current_map_y))
        
    def interact(self, current_cell):
        coords = self.get_coord()
        x_in_cell = int(self.rect.x - self.start_board_x - coords[0]*40)
        y_in_cell = int(self.rect.y - self.start_board_y - coords[1]*40)
        if isinstance(current_cell, cell.FoodCell):
            if self.player_direction == PlayerDirection.right or self.player_direction == PlayerDirection.left:
                if x_in_cell in range(6, 9):
                    self.event = PlayerEventType.FoodEvent
                    self.score += 50
            if self.player_direction == PlayerDirection.up or self.player_direction == PlayerDirection.down:
                if y_in_cell in range(6, 9):
                    self.event = PlayerEventType.FoodEvent
                    self.score += 50
                    
    def change_direction(self, direction):
        directions = {0: PlayerDirection.stay,
                      1: PlayerDirection.right,
                      2: PlayerDirection.left,
                      3: PlayerDirection.down,
                      4: PlayerDirection.up}
        self.player_direction = directions[direction]
        
    def clear_event(self):
        self.event = PlayerEventType.NoEvent