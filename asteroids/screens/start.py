import pygame

from asteroids.constants import FONT_PATH
from asteroids.screens.common import draw_text_box

FONT_SIZE = 30
FONT = pygame.freetype.Font(file=FONT_PATH, size=FONT_SIZE)


def draw_start_screen(screen: pygame.Surface):
    screen_text = [
        "Welcome to Asteroids!",
        "Kill as many as you can, as fast as you can!",
        "Before they kill you!",
        "Controls:",
        "A - turn left",
        "D - turn right",
        "S - move backward",
        "W - move forward",
        "Space - fire!",
        "P - pause game",
        "Q - quit",
        "Press ENTER to start playing",
    ]

    draw_text_box(screen, screen_text, FONT_SIZE, FONT)
