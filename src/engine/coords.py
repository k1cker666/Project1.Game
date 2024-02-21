class Coords:
    cells: int
    pixels: int
    screen_width = 650
    screen_height = 800
    cell_width = cell_height = screen_height/20
    start_board_x = screen_width/2 - cell_width*15/2
    start_board_y = screen_height/2 - cell_height*15/2 + 3*screen_height/32
    
    def pixels_to_cells_xy(self, pixel_x, pixel_y):
        px = (pixel_x - self.start_board_x)//self.cell_width
        py = (pixel_y - self.start_board_y)//self.cell_height
        return int(px), int(py)
        
    def pixels_to_cells_x(self, pixel_x):
        px = (pixel_x - self.start_board_x)//self.cell_width
        return px
    
    def pixels_to_cells_y(self, pixel_y):
        py = (pixel_y - self.start_board_y)//self.cell_height
        return py
      
    def cells_to_pixels_xy(self, coords):
        pixel_x = self.start_board_x+self.cell_width*coords[0]
        pixel_y = self.start_board_y+self.cell_height*coords[1]
        return pixel_x, pixel_y
    
    def cells_to_pixels_x(self, px):
        pixel_x = self.start_board_x+self.cell_width*px
        return pixel_x
    
    def cells_to_pixels_y(self, py):
        pixel_y = self.start_board_y+self.cell_height*py
        return pixel_y
    
    def get_xy_in_cell(self, coords: tuple, x, y):
        x_in_cell = int(x - self.start_board_x - coords[0]*self.cell_width)
        y_in_cell = int(y - self.start_board_y - coords[1]*self.cell_height)
        return x_in_cell, y_in_cell
    
    def get_x_in_cell(self, coords: tuple, x):
        x_in_cell = int(x - self.start_board_x - coords[0]*self.cell_width)
        return x_in_cell
    
    def get_y_in_cell(self, coords: tuple, y):
        y_in_cell = int(y - self.start_board_y - coords[1]*self.cell_height)
        return y_in_cell