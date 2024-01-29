import json
from engine.board import cell
import pygame

class Board:
    
    def load(file):
        file = str("././config/maps/"+file)
        file = open(file, 'r')
        game_map = json.loads(file.read())
        file.close
        px = 0
        py = 0
        for y in game_map:
            for x in y:
                if x == 0:
                    game_map[py][px] = BlockCell.color
                    px += 1
                elif x == 1:
                    game_map[py][px] = EmptyCell.color
                    px += 1
                elif x == 2:
                    game_map[py][px] = FoodCell.color
                    px += 1
                if px == 10:
                    px = 0
                    py += 1
        return game_map 
    
    def draw(screen, file):
        game_map = Board.load(file)
        cell_width = cell_height = 40
        start_x = 125
        start_y = 200
        for y in range(len(game_map)):
            for x in range(len(game_map[y])):
                px = x*cell_width+start_x
                py = y*cell_width+start_y
                pygame.draw.rect(screen, game_map[y][x], (px, py, cell_width, cell_height))
        pygame.display.flip()
        
class EmptyCell(cell.Cell):
    color = (255, 0, 0)
    def draw():
        pass

class FoodCell(cell.Cell):
    color = (0, 255, 0)
    def draw():
        pass
    
class BlockCell(cell.Cell):
    color = (0, 0, 255)
    def draw():
        pass