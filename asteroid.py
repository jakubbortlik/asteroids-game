import random

import pygame

from constants import ASTEROID_LINE_WIDTH, ASTEROID_MIN_RADIUS, WHITE

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float, speed: int = 0) -> None:
        super().__init__(x, y, radius, speed)

    def draw(self, screen: pygame.Surface) -> None:
        """Redraw the instance on the `screen`."""
        pygame.draw.circle(
            surface=screen,
            color=WHITE,
            center=self.position,
            radius=self.radius,
            width=ASTEROID_LINE_WIDTH,
        )

    def update(self, dt: float) -> None:
        """Update the state of the instance."""
        self.position += self.velocity * dt

    def split(self) -> None:
        """Kill the current Asteroid and spawn new ones if applicable."""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(
            x=self.position[0], y=self.position[1], radius=new_radius, speed=self.speed
        )
        new_asteroid_1.velocity = new_velocity_1 * 1.2
        new_asteroid_2 = Asteroid(
            x=self.position[0], y=self.position[1], radius=new_radius, speed=self.speed
        )
        new_asteroid_2.velocity = new_velocity_2
