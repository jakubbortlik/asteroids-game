import sys

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main() -> None:
    """Start the game."""
    print("Starting asteroids!")

    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0

    updatables: pygame.sprite.Group = pygame.sprite.Group()
    drawables: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    shots: pygame.sprite.Group = pygame.sprite.Group()

    Shot.containers = (shots, updatables, drawables)  # type: ignore
    Asteroid.containers = (asteroids, updatables, drawables)  # type: ignore
    AsteroidField.containers = (updatables,)  # type: ignore
    Player.containers = (updatables, drawables)  # type: ignore

    _ = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        for updatable in updatables:
            updatable.update(dt)

        # Check for collision of any of the asteroids with any of the bullets
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        # Check for collision of the player with any of the asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
