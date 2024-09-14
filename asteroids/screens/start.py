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

START_FONT_SIZE = 30
START_FONT = pygame.freetype.Font(file=FONT_PATH, size=START_FONT_SIZE)
START_BOX_BORDER_WIDTH = 2
START_BOX_PADDING = 20


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
        "Press ENTER to start playing"
    ]

    line_height = START_FONT_SIZE * 1.5
    total_text_height = line_height * len(screen_text)
    free_screen_height = SCREEN_HEIGHT - total_text_height - 100
    start_y = free_screen_height / 2

    text_widths = get_text_widths(screen_text, START_FONT)
    max_text_width = max(text_widths) + START_BOX_PADDING * 2

    game_over_box_rect = (
        (SCREEN_WIDTH - max_text_width) // 2,
        (free_screen_height + START_BOX_PADDING * 2) // 2,
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
        width=START_BOX_BORDER_WIDTH,
    )

    for i, (text, text_width) in enumerate(zip(screen_text, text_widths), start=1):
        x = (SCREEN_WIDTH - text_width) // 2
        START_FONT.render_to(
            surf=screen,
            dest=(x, start_y + i * line_height),
            text=text,
            fgcolor=WHITE,
        )
    pygame.display.flip()
