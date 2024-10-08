from __future__ import annotations

from itertools import pairwise

from typing import assert_never

import pygame

from asteroids.shapes import Shape, Polygon


class Circle(Shape):
    """Base class for game objects."""

    def __init__(self, x: float, y: float, radius: float, speed: int = 0) -> None:
        super().__init__(x, y, speed)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = speed
        self.radius = radius

    def collides_with(self, other: Circle | Polygon) -> bool:
        """Return true if the instance collides with `other` instance of CircleShape."""
        match other:
            case Circle():
                return self.position.distance_to(other.position) <= (
                    self.radius + other.radius
                )
            case Polygon():
                lines = pairwise(list(other.vertices) + [other.vertices[0]])
                return any(self._intersects_line(*points) for points in lines)
            case _:
                assert_never(other)

    def _intersects_line(
        self, line_start: pygame.Vector2, line_end: pygame.Vector2
    ) -> bool:
        circle_center_to_line_start = self.position - line_start
        line_len = line_end - line_start
        line_len_squared = line_len.dot(line_len)
        acab = circle_center_to_line_start.dot(line_len)  # mystery from Claude.ai
        t = max(0, min(line_len_squared, acab)) / line_len_squared
        closest_point = line_start + line_len * t
        return self.position.distance_to(closest_point) <= self.radius
