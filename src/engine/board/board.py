import json
from engine.board import cell
from engine import coords

class Board:
    game_map: list
    coords = coords.Coords()
    
    def __init__(self, level_name):
        file_path = str("././config/maps/"+level_name)
        file_map = open(file_path, 'r')
        game_map_json = json.loads(file_map.read())
        file_map.close()
        self.game_map = game_map_json.copy()
        self.load()
        
    def load(self):
        px = 0
        py = 0
        for line in self.game_map:
            for item in line:
                if item == 0:
                    self.game_map[py][px] = cell.BlockCell()
                    px += 1
                elif item == 1:
                    self.game_map[py][px] = cell.EmptyCell()
                    px += 1
                elif item == 2:
                    self.game_map[py][px] = cell.FoodCell()
                    px += 1
                elif item == 3:
                    self.game_map[py][px] = cell.StartCell()
                    px += 1
                if px == len(self.game_map[0]):
                    px = 0
                    py += 1
                    
    def draw(self, screen):
        for y, line in enumerate(self.game_map):
            py = self.coords.cells_to_pixels_y(y)
            for x, item in enumerate(line):
                px = self.coords.cells_to_pixels_x(x)
                item.draw(screen, px, py)
        
    def find_start_cell(self):
        for py in range(len(self.game_map)):
            for px in range(len(self.game_map[py])):
                if isinstance(self.game_map[py][px], cell.StartCell):
                    return (px, py)
    
    def get_cell(self, coords):
        return self.game_map[coords[1]][coords[0]]
    
    def set_empty_cell(self, coords):
        self.game_map[coords[1]][coords[0]] = cell.EmptyCell()
        
    def check_food_cells(self):
        for line in self.game_map:
            for item in line:
                if isinstance(item, cell.FoodCell):
                    return False
        return True
    
    def admin_clear_food_cells(self):
        py = 0
        px = 0
        for line in self.game_map:
            for item in line:
                if isinstance(item, cell.FoodCell):
                    self.game_map[py][px] = cell.EmptyCell()
                px += 1
            py +=1
            px = 0