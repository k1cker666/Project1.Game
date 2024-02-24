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
    
    speed = 2

    player_direction = PlayerDirection.stay
    player_want_direction = PlayerDirection.no_direction
    
    event = PlayerEvent(type_event = PlayerEventType.NoEvent)
    
    helthpoints = 4

    score = 0 #TODO: total_score
    score_count = 0 #TODO: curr_level_score


    coords = coords.Coords()

    count = 0 #TODO: переименовать, чтобы было понятно что мы считаем
    #TODO: Перенести в image: sprites.Image.move_right[5]
    move_right = [sprites.player_right_1, sprites.player_right_2, sprites.player_right_3, sprites.player_right_2, sprites.player_right_1]
    move_left = [sprites.player_left_1, sprites.player_left_2, sprites.player_left_3, sprites.player_left_2, sprites.player_left_1]
    move_down = [sprites.player_down_1, sprites.player_down_2, sprites.player_down_3, sprites.player_down_2, sprites.player_down_1]
    move_up = [sprites.player_up_1, sprites.player_up_2, sprites.player_up_3, sprites.player_up_2, sprites.player_up_1]

    def __init__(self):
        super().__init__()
        self.screen_width = config.get_value('screen_width')
        self.screen_height = config.get_value('screen_height')
        self.cell_width = self.cell_height = self.screen_height/20
        self.rect = self.sprites.player_stay.get_rect()
    
    def set_spawn_coord(self, start_cell):
        self.rect.x, self.rect.y = self.coords.cells_to_pixels_xy(start_cell)
          
    def draw(self, screen: pygame.surface.Surface):
        if self.player_direction == PlayerDirection.stay:
            screen.blit(self.sprites.player_stay, (self.rect.x, self.rect.y))
        if self.player_direction == PlayerDirection.right:
            screen.blit(self.move_right[self.count // 6], (self.rect.x, self.rect.y))
        if self.player_direction == PlayerDirection.left:
            screen.blit(self.move_left[self.count // 6], (self.rect.x, self.rect.y))        
        if self.player_direction == PlayerDirection.down:        
            screen.blit(self.move_down[self.count // 6], (self.rect.x, self.rect.y))    
        if self.player_direction == PlayerDirection.up:
            screen.blit(self.move_up[self.count // 6], (self.rect.x, self.rect.y))

    def calculate_count_animation(self):
        if self.count >= 20:
            self.count = 0
            self.player_want_direction = PlayerDirection.no_direction
        else:    
            self.count += 1

    def move(self, is_block_ahead):
        coord = self.get_coord() #текущее
        x_cell = coord[0]+1
        y_cell = coord[1]+1
        

        self.calculate_count_animation()

        x_start_cell = self.coords.get_x_in_cell(coord, self.rect.x)
        y_start_cell = self.coords.get_y_in_cell(coord, self.rect.y)

        is_block = is_block_ahead(self.get_coord(), self.player_direction.value)
        print(self.player_direction.value, is_block, x_start_cell, y_start_cell)

        if x_start_cell == 0 and y_start_cell == 0 and self.player_direction != self.player_want_direction and self.player_want_direction != PlayerDirection.no_direction and not is_block_ahead(self.get_coord(), self.player_want_direction.value):
            print('move available')
            is_block=False
            self.player_direction = self.player_want_direction
            self.player_want_direction = PlayerDirection.no_direction
    
        if self.player_direction == PlayerDirection.stay:
            return

        if self.player_direction == PlayerDirection.right:

            self.rect.x += self.speed
    
            if is_block:
                self.rect.x -= self.coords.get_x_in_cell(coord, self.rect.x)
                self.player_direction = PlayerDirection.stay

        if self.player_direction == PlayerDirection.left:
            
            self.rect.x -= self.speed
            
            if is_block:
                self.rect.x = self.coords.cells_to_pixels_x(x_cell)
                self.player_direction = PlayerDirection.stay

        if self.player_direction == PlayerDirection.down:
            self.rect.y += self.speed
    
            if  is_block:
                self.rect.y -= self.coords.get_y_in_cell(coord, self.rect.y)
                self.player_direction = PlayerDirection.stay

        if self.player_direction == PlayerDirection.up:

            self.rect.y -= self.speed

            if  is_block:
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
                    self.score_count += 50
            if self.player_direction == PlayerDirection.up or self.player_direction == PlayerDirection.down:
                if y_in_cell in range(0, 3):
                    self.event = self.get_player_event(1)
                    self.score += 50
                    self.score_count += 50

    #Передаем enum
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