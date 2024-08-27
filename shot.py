import pygame

from constants import SHOT_LINE_WIDTH, SHOT_RADIUS
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="red",
            center=self.position,
            radius=self.radius,
            width=SHOT_LINE_WIDTH,
        )

    def update(self, dt):
        self.position += self.velocity * dt
