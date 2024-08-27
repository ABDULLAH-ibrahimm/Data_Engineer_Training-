# @grid.py>>> file 


##  1]  Imports and Constants
# sample: From the random module, used for shuffling lists.
# Select: A class from your code (presumably for selecting numbers).
# deepcopy: From the copy module, used to create deep copies of objects.

#create_line_coordinates: Generates coordinates for drawing lines in a grid based on cell_size.
# It creates horizontal and vertical lines to form the grid.

#SUB_GRID_SIZE: Size of a sub-grid (3 for a standard Sudoku).
# GRID_SIZE: Total size of the grid (9 for a standard Sudoku).


# pattern 
# Purpose: 
# Generates a pattern to place numbers in the grid ensuring that each number appears exactly once in each row, column, and sub-grid.
#Explanation:
# row_num % SUB_GRID_SIZE: Determines the row's position within its sub-grid.
# row_num // SUB_GRID_SIZE: Determines which sub-grid row the current row is in.


#shuffle(samp: range)
#Purpose: Randomly shuffles a sequence.
#Explanation:
#Uses random.sample to return a new list containing all elements from samp in a random order.

#create_grid(sub_grid)
 # Purpose: Generates a complete Sudoku grid with numbers filled in.
 #Explanation:
 #row_base = range(sub_grid): Creates a base range for sub-grids (0, 1, 2).
 #Shuffling Rows and Columns:
 #Shuffles the order of sub-grid rows and then shuffles rows within each sub-grid.
 #Similarly, shuffles the order of sub-grid columns and then columns within each sub-grid.
 # Shuffles the numbers 1 through 9.
 #Generating the Grid >>Uses the pattern function to fill in each cell based on the shuffled rows, columns, and numbers.
 


## 2] in class
#The Grid class manages the Sudoku grid and its interactions.

#method
# 1)__init__: 
# Initializes the grid with cell size, coordinates, font, and selection. Calls restart to set up the grid.

#  2)getclick: 
#  Handles mouse clicks. If the click is inside the grid, it sets a cell with the selected number.
#  If the click is outside the grid, it updates the selection. It also checks if the grid is correctly filled.
 
#  3)check_grids:
#  Checks if the current grid matches the solution grid (testgrid). Returns True if the grids match.

#  4)restart:
#  Creates a new grid, makes a copy for the solution, removes some cells to create a puzzle, and resets occupied cells and win status.

#  5)is_cell_preoccupied:
#  Checks if a cell is preoccupied (i.e., originally filled and not meant to be changed).

# 6)pre_occupied_cells: 
# Returns a list of coordinates for cells that are initially filled in the grid.
#print cell is not  empty 

# 7)draw_lines: 
# Draws the grid lines on the screen. Special lines are highlighted in yellow.

#8)remove(self)
#Purpose: Removes a certain number of cells from the filled grid to create the Sudoku puzzle by setting them to zero (representing empty cells)
#  after that i make it empty by making codition in draw num.
# Check if the cell is not empty:self.get_cell(x, y) != 0: If the cell has a number (not 0), proceed to render it.
#Blit the Text:
#screen.blit(text_screen, (x * self.cell_size + self.x_offset, y * self.cell_size + self.y_offset)):


#9)draw_numbers: 
# Renders numbers in the grid. Differentiates between occupied cells, correct cells, and incorrect cells using different colors.

#10)show_select: 
# Draws the selection interface on the screen.

#11)get_cell(self, x, y)
#Purpose: Retrieves the value of a specific cell in the grid.

# 12)set_cell(self, x, y, value)
#Purpose: Sets the value of a specific cell in the grid.



#----------------------------------------------------------------------------------
# on selet.py>>>>file   
#Overview
#The Select class is designed to handle the selection of buttons in a graphical user interface, using Pygame. Each button represents a number, and the class provides methods to draw these buttons, handle button clicks, and retrieve the currently selected number.

#Attributes
#pygame: This is the Pygame module used for rendering graphics and handling events.
#font: A Pygame font object used for rendering text on the buttons.
#btn_w and btn_h: Define the width and height of each button.
#selnum: Stores the number of the currently selected button (0 if no button is selected).
#color_selected and color_normal: Colors used to indicate the selected and normal states of the buttons.
#btn_positions: A list of tuples where each tuple represents the (x, y) position of a button on the screen.


#Methods
# 1) __init__
# Initializes the class with Pygame and font objects.
# Sets the width and height for buttons.
# Defines the colors for selected and normal button states.
# Defines button positions on the screen.

# 2) draw
#Draws each button on the screen:
# If the button is selected (i.e., its index matches selnum), it is drawn with the color_selected.
# If not selected, it is drawn with the color_normal.
# The number on the button is displayed using the font object, with its color depending on whether the button is selected.


# 3)button_clicked
# Checks if a button has been clicked based on the mouse coordinates (mouse_x, mouse_y).
# Updates selnum to the index of the clicked button (1-based index).

# 4)on_button 
# Determines if the mouse coordinates are within the bounds of a button.
# Returns True if the mouse click is inside the button's area.


# get_selected_number
# Returns the currently selected button number.



#------------------------------------------------------------------------------------------------------------------
#@game.py >>> file 
#1. Imports and Initializationpygame:
#  The Pygame library is imported to handle graphics, events, and user interaction.Grid:
#  Imports the Grid class from your grid.py file, which contains the logic for managing the Sudoku game.


#Pygame Setup
#pygame.init():
#Initializes all Pygame modules, such as graphics and sound
#pygame.font.init(): 
#Initializes the Pygame font module.
#fontgame and fontgame2:
#Create two font objects with different sizes for rendering text in the game.

# Create Grid Instance 
# Grid: Instantiates the Grid class with the font and Pygame module. 
# This initializes the Sudoku grid and related functionalities.

#Set Up Game Window
#pygame.display.set_mode((830, 605)): Creates a window with the specified width (830 pixels) and height (605 pixels).
#pygame.display.set_caption("Sudoku --> Hello my friend"): Sets the title of the game window.

#Game Loop
# running = True: 
# Sets a flag to control the game loop.
# while running:
#  Starts the main game loop.
# pygame.event.get(): 
# Retrieves a list of all the events (e.g., key presses, mouse clicks).
# if event.type == pygame.QUIT:: 
# Checks if the user has closed the window. If so, it sets running to False, which ends the loop and closes the game.
# if event.type == pygame.MOUSEBUTTONDOWN and not grid.win:: 
# Checks if a mouse button has been clicked and if the game is not won. It then retrieves the mouse position and processes it with grid.getclick().
# if event.type == pygame.KEYDOWN:: 
# Checks if a key is pressed. If the spacebar (pygame.K_SPACE) is pressed and the game is won, it calls grid.restart() to reset the game.


#Draw Game Elements
#screen.fill((0, 0, 0)): Fills the screen with black color. This clears the screen before drawing new content.
#grid.draw_lines(pygame, screen): 
# Draws the grid lines on the screen.
#grid.draw_numbers(screen): 
# Renders the numbers on the grid.
#grid.show_select(pygame, screen): 
# Draws the selection interface (number buttons).


#Display Win Message
#if grid.win:: Checks if the player has won.
#won_surface = fontgame.render("You Won!", False, (0, 255, 0)): 
# Renders the "You Won!" message in green.
#screen.blit(won_surface, (650, 450)): 
# Draws the "You Won!" message on the screen.
#return_message = fontgame2.render("Press space to restart!", False, (0, 255, 200)): 
# Renders the restart message in light orange.
#screen.blit(return_message, (620, 500)):
#Draws the restart message on the screen.


#Update Display
#pygame.display.flip(): Updates the entire screen with the drawn content.