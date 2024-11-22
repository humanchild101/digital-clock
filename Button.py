import pygame
pygame.init()
class Button:
    def __init__(self, window, x, y, width, height, border_color, text, text_color, command, bg_color=(0, 0, 0, 0)):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_color = border_color
        self.text = text
        self.text_color = text_color
        self.command = command
        self.bg_color = bg_color
    def draw(self):
        # font stuff for text
        font = pygame.font.Font(None, 30)
        words = font.render(self.text, False, self.text_color)
        # 1 rect. will be used to draw 2 rectangles --> 1 for border/one for fill if bg color provided
        button_rect = pygame.Rect((self.x, self.y, self.width, self.height))
        # if a bg color was provided then do both the border rect and the button rect. but if not, just teh border rectangle
        if self.bg_color != (0, 0, 0, 0):
            pygame.draw.rect(self.window, self.bg_color, button_rect, 0, 10)
            pygame.draw.rect(self.window, self.border_color, button_rect, 3, 10)
        else:
            pygame.draw.rect(self.window, self.border_color, button_rect, 3, 10)
        w, h = font.size(self.text)
        # words in the center of rect
        self.window.blit(words, (button_rect.centerx - w / 2, button_rect.centery - h / 2))
    def clicked(self, event):
        mouse_pos = pygame.mouse.get_pos()
        # if its clicked it should perform some function that is given as an argument
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.x + 10 <= mouse_pos[0] <= self.width + self.x + 10 and self.y + 10 <= mouse_pos[1] <= self.height + self.y + 10:
                self.command()
    def change_color(self, fill_color=(255, 255, 255), border=(0, 0, 0), text=(0, 0, 0)):
        self.bg_color = fill_color
        self.border_color = border
        self.text_color = text
