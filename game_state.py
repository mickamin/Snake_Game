# Defining state changes

from direction import Direction
from position import Position


# Managing the game state, including the snake, direction, food, and field size
class GameState:
    def __init__(self, snake, direction, food, field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size


# Defining the initial state
state = GameState(
    snake=[Position(4, 0), Position(4, 1), Position(4, 2)],
    direction=Direction.DOWN,
    food=Position(10, 10),
    field_size=20,
)

# Placeholder for the `step` method, which should handle the game's main logic
state.step()

# Checking the result
expected_state = [Position(4, 1), Position(4, 2), Position(4, 3)]
self.assertEqual(expected_state, state.snake)
self.assertEqual(expected_state, state.snake)
