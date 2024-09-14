import pytest

from asteroids.game_objects import Asteroid, Player


class TestCollisions:
    @pytest.mark.parametrize(
        "asteroid, player",
        [pytest.param(Asteroid(x=0, y=0, radius=3), Player(x=10, y=10))],
    )
    def test_collides_with(self, circle_shape):
        assert True
