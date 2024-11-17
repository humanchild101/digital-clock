#red button not showing up
import pygame
from pygame import QUIT
import sys

# import time

pygame.init()

win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Time to get a clock")

white = (255, 255, 255)
gray_blue = (106, 129, 166)
navy_blue = (38, 66, 110)
midnight_purple = (37, 29, 112)
wisteria = (135, 107, 219)
flowers = (219, 107, 189)
red = (255, 59, 75)
lava = (245, 67, 22)
lemonade = (240, 222, 144)
olive = (121, 138, 83)
sea_glass = (143, 227, 182)

colors = [white, gray_blue, navy_blue, midnight_purple, wisteria, flowers, red, lava, lemonade, olive, sea_glass]

# the default ig
win.fill(gray_blue)


# round_button function (x position, y position, width, height, border color, text, text_color, what function to do
# when clicked, bg color)
def round_button(x, y, width, height, border_color, text, text_color, command, bg_color=(0, 0, 0, 0)):
    mouse_pos = pygame.mouse.get_pos()

    # font stuff for text
    font = pygame.font.Font(None, 30)
    words = font.render(text, False, text_color)

    # sets a surface for the button along with a rectangle for the button. surface is there in case you want a bg color
    button_surface = pygame.Surface((width + 10, height + 10), pygame.SRCALPHA)
    button_rect = pygame.Rect((x, y, width, height))
    border_rect = pygame.Rect(x, y, width, height)

    # get the dimensions of the width/height used by the text
    w, h = font.size(text)

    pygame.draw.rect(button_surface, bg_color, border_rect, 0, 10)
    pygame.draw.rect(button_surface, border_color, button_rect, 5, 10)
    button_surface.blit(words, (button_rect.centerx - w / 2, button_rect.centery - h / 2))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x + 10 <= mouse_pos[0] <= width + x + 10 and y + 10 <= mouse_pos[1] <= height + y + 10:
            command()
            pygame.display.update()

    return button_surface


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

    drop = round_button(10, 10, 175, 40, white, "Colors", white, happy)
    red1 = round_button(10, 60, 175, 40, white, "White", white, lambda: bg_change(red), red)

    win.blit(drop, (10, 10))
    win.blit(red1, (10, 50))

    pygame.display.update()
