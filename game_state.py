# Managing the game state
from random import randint

from direction import Direction
from position import Position

# Initial game settings
INITIAL_SNAKE = [Position(1, 2), Position(2, 2), Position(3, 2)]
INITIAL_DIRECTION = Direction.RIGHT


class GameState:
    """Represents the state of the game, including the snake, direction, food, and field size."""

    def __init__(self, snake, direction, food, field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size

    def set_initial_position(self):
        """Sets the initial state of the game."""
        self.snake = INITIAL_SNAKE[:]
        self.direction = INITIAL_DIRECTION
        self.set_random_food_position()

    def next_head_position(self, direction):
        """Calculates the next position of the snake's head based on the current direction."""
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(pos.x, (pos.y - 1) % self.field_size)
        elif direction == Direction.DOWN:
            return Position(pos.x, (pos.y + 1) % self.field_size)
        elif direction == Direction.RIGHT:
            return Position((pos.x + 1) % self.field_size, pos.y)
        elif direction == Direction.LEFT:
            return Position((pos.x - 1) % self.field_size, pos.y)

    def set_random_food_position(self):
        """Places the food at a random position that does not overlap with the snake."""
        while True:
            self.food = Position(
                randint(0, self.field_size - 1), randint(0, self.field_size - 1)
            )
            if self.food not in self.snake:
                break

    def can_turn(self, direction):
        """Checks if the snake can turn to the given direction."""
        new_head = self.next_head_position(direction)
        return new_head != self.snake[-2]

    def turn(self, direction):
        """Changes the snake's direction if it is valid."""
        if self.can_turn(direction):
            self.direction = direction

    def step(self):
        """Updates the game state for the next step."""
        new_head = self.next_head_position(self.direction)

        # Check for self-collision
        if new_head in self.snake:
            self.set_initial_position()
            return

        # Move snake
        self.snake.append(new_head)

        # Check if snake ate the food
        if new_head == self.food:
            self.set_random_food_position()
        else:
            # Remove the tail if the snake didn't eat
            self.snake = self.snake[1:]
