# Unit Tests for Game State
import unittest

from direction import Direction
from game_state import GameState
from position import Position


class GameStateTest(unittest.TestCase):
    """Unit tests for GameState behavior."""

    def test_snake_moves(self):
        """Test snake movement in various directions."""
        directions = {
            Direction.DOWN: [Position(1, 3), Position(1, 4), Position(1, 5)],
            Direction.RIGHT: [Position(1, 3), Position(1, 4), Position(2, 4)],
            Direction.LEFT: [Position(1, 3), Position(1, 4), Position(0, 4)],
            Direction.UP: [Position(2, 2), Position(3, 2), Position(3, 1)],
        }
        for dir, expected in directions.items():
            with self.subTest(direction=dir):
                state = GameState(
                    snake=[Position(1, 2), Position(1, 3), Position(1, 4)],
                    direction=dir,
                    food=Position(10, 10),
                    field_size=20,
                )
                state.step()
                self.assertEqual(expected, state.snake)

    def test_snake_wraps(self):
        """Test snake wrapping around the field edges."""
        # Add similar cases for wrapping behavior...

    def test_snake_eats_food(self):
        """Test that snake grows when eating food."""
        # Add tests for food eating...

    def test_snake_collision(self):
        """Test resetting when the snake collides with itself."""
        # Add tests for collision...
