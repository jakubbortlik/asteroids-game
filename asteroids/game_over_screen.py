import pygame

from asteroids.constants import (
    BLACK,
    GAME_OVER_BOX_BORDER_WIDTH,
    GAME_OVER_BOX_PADDING,
    GAME_OVER_FONT,
    GAME_OVER_FONT_SIZE,
    GRAY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    WHITE,
)


def get_text_widths(texts: list[str]) -> list[int]:
    text_widths = [GAME_OVER_FONT.get_rect(line)[2] for line in texts]
    return text_widths


def draw_game_over(screen: pygame.Surface, score: int):
    screen_text = [
        "Game over!",
        f"Your score was: {score}",
    ]

    line_height = GAME_OVER_FONT_SIZE * 1.5
    total_text_height = line_height * len(screen_text)
    start_y = (SCREEN_HEIGHT - total_text_height) / 2

    text_widths = get_text_widths(screen_text)
    max_text_width = max(text_widths) + GAME_OVER_BOX_PADDING * 2

    game_over_box_rect = (
        (SCREEN_WIDTH - max_text_width) // 2,
        (SCREEN_HEIGHT - total_text_height + GAME_OVER_BOX_PADDING * 2) // 2,
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
