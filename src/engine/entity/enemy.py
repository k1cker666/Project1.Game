import pygame
from engine import sprites
from engine import coords
from engine.entity import direction
from engine.entity import enemyname
from random import choice
#TODO: ограничить область передвижения

class Enemy:
    coords = coords.Coords()
    speed = 2
    enemy_direction = direction.Direction.no_direction
    enemy_past_direction = direction.Direction.no_direction
    ticks_for_animation = 0
    delay_timer = 0
    
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
        pos = (self.rect.x, self.rect.y)
        if self.name == enemyname.EnemyName.Blinky:
            self.draw_blinky(screen, pos)
        if self.name == enemyname.EnemyName.Clyde:
            self.draw_clyde(screen, pos)
        if self.name == enemyname.EnemyName.Inky:
            self.draw_inky(screen, pos)
        if self.name == enemyname.EnemyName.Pinky:
            self.draw_pinky(screen, pos)
            
    def draw_blinky(self, screen: pygame.surface.Surface, pos):
        blinky_anim = sprites.Sprites.enemies_animation['blinky']
        if self.enemy_direction == direction.Direction.no_direction or self.enemy_direction == direction.Direction.right:
            screen.blit(blinky_anim['right'][self.ticks_for_animation // 6], pos)
        if self.enemy_direction == direction.Direction.left:
            screen.blit(blinky_anim['left'][self.ticks_for_animation // 6], pos)        
        if self.enemy_direction == direction.Direction.down:        
            screen.blit(blinky_anim['down'][self.ticks_for_animation // 6], pos)    
        if self.enemy_direction == direction.Direction.up:
            screen.blit(blinky_anim['up'][self.ticks_for_animation // 6], pos)
    
    def draw_clyde(self, screen: pygame.surface.Surface, pos):
        clyde_anim = sprites.Sprites.enemies_animation['clyde']
        if self.enemy_direction == direction.Direction.no_direction or self.enemy_direction == direction.Direction.left:
            screen.blit(clyde_anim['left'][self.ticks_for_animation // 6], pos)
        if self.enemy_direction == direction.Direction.right:
            screen.blit(clyde_anim['right'][self.ticks_for_animation // 6], pos)      
        if self.enemy_direction == direction.Direction.down:        
            screen.blit(clyde_anim['down'][self.ticks_for_animation // 6], pos)    
        if self.enemy_direction == direction.Direction.up:
            screen.blit(clyde_anim['up'][self.ticks_for_animation // 6], pos)
    
    def draw_inky(self, screen: pygame.surface.Surface, pos):
        inky_anim = sprites.Sprites.enemies_animation['inky']
        if self.enemy_direction == direction.Direction.no_direction or self.enemy_direction == direction.Direction.right:
            screen.blit(inky_anim['right'][self.ticks_for_animation // 6], pos)
        if self.enemy_direction == direction.Direction.left:
            screen.blit(inky_anim['left'][self.ticks_for_animation // 6], pos)        
        if self.enemy_direction == direction.Direction.down:        
            screen.blit(inky_anim['down'][self.ticks_for_animation // 6], pos)    
        if self.enemy_direction == direction.Direction.up:
            screen.blit(inky_anim['up'][self.ticks_for_animation // 6], pos)
        
    def draw_pinky(self, screen: pygame.surface.Surface, pos):
        pinky_anim = sprites.Sprites.enemies_animation['pinky']
        if self.enemy_direction == direction.Direction.no_direction or self.enemy_direction == direction.Direction.left:
            screen.blit(pinky_anim['left'][self.ticks_for_animation // 6], pos)
        if self.enemy_direction == direction.Direction.right:
            screen.blit(pinky_anim['right'][self.ticks_for_animation // 6], pos)      
        if self.enemy_direction == direction.Direction.down:        
            screen.blit(pinky_anim['down'][self.ticks_for_animation // 6], pos)    
        if self.enemy_direction == direction.Direction.up:
            screen.blit(pinky_anim['up'][self.ticks_for_animation // 6], pos)
            
    def get_coord(self):
        return ((self.coords.pixels_to_cells_xy(self.rect.x, self.rect.y)))
    
    def move(self, is_block, free_diretnion):
        if self.delay_timer != 60:
            self.delay_timer += 1
        else:
            coords = self.get_coord()

            x_start_cell = self.coords.get_x_in_cell(coords, self.rect.x)
            y_start_cell = self.coords.get_y_in_cell(coords, self.rect.y)
            
            main_condirion = is_block(coords, self.enemy_direction) and x_start_cell == 0 and y_start_cell == 0

            if self.enemy_direction == direction.Direction.no_direction:
                self.enemy_direction = choice(free_diretnion(coords, self.enemy_past_direction))

            if self.addit_conditions() and x_start_cell == 0 and y_start_cell == 0:
                self.enemy_past_direction = self.enemy_direction
                self.enemy_direction = choice(free_diretnion(coords, self.enemy_past_direction))
            
            if main_condirion:
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

    def addit_conditions(self):
        coords = self.get_coord()
        if self.name == enemyname.EnemyName.Blinky:
            if self.enemy_direction == direction.Direction.right:
                if coords[0] >= 7:
                    return True
            if self.enemy_direction == direction.Direction.down:
                if coords[1] >= 7:
                    return True
        
        if self.name == enemyname.EnemyName.Clyde:
            if self.enemy_direction == direction.Direction.left:
                if coords[0] <= 7:
                    return True
            if self.enemy_direction == direction.Direction.down:
                if coords[1] >= 7:
                    return True
                
        if self.name == enemyname.EnemyName.Inky:
            if self.enemy_direction == direction.Direction.right:
                if coords[0] >= 7:
                    return True
            if self.enemy_direction == direction.Direction.up:
                if coords[1] <= 7:
                    return True
                
        if self.name == enemyname.EnemyName.Pinky:
            if self.enemy_direction == direction.Direction.left:
                if coords[0] <= 7:
                    return True
            if self.enemy_direction == direction.Direction.up:
                if coords[1] <= 7:
                    return True
        return False
        
    def clear_delay_timer(self):
        self.delay_timer = 0
        
    def get_xy_coord(self):
        return ((self.rect.x, self.rect.y))