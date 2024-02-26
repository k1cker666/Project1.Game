from pygame import Surface 
from engine import sprites

class Cell():
        
    def __init__(self):
        pass
    
    def draw():
        pass
    
class EmptyCell(Cell):
    def __init__(self):
        self.image = sprites.Sprites.empty_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))

class FoodCell(Cell):
    def __init__(self):
        self.image = sprites.Sprites.food_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))
    
class BlockCell(Cell):
    def __init__(self):
        self.image = sprites.Sprites.block_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))
        
class StartCell(Cell):
    def __init__(self):
        self.image = sprites.Sprites.empty_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))
        
class EnemyStartCell(Cell):
    def __init__(self):
        self.image = sprites.Sprites.empty_cell
        self.rect = self.image.get_rect()
    
    def draw(self, screen: Surface, px, py):
        screen.blit(self.image, (px, py))