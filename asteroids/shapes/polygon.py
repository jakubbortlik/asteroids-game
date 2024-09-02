from __future__ import annotations

from abc import abstractmethod

import pygame

from asteroids.shapes import Shape


class Polygon(Shape):
    """Base class for triangular shapes."""

    def __init__(self, x: float, y: float, size: float, speed: int = 0) -> None:
        super().__init__(x, y, speed)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = speed
        self._size = size
        self.rotation = 0

    @abstractmethod
    def _get_vertices(self):
        """Calculate the polygon vertices."""
        
    @property
    def vertices(self):
        return self._get_vertices()
