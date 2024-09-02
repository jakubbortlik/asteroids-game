import pygame

from asteroids.constants import (
    ASTEROID_MIN_SPEED,
    FONT,
    GRAY,
    SCORE_BOX_BORDER_WIDTH,
    SCORE_BOX_HEIGHT,
    SCORE_BOX_PADDING,
    SCORE_BOX_WIDTH,
    SCORE_BOX_X,
    SCORE_BOX_Y,
)


class ScoreTracker(pygame.sprite.Sprite):
    score = 0

    def __init__(self) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

    def add_points(self, asteroid):
        self.score += int(100 / asteroid.radius * asteroid.speed / ASTEROID_MIN_SPEED)

    def draw(self, screen: pygame.Surface):
        """Redraw the score table on the `screen`."""
        pygame.draw.rect(
            surface=screen,
            color=GRAY,
            rect=(SCORE_BOX_X, SCORE_BOX_Y, SCORE_BOX_WIDTH, SCORE_BOX_HEIGHT),
            width=SCORE_BOX_BORDER_WIDTH,
        )
        FONT.render_to(
            surf=screen,
            dest=(SCORE_BOX_X + SCORE_BOX_PADDING, SCORE_BOX_Y + SCORE_BOX_PADDING),
            text=f"Score: {self.score}",
            fgcolor=GRAY,
        )
