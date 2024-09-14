import pygame

from asteroids.constants import (
    BLACK,
    GRAY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TEXT_BOX_BORDER_WIDTH,
    TEXT_BOX_PADDING,
    WHITE,
)


def get_text_widths(texts: list[str], font) -> list[int]:
    text_widths = [font.get_rect(line)[2] for line in texts]
    return text_widths


def draw_text_box(screen, screen_text, font_size, font):
    line_height = font_size * 1.5
    total_text_height = line_height * len(screen_text)
    free_screen_height = SCREEN_HEIGHT - total_text_height - 100
    start_y = free_screen_height / 2

    text_widths = get_text_widths(screen_text, font)
    max_text_width = max(text_widths) + TEXT_BOX_PADDING * 2

    box_rect = (
        (SCREEN_WIDTH - max_text_width) // 2,
        (free_screen_height + TEXT_BOX_PADDING * 2) // 2,
        max_text_width,
        total_text_height + line_height,
    )

    # Cover objects on screen with BG color
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        rect=box_rect,
        width=0,
    )

    pygame.draw.rect(
        surface=screen,
        color=GRAY,
        rect=box_rect,
        width=TEXT_BOX_BORDER_WIDTH,
    )

    for i, (text, text_width) in enumerate(zip(screen_text, text_widths), start=1):
        x = (SCREEN_WIDTH - text_width) // 2
        font.render_to(
            surf=screen,
            dest=(x, start_y + i * line_height),
            text=text,
            fgcolor=WHITE,
        )
    pygame.display.flip()
