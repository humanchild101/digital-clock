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
wisteria = (135, 107, 219, 255)
flowers = (219, 107, 189, 255)
red = (255, 59, 75, 255)
lava = (245, 67, 22, 255)
lemonade = (240, 222, 144, 255)
olive = (121, 138, 83, 255)
sea_glass = (143, 227, 182, 255)

colors = [white, gray_blue, navy_blue, midnight_purple, wisteria, flowers, red, lava, lemonade, olive, sea_glass]

# the default ig
win.fill(gray_blue)


# round button function. (Surface, x_pos, y_pos, width, height, border_color, text you want, text_color,
# button function, background color)
def round_button(window, x, y, width, height, border_color, text, text_color, command, bg_color=(0, 0, 0, 255)):
    mouse_pos = pygame.mouse.get_pos()

    # font stuff for text
    font = pygame.font.Font(None, 30)
    words = font.render(text, False, text_color)

    # two rectangles. 1 for the button and 1 for the border
    button_rect = pygame.Rect((x, y, width, height))
    border_rect = pygame.Rect(x, y, width, height)

    w, h = font.size(text)

    pygame.draw.rect(window, bg_color, border_rect, 0, 10)
    pygame.draw.rect(window, border_color, button_rect, 5, 10)

    window.blit(words, (button_rect.centerx - w / 2, button_rect.centery - h / 2))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x + 10 <= mouse_pos[0] <= width + x + 10 and y + 10 <= mouse_pos[1] <= height + y + 10:
            command()
            pygame.display.update()


def bg_change(color):
    win.fill(color)


"""
def color_drop():
    round_button(10,50,175, 40, white, "White", white, lambda: bg_change(white))
"""


def happy():
    win.fill(navy_blue)


dropdown = pygame.Rect((10, 10, 200, 50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    round_button(win, 10, 10, 175, 40, white, "Colors", white, happy)
    round_button(win, 10, 60, 175, 40, white, "White", white, lambda: bg_change(red), red)

    pygame.display.update()
