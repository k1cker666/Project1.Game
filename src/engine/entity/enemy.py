import pygame
from engine import sprites
from engine import coords
from engine.entity import direction
from engine.entity import enemyname

class Enemy:
    coords = coords.Coords()
    speed = 2
    enemy_direction = direction.Direction.no_direction
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
            screen.blit(sprites.Sprites.blinky_move_right[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
        if self.name == enemyname.EnemyName.Clyde:
            screen.blit(sprites.Sprites.clyde_move_left[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
        if self.name == enemyname.EnemyName.Inky:
            screen.blit(sprites.Sprites.inky_move_right[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))
        if self.name == enemyname.EnemyName.Pinky:
            screen.blit(sprites.Sprites.pinky_move_left[self.ticks_for_animation // 6], (self.rect.x, self.rect.y))