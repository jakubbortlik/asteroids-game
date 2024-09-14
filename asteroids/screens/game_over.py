import pygame

from asteroids.constants import FONT_PATH
from asteroids.screens.common import get_text_widths

from asteroids.constants import (
    BLACK,
    GRAY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WHITE,
)

GAME_OVER_FONT_SIZE = 36
GAME_OVER_FONT = pygame.freetype.Font(file=FONT_PATH, size=GAME_OVER_FONT_SIZE)
GAME_OVER_BOX_BORDER_WIDTH = 2
GAME_OVER_BOX_PADDING = 20


def draw_game_over(screen: pygame.Surface, score: int):
    screen_text = [
        "Game over!",
        f"Your score was: {score}",
    ]

    line_height = GAME_OVER_FONT_SIZE * 1.5
    total_text_height = line_height * len(screen_text)
    free_screen_height = SCREEN_HEIGHT - total_text_height - 100
    start_y = free_screen_height / 2

    text_widths = get_text_widths(screen_text, GAME_OVER_FONT)
    max_text_width = max(text_widths) + GAME_OVER_BOX_PADDING * 2

    game_over_box_rect = (
        (SCREEN_WIDTH - max_text_width) // 2,
        (free_screen_height + GAME_OVER_BOX_PADDING * 2) // 2,
        max_text_width,
        total_text_height + line_height,
    )

    # Cover objects on screen with BG color
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        rect=game_over_box_rect,
        width=0,
    )

    pygame.draw.rect(
        surface=screen,
        color=GRAY,
        rect=game_over_box_rect,
        width=GAME_OVER_BOX_BORDER_WIDTH,
    )

    for i, (text, text_width) in enumerate(zip(screen_text, text_widths), start=1):
        x = (SCREEN_WIDTH - text_width) // 2
        GAME_OVER_FONT.render_to(
            surf=screen,
            dest=(x, start_y + i * line_height),
            text=text,
            fgcolor=WHITE,
        )
