import pygame

from asteroids.constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE
from asteroids.screens.game_over import GAME_OVER_FONT


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
