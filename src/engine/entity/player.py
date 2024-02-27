import config
from engine.board import cell
import pygame
from enum import Enum, auto
from engine import sprites
from engine import coords
from engine.entity import direction

#TODO: сделать ивент столкновения
    
class PlayerEventType(Enum):
    NoEvent = auto()
    FoodEvent = auto()
    EnemyAttack = auto()

class PlayerEvent:
    type_event: PlayerEventType
    context: dict
    
    def __init__(self, type_event, context = None):
        self.type_event = type_event
        self.context = context

class PlayerState(Enum):
    vulnerable = auto()
    invulnerable = auto()
    
class Player:
    
    speed = 2

    player_direction = direction.Direction.stay
    player_want_direction = direction.Direction.no_direction
    
    player_state = PlayerState.vulnerable
    
    event = PlayerEvent(type_event = PlayerEventType.NoEvent)
    
    helthpoints = 4

    total_score = 0
    curr_level_score = 0

    coords = coords.Coords()

    invulnerable_timer = 0
    ticks_for_animation = 0
    
    player_anim = sprites.Sprites.player_animation

    def __init__(self):
        self.screen_width = config.get_value('screen_width')
        self.screen_height = config.get_value('screen_height')
        self.cell_width = self.cell_height = self.screen_height/20
        self.rect = self.player_anim['stay'].get_rect()
    
    def set_spawn_coord(self, start_cell):
        self.rect.x, self.rect.y = self.coords.cells_to_pixels_xy(start_cell)
          
    def get_coord(self):
        return ((self.coords.pixels_to_cells_xy(self.rect.x, self.rect.y)))
    
    def draw(self, screen: pygame.surface.Surface):
        if self.player_direction == direction.Direction.stay:
            screen.blit(self.player_anim['stay'], (self.rect.x, self.rect.y))
        if self.player_direction == direction.Direction.right:
            screen.blit(self.player_anim['right'][self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
        if self.player_direction == direction.Direction.left:
            screen.blit(self.player_anim['left'][self.ticks_for_animation // 6], (self.rect.x, self.rect.y))        
        if self.player_direction == direction.Direction.down:        
            screen.blit(self.player_anim['down'][self.ticks_for_animation // 6], (self.rect.x, self.rect.y))    
        if self.player_direction == direction.Direction.up:
            screen.blit(self.player_anim['up'][self.ticks_for_animation // 6], (self.rect.x, self.rect.y))

    def calculate_ticks_for_animation(self):
        if self.ticks_for_animation >= 20:
            self.ticks_for_animation = 0
        else:    
            self.ticks_for_animation += 1

    def move(self, is_block_ahead):
        coord = self.get_coord()
        
        self.calculate_ticks_for_animation()

        x_start_cell = self.coords.get_x_in_cell(coord, self.rect.x)
        y_start_cell = self.coords.get_y_in_cell(coord, self.rect.y)

        is_block = is_block_ahead(self.get_coord(), self.player_direction)

        if x_start_cell == 0 and y_start_cell == 0 and self.player_direction != self.player_want_direction and self.player_want_direction != direction.Direction.no_direction and not is_block_ahead(self.get_coord(), self.player_want_direction):
            is_block=False
            self.player_direction = self.player_want_direction
            self.player_want_direction = direction.Direction.no_direction
    
        if self.player_direction == direction.Direction.stay:
            return

        if self.player_direction == direction.Direction.right:
            self.rect.x += self.speed
    
            if self.player_want_direction == direction.Direction.left:
                self.player_direction = self.player_want_direction
                self.player_want_direction = direction.Direction.no_direction
            
            if is_block:
                self.rect.x -= self.coords.get_x_in_cell(coord, self.rect.x)
                self.player_direction = direction.Direction.stay

        if self.player_direction == direction.Direction.left:
            self.rect.x -= self.speed
            
            if self.player_want_direction == direction.Direction.right:
                self.player_direction = self.player_want_direction
                self.player_want_direction = direction.Direction.no_direction
            
            if is_block and self.coords.get_x_in_cell(coord, self.rect.x) == 0:
                self.player_direction = direction.Direction.stay

        if self.player_direction == direction.Direction.down:
            self.rect.y += self.speed
    
            if self.player_want_direction == direction.Direction.up:
                self.player_direction = self.player_want_direction
                self.player_want_direction = direction.Direction.no_direction
            
            if  is_block:
                self.rect.y -= self.coords.get_y_in_cell(coord, self.rect.y)
                self.player_direction = direction.Direction.stay

        if self.player_direction == direction.Direction.up:
            self.rect.y -= self.speed

            if self.player_want_direction == direction.Direction.down:
                self.player_direction = self.player_want_direction
                self.player_want_direction = direction.Direction.no_direction
            
            if  is_block and self.coords.get_y_in_cell(coord, self.rect.y) == 0:
                self.player_direction = direction.Direction.stay

    def interact_cell(self, current_cell):
        x_in_cell, y_in_cell = self.coords.get_xy_in_cell(self.get_coord(), self.rect.x, self.rect.y)
        if isinstance(current_cell, cell.FoodCell):
            if self.player_direction == direction.Direction.right or self.player_direction == direction.Direction.left:
                if x_in_cell in range(0, 3):
                    self.event = self.get_player_event(1)
                    self.total_score += 50
                    self.curr_level_score += 50
            if self.player_direction == direction.Direction.up or self.player_direction == direction.Direction.down:
                if y_in_cell in range(0, 3):
                    self.event = self.get_player_event(1)
                    self.total_score += 50
                    self.curr_level_score += 50

    def interact_enemy(self, enemy_coords):
        enemy_x, enemy_y = enemy_coords
        if self.player_state == PlayerState.vulnerable and self.rect.x - enemy_x == 0 and self.rect.y - enemy_y == 0:
                print('attack!')
                self.helthpoints -= 1
                self.player_state = PlayerState.invulnerable
        if self.player_state == PlayerState.invulnerable:
            if self.invulnerable_timer == 160:
                self.invulnerable_timer = 0
                self.player_state = PlayerState.vulnerable
                print('one more time')
            else:
                self.invulnerable_timer += 1
            
        
    def get_player_event(self, event):
        events = {
            0: PlayerEventType.NoEvent,
            1: PlayerEventType.FoodEvent,
            2: PlayerEventType.EnemyAttack
        }
        return PlayerEvent(type_event=events[event], context={'coords': self.get_coord()})
    
    def clear_event(self):
        self.event = self.get_player_event(0)
        
    def change_direction(self, direction):
        self.player_want_direction = direction
    
    def get_current_direction(self):
        return self.player_direction.value
        
    def clear_curr_level_score(self):
        self.curr_level_score = 0