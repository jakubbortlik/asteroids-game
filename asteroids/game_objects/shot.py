import pygame

from asteroids.constants import SHOT_LINE_WIDTH, SHOT_RADIUS
from asteroids.shapes import Circle


class Shot(Circle):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        """Redraw the instance on the `screen`."""
        pygame.draw.circle(
            surface=screen,
            color="red",
            center=self.position,
            radius=self.radius,
            width=SHOT_LINE_WIDTH,
        )

    def update(self, dt: float) -> None:
        """Update the state of the instance."""
        self.position += self.velocity * dt
