from .food import Food
from .snake import Snake

class GameState:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.snake = Snake([(11,11)])
        self.food = Food.create_random_food()

    def check_food_eaten(self) -> bool:
        return self.snake.body[0] == self.food.coords
