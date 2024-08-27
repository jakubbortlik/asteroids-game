from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
import pygame
from player import Player


def main() -> None:
    """Start the game."""
    print("Starting asteroids!")

    pygame.init() 
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    _ = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        for updatable_item in updatable:
            updatable_item.update(dt)
        for drawable_item in drawable:
            drawable_item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
