import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects."""

    def __init__(self, x: float, y: float, radius: float, speed: int = 0) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = speed
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        """Redraw the object on the `screen`."""

    def update(self, dt: float) -> None:
        """Update the state of the object."""

    def collides_with(self, other: "CircleShape") -> bool:
        """Return true if the instance collides with `other` instance of CircleShape."""
        return self.position.distance_to(other.position) <= (self.radius + other.radius)
