# Implements unit tests for the snake project.

from src.main import create_food, check_food_eaten
from unittest.mock import patch

@patch('src.main.random.randint')
def test_create_food(mock_randint):
    grid_size = 47
    mock_randint.side_effect = [7, 11, 1]
    food = create_food(grid_size) 

    # Check that food is created as expected
    assert food == ((7,11), 1)

    # Check that randint is invoked correctly
    expected_calls = [((0, grid_size - 1),), ((0, grid_size - 1),), ((0, 2),)]
    mock_randint.assert_has_calls(expected_calls, any_order=False)

def test_check_food_eaten():
    snake = [(11,3),(10,3),(9,3)]
    food = ((11,3), 1)
    assert check_food_eaten(snake, food)
    snake.insert(0, (12,3))
    assert not check_food_eaten(snake, food)

