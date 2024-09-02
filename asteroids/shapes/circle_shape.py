from __future__ import annotations

from itertools import pairwise

from typing import assert_never

import pygame

from asteroids.shapes import Shape, TriangleShape


class CircleShape(Shape):
    """Base class for game objects."""

    def __init__(self, x: float, y: float, radius: float, speed: int = 0) -> None:
        super().__init__(x, y, speed)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = speed
        self.radius = radius

    def collides_with(self, other: CircleShape | TriangleShape) -> bool:
        """Return true if the instance collides with `other` instance of CircleShape."""
        match other:
            case CircleShape():
                return self.position.distance_to(other.position) <= (self.radius + other.radius)
            case TriangleShape():
                lines = pairwise(list(other.triangle) + [other.triangle[0]])
                return any(self._intersects_line(*points) for points in lines)
            case _:
                assert_never(other)

    def _intersects_line(self, line_start: pygame.Vector2, line_end: pygame.Vector2) -> bool:
        ac = self.position - line_start
        ab = line_end - line_start
        ab2 = ab.dot(ab)
        acab = ac.dot(ab)
        t = acab / ab2

        t = max(0, min(ab2, ac.dot(ab))) / ab2

        closest_point = line_start + ab * t
        return self.position.distance_to(closest_point) <= self.radius
