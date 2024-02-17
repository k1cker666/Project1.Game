import pygame
import config
from engine import image

class Cell(pygame.sprite.Sprite):
    images = image.Image
        
    def __init__(self):
        super().__init__()
    
    def draw():
        pass
    
class EmptyCell(Cell):
    def __init__(self):
        super().__init__()
        self.image = self.images.empty_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen, px, py):
        screen.blit(self.image, (px, py))

class FoodCell(Cell):
    def __init__(self):
        super().__init__()
        self.image = self.images.food_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen, px, py):
        screen.blit(self.image, (px, py))
    
class BlockCell(Cell):
    def __init__(self):
        super().__init__()
        self.image = self.images.block_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen, px, py):
        screen.blit(self.image, (px, py))
        
class StartCell(Cell):
    def __init__(self):
        super().__init__()
        self.image = self.images.empty_cell
        self.rect = self.image.get_rect()
        
    def draw(self, screen, px, py):
        screen.blit(self.image, (px, py))
