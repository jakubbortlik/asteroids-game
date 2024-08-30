import pygame

from constants import (
    BLACK,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from asteroid import Asteroid
from asteroidfield import AsteroidField
from game_over_screen import draw_game_over
from player import Player
from score_tracker import ScoreTracker
from shot import Shot


def main() -> None:
    """Start the game."""
    print("Starting asteroids!")
    pygame.display.set_caption("Kill all the asteroids before they kill you!")

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
    ScoreTracker.containers = (updatables, drawables) # type: ignore

    _ = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score_tracker = ScoreTracker()

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        screen.fill(color=BLACK)

        # Update objects
        for updatable in updatables:
            updatable.update(dt)

        # Check for collision of any of the asteroids with any of the bullets
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    score_tracker.add_points(asteroid)
                    shot.kill()
                    asteroid.split()

        # Check for collision of the player with any of the asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                playing = False

        # Redraw objects
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
    draw_game_over(screen, score_tracker.score)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
        pygame.display.flip()

if __name__ == "__main__":
    main()
