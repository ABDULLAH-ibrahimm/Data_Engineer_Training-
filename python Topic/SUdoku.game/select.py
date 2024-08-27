# select.py

class Select:
    def __init__(self, pygame, font):
        self.pygame = pygame
        self.btn_w = 60  # button width
        self.btn_h = 65  # button height
        self.font = font
        self.selnum = 0 
        self.color_selected = (0, 255, 0)
        self.color_normal = (200, 200, 200)
        self.btn_positions = [
            (650, 20), (740, 20),
            (650, 105), (740, 105),
            (650, 190), (740, 190),
            (650, 275), (740, 275),
            (740, 360)
        ]
        
    def draw(self, screen):
        for index, pos in enumerate(self.btn_positions):
            if self.selnum == index + 1:
                self.pygame.draw.rect(screen, self.color_selected, [pos[0], pos[1], self.btn_w, self.btn_h], width=3, border_radius=10)
                text_surface = self.font.render(str(index + 1), False, (0, 255, 0))
            else:
                self.pygame.draw.rect(screen, self.color_normal, [pos[0], pos[1], self.btn_w, self.btn_h], width=3, border_radius=10)
                text_surface = self.font.render(str(index + 1), False, (255, 255, 255))  # Render with white color

            screen.blit(text_surface, (pos[0] + 20, pos[1]+7))
        
    def button_clicked(self, mouse_x, mouse_y):
        for index, pos in enumerate(self.btn_positions):
            if self.on_button(mouse_x, mouse_y, pos):
                self.selnum = index + 1  # Update selnum to the selected button's index
                
    def button_hover(self, pos):
        mouse_pos = self.pygame.mouse.get_pos()  # Call the function to get the mouse position
        if self.on_button(mouse_pos[0], mouse_pos[1], pos):
            return True
        return False
        
    def on_button(self, mouse_x, mouse_y, pos):
        return pos[0] < mouse_x < pos[0] + self.btn_w and pos[1] < mouse_y < pos[1] + self.btn_h

    def get_selected_number(self):
        return self.selnum