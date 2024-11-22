# to do: the hover thing for button, list parameter in the dropdown (general not specifically for the thing) + dropdown, clock,
import pygame
from pygame import QUIT
import sys
import datetime
from Button import *

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
i = 0  # for iterating through colors

# the default ig
win.fill(gray_blue)


# round button function. (Surface, x_pos, y_pos, width, height, border_color, text you want, text_color,
# button function, background color)

# change to desired color. not in actual program.
def manual_bg_change(color):
    win.fill(color)


# use list to change colors in order
def bg_change_in_order():
    global i
    win.fill(colors[i])
    i = (i + 1) % len(colors)


def changing_time():
    return


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        button = Button(win, 10, 10, 175, 40, white, "Change Color", white, bg_change_in_order, midnight_blue)
        button.draw()
        button.clicked(event)

    time = pygame.time.get_ticks()
    # ok so create a new surface for this. put the datetime.time thing on it and update it every 1000 ms (so every second).. easy enough i hope its actually this simple.

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    time_surface = pygame.Surface((200, 100), pygame.SRCALPHA)

    font1 = pygame.font.Font(None, 60)
    time_text = font1.render(current_time, True, colors[3])

    w, h = font1.size(current_time)

    for ms in range(0, time, 1000):
        time_text = font1.render(current_time, True, colors[3])
        time_surface.blit(time_text, (200 - w / 2, 100 - h / 2))
        win.blit(time_text, (400, 450))



    pygame.display.update()
