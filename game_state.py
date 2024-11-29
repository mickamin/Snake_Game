# Defining state changes

from random import randint

from direction import Direction
from position import Position

# Defining the initial game settings
INITIAL_SNAKE = [Position(1, 2), Position(2, 2), Position(3, 2)]
INITIAL_DIRECTION = Direction.RIGHT


# Managing the game state, including the snake, direction, food, and field size
class GameState:
    # Initialize the game state.
    def __init__(self, snake, direction, food, field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size

    # Resetting game state to the initial position, setting a random food position.
    def set_initial_position(self):
        self.snake = INITIAL_SNAKE[:]
        self.direction = INITIAL_DIRECTION
        self.set_random_food_position()

    # Calculating the next position of the snake's head based on its current direction.
    def next_head_position(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(pos.x, (pos.y - 1) % self.field_size)
        elif direction == Direction.DOWN:
            return Position(pos.x, (pos.y + 1) % self.field_size)
        elif direction == Direction.RIGHT:
            return Position((pos.x + 1) % self.field_size, pos.y)
        elif direction == Direction.LEFT:
            return Position((pos.x - 1) % self.field_size, pos.y)

    # Placing the food at a random position, ensuring it does not overlap with the snake.
    def set_random_food_position(self):
        search = True
        while search:
            self.food = Position(
                randint(0, self.field_size - 1), randint(0, self.field_size - 1)
            )
            search = self.food in self.snake

    # Checking if the snake can turn in the specified direction without colliding with itself.
    def can_turn(self, direction):
        new_head = self.next_head_position(direction)
        return new_head != self.snake[-2]

    # Updating the game state for the next step, moving the snake and handling collisions.
    def step(self):
        new_head = self.next_head_position(self.direction)

        if new_head in self.snake:
            self.set_initial_position()
            return

        self.snake.append(new_head)

        if new_head == self.food:
            # Snake ate the food; place new food
            self.set_random_food_position()
        else:
            # Remove the tail if the snake didn't eat
            self.snake = self.snake[1:]
