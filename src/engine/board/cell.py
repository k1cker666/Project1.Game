import pygame
from engine import sprites

class Cell(): #pygame.sprite.Sprite 
    sprites = sprites.Image
        
    def __init__(self):
        super().__init__()
    
    def draw():
        pass
    
class EmptyCell(Cell):
    def __init__(self):
        super().__init__()
        self.image = self.sprites.empty_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen, px, py):
        screen.blit(self.image, (px, py))

class FoodCell(Cell):
    def __init__(self):
        super().__init__()
        self.image = self.sprites.food_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen, px, py):
        screen.blit(self.image, (px, py))
    
class BlockCell(Cell):
    def __init__(self):
        super().__init__()
        self.image = self.sprites.block_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen, px, py):
        screen.blit(self.image, (px, py))
        
class StartCell(Cell):
    def __init__(self):
        super().__init__()
        self.image = self.sprites.empty_cell
        self.rect = self.image.get_rect()
        
    def draw(self, screen, px, py):
        screen.blit(self.image, (px, py))
