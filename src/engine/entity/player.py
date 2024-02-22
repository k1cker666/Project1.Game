import config
from engine.board import cell
import pygame
from enum import Enum, auto
from engine import sprites
from engine import coords

class PlayerDirection(Enum):
    stay = auto()
    right = auto()
    left = auto()
    down = auto()
    up = auto()
    no_direction = auto()
    
class PlayerEventType(Enum):
    NoEvent = auto()
    FoodEvent = auto()

class PlayerEvent:
    type_event: PlayerEventType
    context: dict
    
    def __init__(self, type_event, context = None):
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
    player_direction = PlayerDirection.right
    player_want_direction = PlayerDirection.no_direction
    event = PlayerEvent(type_event = PlayerEventType.NoEvent)
    helthpoints = 4
    score = 0
    current_x = int
    current_y = int
    score_count = 0
    coords = coords.Coords()
    
    def __init__(self):
        super().__init__()
        self.screen_width = config.get_value('screen_width')
        self.screen_height = config.get_value('screen_height')
        self.cell_width = self.cell_height = self.screen_height/20
        self.image = self.sprites.player_stay
        self.rect = self.image.get_rect()
    
    def set_spawn_coord(self, start_cell_px, start_cell_py):
        start_coord_tuple = (start_cell_px, start_cell_py)
        self.rect.x, self.rect.y = self.coords.cells_to_pixels_xy(start_coord_tuple)
          
    def draw(self, screen: pygame.surface.Surface):
        if self.player_direction == PlayerDirection.stay:
            self.image = self.sprites.player_stay
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.player_direction == PlayerDirection.right:
            self.image = self.move_right[self.count // 6]
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.player_direction == PlayerDirection.left:
            self.image = self.move_left[self.count // 6]
            screen.blit(self.image, (self.rect.x, self.rect.y))        
        if self.player_direction == PlayerDirection.down:        
            self.image = self.move_down[self.count // 6]
            screen.blit(self.image, (self.rect.x, self.rect.y))    
        if self.player_direction == PlayerDirection.up:
            self.image = self.move_up[self.count // 6]
            screen.blit(self.image, (self.rect.x, self.rect.y))
                
    def move(self, is_block_ahead: bool, is_cross_ahead: bool):
        left_board_x = self.coords.start_board_x
        up_board_y = self.coords.start_board_y
        right_board_x = self.screen_width-left_board_x
        down_board_y = up_board_y + self.cell_height*15
        coord = self.get_coord()
        x_cell = coord[0]+1
        y_cell = coord[1]+1
        if self.player_direction == PlayerDirection.stay:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y
        if self.player_direction == PlayerDirection.right:
            if self.count >= 20:
                self.count = 0
            else:
                self.count += 1
                self.rect.x += self.speed
            if self.rect.x >= right_board_x-40:
                self.rect.x = left_board_x
            if not is_block_ahead:
                self.rect.x -= self.coords.get_x_in_cell(coord, self.rect.x)
                self.player_direction = PlayerDirection.stay
            if not is_cross_ahead:
                if self.player_want_direction == PlayerDirection.down:
                    want_coord = (coord[0]+1, coord[0])
                    if self.rect.x == self.coords.get_x_in_cell(want_coord, self.rect.x):
                        self.player_direction = PlayerDirection.down
                        self.player_want_direction = PlayerDirection.no_direction
                if self.player_want_direction == PlayerDirection.up:
                    want_coord = (coord[0]+1, coord[0])
                    if self.rect.x == self.coords.get_x_in_cell(want_coord, self.rect.x):
                        self.player_direction = PlayerDirection.up
                        self.player_want_direction = PlayerDirection.no_direction
        if self.player_direction == PlayerDirection.left:
            if self.count >= 20:
                self.count = 0
            else:    
                self.count += 1
                self.rect.x -= self.speed
            if self.rect.x <= left_board_x:
                self.rect.x = right_board_x-40
            if not is_block_ahead:
                self.rect.x = self.coords.cells_to_pixels_x(x_cell)
                self.player_direction = PlayerDirection.stay
        if self.player_direction == PlayerDirection.down:
            if self.count >= 20:
                self.count = 0
            else:    
                self.count += 1
                self.rect.y += self.speed
            if self.rect.y >= down_board_y-40:
                self.rect.y = up_board_y
            if not is_block_ahead:
                self.rect.y -= self.coords.get_y_in_cell(coord, self.rect.y)
                self.player_direction = PlayerDirection.stay
        if self.player_direction == PlayerDirection.up:
            if self.count >= 20:
                self.count = 0
            else:    
                self.count += 1
                self.rect.y -= self.speed
            if self.rect.y <= up_board_y:
                self.rect.y = down_board_y-40
            if not is_block_ahead:
                self.rect.y = self.coords.cells_to_pixels_y(y_cell)
                self.player_direction = PlayerDirection.stay
                
    def get_coord(self):
        return ((self.coords.pixels_to_cells_xy(self.rect.x, self.rect.y)))
        
    def get_player_event(self, event):
        events = {
            0: PlayerEventType.NoEvent,
            1: PlayerEventType.FoodEvent
        }
        return PlayerEvent(type_event=events[event], context={'coords': self.get_coord()})
    
    def interact(self, current_cell):
        x_in_cell, y_in_cell = self.coords.get_xy_in_cell(self.get_coord(), self.rect.x, self.rect.y)
        if isinstance(current_cell, (cell.FoodCell, cell.CrossFoodCell)):
            if self.player_direction == PlayerDirection.right or self.player_direction == PlayerDirection.left:
                if x_in_cell in range(0, 3):
                    self.event = self.get_player_event(1)
                    self.score += 50
                    self.score_count += 1
            if self.player_direction == PlayerDirection.up or self.player_direction == PlayerDirection.down:
                if y_in_cell in range(0, 3):
                    self.event = self.get_player_event(1)
                    self.score += 50
                    self.score_count += 1
                    
    def change_direction(self, direction):
        directions = {1: PlayerDirection.stay,
                      2: PlayerDirection.right,
                      3: PlayerDirection.left,
                      4: PlayerDirection.down,
                      5: PlayerDirection.up}
        self.player_want_direction = directions[direction]
        
    def clear_event(self):
        self.event = self.get_player_event(0)
        
    def clear_score_count(self):
        self.score_count = 0
    
    def get_current_direction(self):
        return self.player_direction.value