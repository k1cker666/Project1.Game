import pygame
from engine import sprites
from engine import coords
from engine.entity import direction
from engine.entity import enemyname
from random import choice

class Enemy:
    coords = coords.Coords()
    speed = 2
    enemy_direction = direction.Direction.no_direction
    enemy_past_direction = direction.Direction.no_direction
    ticks_for_animation = 0
    
    def __init__(self, name):
        self.name = name
    
    def set_spawn_coord(self, start_cell):
        self.rect.x, self.rect.y = self.coords.cells_to_pixels_xy(start_cell)
        
    def create_unit(self):
        if self.name == enemyname.EnemyName.Blinky:
            self.image = sprites.Sprites.blinky_right_1
            self.rect = self.image.get_rect()
        if self.name == enemyname.EnemyName.Clyde:
            self.image = sprites.Sprites.clyde_left_1
            self.rect = self.image.get_rect()
        if self.name == enemyname.EnemyName.Inky:
            self.image = sprites.Sprites.inky_right_1
            self.rect = self.image.get_rect()
        if self.name == enemyname.EnemyName.Pinky:
            self.image = sprites.Sprites.pinky_left_1
            self.rect = self.image.get_rect()
            
    def calculate_ticks_for_animation(self):
        if self.ticks_for_animation >= 11:
            self.ticks_for_animation = 0
        else:    
            self.ticks_for_animation += 1
    
    def draw(self, screen: pygame.surface.Surface):
        self.calculate_ticks_for_animation()
        
        if self.name == enemyname.EnemyName.Blinky:
            if self.enemy_direction == direction.Direction.no_direction or self.enemy_direction == direction.Direction.right:
                screen.blit(sprites.Sprites.blinky_move_right[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
            if self.enemy_direction == direction.Direction.left:
                screen.blit(sprites.Sprites.blinky_move_left[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))        
            if self.enemy_direction == direction.Direction.down:        
                screen.blit(sprites.Sprites.blinky_move_down[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))    
            if self.enemy_direction == direction.Direction.up:
                screen.blit(sprites.Sprites.blinky_move_up[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
        
        if self.name == enemyname.EnemyName.Clyde:
            if self.enemy_direction == direction.Direction.no_direction or self.enemy_direction == direction.Direction.left:
                screen.blit(sprites.Sprites.clyde_move_left[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
            if self.enemy_direction == direction.Direction.right:
                screen.blit(sprites.Sprites.clyde_move_right[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))      
            if self.enemy_direction == direction.Direction.down:        
                screen.blit(sprites.Sprites.clyde_move_down[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))    
            if self.enemy_direction == direction.Direction.up:
                screen.blit(sprites.Sprites.clyde_move_up[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
        
        if self.name == enemyname.EnemyName.Inky:
            if self.enemy_direction == direction.Direction.no_direction or self.enemy_direction == direction.Direction.right:
                screen.blit(sprites.Sprites.inky_move_right[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
            if self.enemy_direction == direction.Direction.left:
                screen.blit(sprites.Sprites.inky_move_left[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))        
            if self.enemy_direction == direction.Direction.down:        
                screen.blit(sprites.Sprites.inky_move_down[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))    
            if self.enemy_direction == direction.Direction.up:
                screen.blit(sprites.Sprites.inky_move_up[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
        
        if self.name == enemyname.EnemyName.Pinky:
            if self.enemy_direction == direction.Direction.no_direction or self.enemy_direction == direction.Direction.left:
                screen.blit(sprites.Sprites.pinky_move_left[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
            if self.enemy_direction == direction.Direction.right:
                screen.blit(sprites.Sprites.pinky_move_right[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))      
            if self.enemy_direction == direction.Direction.down:        
                screen.blit(sprites.Sprites.pinky_move_down[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))    
            if self.enemy_direction == direction.Direction.up:
                screen.blit(sprites.Sprites.pinky_move_up[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
            
    def get_coord(self):
        return ((self.coords.pixels_to_cells_xy(self.rect.x, self.rect.y)))
    
    def move(self, is_block, free_diretnion):
        coords = self.get_coord()
        
        x_start_cell = self.coords.get_x_in_cell(coords, self.rect.x)
        y_start_cell = self.coords.get_y_in_cell(coords, self.rect.y)
        
        if self.enemy_direction == direction.Direction.no_direction:
            self.enemy_direction = choice(free_diretnion(coords, self.enemy_past_direction))
                
        if is_block(coords, self.enemy_direction) and x_start_cell == 0 and y_start_cell == 0:
            self.enemy_past_direction = self.enemy_direction
            self.enemy_direction = choice(free_diretnion(coords, self.enemy_past_direction))
            
        if self.enemy_direction == direction.Direction.right:
            self.rect.x += self.speed

        if self.enemy_direction == direction.Direction.left:
            self.rect.x -= self.speed

        if self.enemy_direction == direction.Direction.down:
            self.rect.y += self.speed

        if self.enemy_direction == direction.Direction.up:
            self.rect.y -= self.speed
            