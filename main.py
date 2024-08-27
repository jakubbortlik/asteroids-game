from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
import pygame


def main() -> None:
    """Start the game."""
    print("Starting asteroids!")
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
