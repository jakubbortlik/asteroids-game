from __future__ import annotations

import pygame

from shapes import Shape


class CircleShape(Shape):
    """Base class for game objects."""

    def __init__(self, x: float, y: float, radius: float, speed: int = 0) -> None:
        super().__init__(x, y, speed)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = speed
        self.radius = radius

    def collides_with(self, other: CircleShape) -> bool:
        """Return true if the instance collides with `other` instance of CircleShape."""
        return self.position.distance_to(other.position) <= (self.radius + other.radius)
