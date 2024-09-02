import pygame

from constants import GAME_OVER_FONT, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE


text = "PAUSE (press P to continue)"
text_width = GAME_OVER_FONT.get_rect(text)[2]


def draw_pause_screen(screen):
    GAME_OVER_FONT.render_to(
        surf=screen,
        dest=(
            (SCREEN_WIDTH - text_width) // 2,
            SCREEN_HEIGHT // 2,
        ),
        text="PAUSE (press P to continue)",
        fgcolor=WHITE,
    )
    pygame.display.flip()
