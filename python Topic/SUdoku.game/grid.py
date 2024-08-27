from random import sample
from select import Select
from copy import deepcopy

def create_line_coordinates(cell_size):
    coordinates = []
    for y in range(1, 9): 
        horizontal_line = [(0, y * cell_size), (cell_size * 9, y * cell_size)]
        coordinates.append(horizontal_line)
    for x in range(1, 9):  
        vertical_line = [(x * cell_size, 0), (x * cell_size, cell_size * 9)]
        coordinates.append(vertical_line)
    return coordinates

SUB_GRID_SIZE = 3
GRID_SIZE = SUB_GRID_SIZE * SUB_GRID_SIZE

def pattern(row_num, col_num):
    return (SUB_GRID_SIZE * (row_num % SUB_GRID_SIZE) + row_num // SUB_GRID_SIZE + col_num) % GRID_SIZE

def shuffle(samp: range):
    return sample(samp, len(samp))

def create_grid(sub_grid):
    """Creates the 9x9 grid filled with random numbers."""
    row_base = range(sub_grid)
    rows = [g * sub_grid + r for g in shuffle(row_base) for r in shuffle(row_base)]
    cols = [g * sub_grid + c for g in shuffle(row_base) for c in shuffle(row_base)]
    nums = shuffle(range(1, sub_grid * sub_grid + 1))
    return [[nums[pattern(r, c)] for c in cols] for r in rows]

class Grid:
    def __init__(self, font, pygame):
        self.cell_size = 67
        self.coordinates = create_line_coordinates(self.cell_size)
        self.font = font
        self.x_offset = 25
        self.y_offset = 10
        self.selection = Select(pygame, self.font)
        self.win = False
        self.restart()  # Initialize the grid and remove cells during initialization

    def getclick(self, x, y):
        if x <= 600:
            grid_x, grid_y = x // self.cell_size, y // self.cell_size
            if not self.is_cell_preoccupied(grid_x, grid_y):
                selected_num = self.selection.get_selected_number()
                if selected_num != 0:  # Only set the cell if a number is selected
                    self.set_cell(grid_x, grid_y, selected_num)
        else:
            self.selection.button_clicked(x, y)
        if self.check_grids():
            print('win')
            self.win = True

    def check_grids(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != self.testgrid[y][x]:
                    return False
        return True

    def restart(self):
        self.grid = create_grid(SUB_GRID_SIZE)
        self.testgrid = deepcopy(self.grid)
        self.remove()
        self.occupied = self.pre_occupied_cells()
        self.win = False
        self.selection.selnum = 0  # Reset the selected number

    def is_cell_preoccupied(self, x, y):
        return (y, x) in self.occupied

    def pre_occupied_cells(self):
        occupied_cell_coordinates = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x, y) != 0:
                    occupied_cell_coordinates.append((y, x))
        return occupied_cell_coordinates

    def draw_lines(self, pg, screen):
        for index, coordinates in enumerate(self.coordinates):
            if index in [2, 5, 10, 13]:
                pg.draw.line(screen, (255, 200, 0), coordinates[0], coordinates[1], 4)
            else:
                pg.draw.line(screen, (0, 200, 255), coordinates[0], coordinates[1], 1)

    def remove(self):
        num_of_cells = GRID_SIZE * GRID_SIZE
        empties = num_of_cells * 3 // 20
        for i in sample(range(num_of_cells), empties):
            self.grid[i // GRID_SIZE][i % GRID_SIZE] = 0

    def draw_numbers(self, screen):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x, y) != 0:
                    if (y, x) in self.occupied:
                        text_surface = self.font.render(str(self.get_cell(x, y)), False, (0, 200, 255))
                    else:
                        text_surface = self.font.render(str(self.get_cell(x, y)), False, (0, 255, 0))
                    if self.get_cell(x, y) != self.testgrid[y][x]:
                        text_surface = self.font.render(str(self.get_cell(x, y)), False, (255, 0, 0))
                    screen.blit(text_surface, (x * self.cell_size + self.x_offset, y * self.cell_size + self.y_offset))

    def show_select(self, py, screen):
        self.selection.draw(screen)

    def get_cell(self, x, y):
        return self.grid[y][x]

    def set_cell(self, x, y, value):
        self.grid[y][x] = value

