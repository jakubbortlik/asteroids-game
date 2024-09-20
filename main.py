import pygame
import typer

from asteroids.constants import BLACK, SCREEN_WIDTH, SCREEN_HEIGHT
from asteroids.game_objects import Asteroid, AsteroidField, Player, Shot
from asteroids.screens.game_over import draw_game_over
from asteroids.screens.start import draw_start_screen
from asteroids.screens.pause import draw_pause_screen
from asteroids.score_tracker import ScoreTracker

cli = typer.Typer()


@cli.command()
def run() -> None:
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
    killables: pygame.sprite.Group = pygame.sprite.Group()

    Shot.containers = (shots, updatables, drawables, killables)  # type: ignore
    Asteroid.containers = (asteroids, updatables, drawables, killables)  # type: ignore
    AsteroidField.containers = (updatables,)  # type: ignore
    Player.containers = (updatables, drawables, killables)  # type: ignore
    ScoreTracker.containers = (updatables, drawables)  # type: ignore

    _ = AsteroidField()
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score_tracker = ScoreTracker()

    restart = True
    playing = True
    quit_game = False

    started = False
    while not started:
        draw_start_screen(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    started = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    started = True
                    playing = False

    paused = was_paused = False
    while playing:
        if restart:
            player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            score_tracker.score = 0
            restart = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_q:
                    quit_game = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player.speedup = 0.0

        if paused:
            was_paused = True
            draw_pause_screen(screen)
            continue

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
            if asteroid.collides_with(player) or quit_game:
                quit_game = False

                draw_game_over(screen, score_tracker.score)

                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                restart = True
                                waiting = False

                            if event.key == pygame.K_q:
                                waiting, playing = False, False

                        if event.type == pygame.QUIT:
                            waiting, playing = False, False

                for killable in killables:
                    killable.kill()


        # Redraw objects
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        tick = clock.tick(60)
        if was_paused:
            tick, was_paused = 0, False

        dt = tick / 1000


if __name__ == "__main__":
    cli()
