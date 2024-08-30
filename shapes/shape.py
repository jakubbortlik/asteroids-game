from __future__ import annotations

from abc import abstractmethod

import pygame


class Shape(pygame.sprite.Sprite):
    """Base class for game objects."""

    def __init__(self, x: float, y: float, speed: int = 0) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = speed

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        """Redraw the object on the `screen`."""

    @abstractmethod
    def update(self, dt: float) -> None:
        """Update the state of the object."""

    @abstractmethod
    def collides_with(self, other: Shape) -> bool:
        """Return True if the instance collides with `other` instance of a Shape."""
