# bg color issue
# to do: the hover thing for button, list parameter in the dropdown (general not specifically for the thing) + dropdown, clock,
import pygame
from pygame import QUIT
import sys

# import time

pygame.init()

win = pygame.display.set_mode((1000, 1000), pygame.SRCALPHA)
pygame.display.set_caption("Time to get a clock")

white = (255, 255, 255, 255)
gray_blue = (106, 129, 166, 255)
navy_blue = (38, 66, 110, 255)
midnight_purple = (37, 29, 112, 255)
midnight_blue = (2, 15, 36, 255)
wisteria = (135, 107, 219, 255)
flowers = (219, 107, 189, 255)
red = (255, 59, 75, 255)
lava = (245, 67, 22, 255)
lemonade = (240, 222, 144, 255)
olive = (121, 138, 83, 255)
sea_glass = (143, 227, 182, 255)

colors = [white, gray_blue, navy_blue, midnight_purple, wisteria, flowers, red, lava, lemonade, olive, sea_glass]
i = 0 #for iterating through colors

# the default ig
win.fill(gray_blue)


# round button function. (Surface, x_pos, y_pos, width, height, border_color, text you want, text_color,
# button function, background color)
def round_button(window, x, y, width, height, border_color, text, text_color, command, bg_color=(0, 0, 0, 0)):
    mouse_pos = pygame.mouse.get_pos()

    # font stuff for text
    font = pygame.font.Font(None, 30)
    words = font.render(text, False, text_color)

    # 1 rect. will be used to draw 2 rectangles --> 1 for border/one for fill if bg color provided
    button_rect = pygame.Rect((x, y, width, height))

    #if a bg color was provided then do both the border rect and the button rect. but if not, just teh border rectangle
    if bg_color != (0, 0, 0, 0):
        pygame.draw.rect(window, bg_color, button_rect, 0, 10)
        pygame.draw.rect(window, border_color, button_rect, 3, 10)
    else:
        pygame.draw.rect(window, border_color, button_rect, 3, 10)

    w, h = font.size(text)

    #words in the center of rect
    window.blit(words, (button_rect.centerx - w / 2, button_rect.centery - h / 2))

    #if its clicked it should perform some function that is given as an argument
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x + 10 <= mouse_pos[0] <= width + x + 10 and y + 10 <= mouse_pos[1] <= height + y + 10:
            command()
            pygame.display.update()


#change to desired color. not in actual program.
def manual_bg_change(color):
    win.fill(color)

def bg_change_in_order():
    global i
    win.fill(colors[i])
    i = (i+1) % len(colors)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    round_button(win, 10, 10, 175, 40, white, "Change Color", white, bg_change_in_order, midnight_blue)

    pygame.display.update()
