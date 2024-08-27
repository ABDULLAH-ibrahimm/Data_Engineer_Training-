import pygame
from grid import Grid

# Initialize Pygame
pygame.init()

# Initialize the font
pygame.font.init()
fontgame = pygame.font.SysFont('Comic Sans MS', 30)
fontgame2 = pygame.font.SysFont('Comic Sans MS', 18)

# Instantiate the Grid object
grid = Grid(fontgame, pygame)

# Set up the game window
screen = pygame.display.set_mode((830, 605))
pygame.display.set_caption("Sudoku        -->  Hello my friend")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.win:
            if pygame.mouse.get_pressed()[0]:  # Check for the left mouse button
                pos = pygame.mouse.get_pos()
                grid.getclick(pos[0], pos[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.win:
                grid.restart()  # Reset the grid when the spacebar is pressed

    # Fill the screen with a color (optional)
    screen.fill((0, 0, 0))

    # Draw the grid
    grid.draw_lines(pygame, screen)
    grid.draw_numbers(screen)
    grid.show_select(pygame, screen)

    # Display a win message if the player has won
    if grid.win:
        won_surface = fontgame.render("You Won!", False, (0, 255, 0))
        screen.blit(won_surface, (650, 450))
        return_message = fontgame2.render("Press space to restart!", False, (0, 255, 200))
        screen.blit(return_message, (620, 500))

    # Update the display
    pygame.display.flip()
