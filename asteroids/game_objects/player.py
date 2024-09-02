import pygame

from asteroids.constants import (
    AZURE,
    PLAYER_LINE_WIDTH,
    PLAYER_SIZE,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from asteroids.game_objects import Shot
from asteroids.shapes import TriangleShape


class Player(TriangleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_SIZE)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.shoot_timer = 0.0

    def draw(self, screen: pygame.Surface) -> None:
        """Redraw the player on the `screen`."""
        pygame.draw.polygon(
            surface=screen,
            color=AZURE,
            points=self.triangle,
            width=PLAYER_LINE_WIDTH,
        )

    def rotate(self, dt: float) -> None:
        """Rorate the player based on user input."""
        self.rotation += int(PLAYER_TURN_SPEED * dt)

    def update(self, dt: float) -> None:
        """Update the player state and get user input."""
        self.shoot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_timer <= 0:
                self.shoot(dt)

    def move(self, dt: float) -> None:
        """Change position of player based on user input."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt: float) -> None:
        """Shoot according to user input."""
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(*self.position)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
