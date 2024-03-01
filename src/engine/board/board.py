import json
from engine.board import cell
from engine import coords
from engine.entity import direction
from engine.entity import area

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
                elif item == 4:
                    self.game_map[py][px] = cell.EnemyStartCell()
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
        
    def get_player_start_cell(self):
        for py in range(len(self.game_map)):
            for px in range(len(self.game_map[py])):
                if isinstance(self.game_map[py][px], cell.StartCell):
                    return ((px, py))
    
    def get_cell(self, coords):
        return self.game_map[coords[1]][coords[0]]
    
    def set_empty_cell(self, coords):
        if isinstance(self.game_map[coords[1]][coords[0]], cell.FoodCell):
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

    def is_block_ahead(self):
        def check(coords, curr_direction):
            x, y = coords[0], coords[1]
            if curr_direction == direction.Direction.right:
                return isinstance(self.game_map[y][x+1], cell.BlockCell)
            elif curr_direction == direction.Direction.left:
                return isinstance(self.game_map[y][x-1], cell.BlockCell)
            elif curr_direction == direction.Direction.down:
                return isinstance(self.game_map[y+1][x], cell.BlockCell)
            elif curr_direction == direction.Direction.up:
                return isinstance(self.game_map[y-1][x], cell.BlockCell)
            else:
                return False

        return lambda coords, curr_direction: check(coords, curr_direction)
    
    def get_enemy_start_cell(self, e_area):
        if e_area == area.Area.areaA:
            for py in range(0, 8):
                for px in range(0, 8):
                    if isinstance(self.game_map[py][px], cell.EnemyStartCell):
                        return ((px, py))
        if e_area == area.Area.areaB:
            for py in range(0, 8):
                for px in range(8, 15):
                    if isinstance(self.game_map[py][px], cell.EnemyStartCell):
                        return ((px, py))
        if e_area == area.Area.areaC:
            for py in range(7, 15):
                for px in range(0, 8):
                    if isinstance(self.game_map[py][px], cell.EnemyStartCell):
                        return ((px, py))
        if e_area == area.Area.areaD:
            for py in range(7, 15):
                for px in range(7, 15):
                    if isinstance(self.game_map[py][px], cell.EnemyStartCell):
                        return ((px, py))
                    
    def get_free_direction(self):
        def check(coords, past_direction):
            directions = []
            x, y = coords[0], coords[1]
                
            if past_direction == direction.Direction.right or past_direction == direction.Direction.left or past_direction == direction.Direction.no_direction:
                if not isinstance(self.game_map[y-1][x], cell.BlockCell):
                    directions.append(direction.Direction.up)
                if not isinstance(self.game_map[y+1][x], cell.BlockCell):
                    directions.append(direction.Direction.down)
                if len(directions) == 0:
                    if past_direction == direction.Direction.right:
                        return ([direction.Direction.left])
                    else:
                        return ([direction.Direction.right])
                 
            if past_direction == direction.Direction.down or past_direction == direction.Direction.up or past_direction == direction.Direction.no_direction:
                if not isinstance(self.game_map[y][x+1], cell.BlockCell):
                    directions.append(direction.Direction.right)
                if not isinstance(self.game_map[y][x-1], cell.BlockCell):
                    directions.append(direction.Direction.left)
                if len(directions) == 0:
                    if past_direction == direction.Direction.down:
                        return ([direction.Direction.up])
                    else:
                        return ([direction.Direction.down])

            return directions

        return lambda coords, past_direction: check(coords, past_direction)
    
    def is_own_area(self):
        def check(coords, curr_direction, e_area):
            x = coords[0]
            y = coords[1]
        
            if curr_direction == direction.Direction.right:
                return not self.coords.get_area_from_coords(x+1, y) == e_area
        
            elif curr_direction == direction.Direction.left:
                return not self.coords.get_area_from_coords(x-1, y) == e_area
        
            elif curr_direction == direction.Direction.down:
                return not self.coords.get_area_from_coords(x, y+1) == e_area
            
            elif curr_direction == direction.Direction.up:
                return not self.coords.get_area_from_coords(x, y-1) == e_area

        return lambda coords, curr_direction, e_area: check(coords, curr_direction, e_area)