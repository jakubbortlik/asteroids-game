import pygame

from asteroids.constants import FONT_PATH
from asteroids.screens.common import draw_text_box

FONT_SIZE = 36
FONT = pygame.freetype.Font(file=FONT_PATH, size=FONT_SIZE)


def draw_game_over(screen: pygame.Surface, score: int):
    screen_text = [
        "Game over!",
        f"Your score was: {score}",
        "",
        "Enter - play again",
        "Q - quit",
    ]

    draw_text_box(screen, screen_text, FONT_SIZE, FONT)
