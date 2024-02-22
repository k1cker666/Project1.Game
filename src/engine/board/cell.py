from pygame import Surface 
from engine import sprites

class Cell():
    sprites = sprites.Image
        
    def __init__(self):
        pass
    
    def draw():
        pass
    
class EmptyCell(Cell):
    def __init__(self):
        self.image = self.sprites.empty_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))

class FoodCell(Cell):
    def __init__(self):
        self.image = self.sprites.food_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))
    
class BlockCell(Cell):
    def __init__(self):
        self.image = self.sprites.block_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))
        
class StartCell(Cell):
    def __init__(self):
        self.image = self.sprites.empty_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))
            
class CrossEmptyCell(Cell):
    def __init__(self):
        self.image = self.sprites.empty_cell
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))

class CrossFoodCell(Cell):
    def __init__(self):
        self.image = self.sprites.food_cell
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))
        
    
