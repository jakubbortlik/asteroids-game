import pygame

from asteroids.constants import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE
from asteroids.screens.game_over import FONT


text = "PAUSE (press P to continue)"
text_width = FONT.get_rect(text)[2]


def draw_pause_screen(screen):
    FONT.render_to(
        surf=screen,
        dest=(
            (SCREEN_WIDTH - text_width) // 2,
            SCREEN_HEIGHT // 2,
        ),
        text="PAUSE (press P to continue)",
        fgcolor=WHITE,
    )
    pygame.display.flip()
