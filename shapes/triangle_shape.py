from __future__ import annotations

import pygame

from shapes import Shape


class TriangleShape(Shape):
    """Base class for triangular shapes."""

    def __init__(self, x: float, y: float, size: float, speed: int = 0) -> None:
        super().__init__(x, y, speed)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = speed
        self._size = size
        self.rotation = 0

    def _calculate_vertices(self):
        """Calculate the triangle vertices."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self._size / 1.5
        a = self.position + forward * self._size
        b = self.position - forward * self._size - right
        c = self.position - forward * self._size + right
        return [a, b, c]
        

    @property
    def triangle(self):
        return self._calculate_vertices()
