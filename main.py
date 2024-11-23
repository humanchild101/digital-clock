# bg color issue
# to do: the hover thing for button, list parameter in the dropdown (general not specifically for the thing) + dropdown, clock,
import pygame
from pygame import QUIT
import sys
import datetime
import pytz #timezone
from Button import *

pygame.init()

win = pygame.display.set_mode((1000, 1000), pygame.SRCALPHA)
pygame.display.set_caption("Time to get a clock")
bg_surf = pygame.Surface((1000,1000))


white = (240, 240, 240, 255)
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
i = 2  # for iterating through colors



# the default ig
bg_surf.fill(navy_blue)

curtz = None  # Tracks selected timezone (None for default)

# round button function. (Surface, x_pos, y_pos, width, height, border_color, text you want, text_color,
# button function, background color)


# use list to change colors in order

def bg_change_in_order():
    global i
    bg_surf.fill(colors[i])
    i = (i + 1) % len(colors)



# Update timezone
def default():
    global curtz
    curtz = None

def london():
    global curtz
    curtz = "Europe/London"

def india():
    global curtz
    curtz = "Asia/Kolkata"

# Display time
def display_time(timezone=None):
    if timezone:
        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz)
    else:
        now = datetime.datetime.now()

    current_time = now.strftime("%H:%M:%S")
    font = pygame.font.Font("fontss/Orbitron-VariableFont_wght.ttf", 60)
    time_text = font.render(current_time, True, white)
    w, h = font.size(current_time)

    win.blit(time_text, ((500 - w / 2, 500 - h / 2))) # Display time in the center

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Handle button clicks
        defa = Button(win, 815, 10, 175, 40, white, "Your Time", white, default, midnight_blue)
        lon = Button(win, 815, 60, 175, 40, white, "London Time", white, london, midnight_blue)
        ind = Button(win, 815, 110, 175, 40, white, "India Time", white, india, midnight_blue)

        button = Button(win, 10, 10, 175, 40, white, "Change Color", white, bg_change_in_order, midnight_blue)

        defa.clicked(event)
        lon.clicked(event)
        ind.clicked(event)

        button.clicked(event)

    # Draw background and buttons
    win.blit(bg_surf, (0, 0))
    defa.draw()
    lon.draw()
    ind.draw()
    button.draw()


    # Display the correct time
    if curtz:
        display_time(curtz)
    else:
        display_time()

    # Update display
    pygame.display.update()
