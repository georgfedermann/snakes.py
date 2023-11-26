# Grid is say 21 x 21 cells
# Each cell is 25 x 25
# Padding around cell is 2

import pygame
import random

class GameConfig:
    # Define the game field
    CELL_SIZE = 27
    GRID_SIZE = 21
    TOKEN_SIZE = 25
    SCREEN_WIDTH = CELL_SIZE * GRID_SIZE
    SCREEN_HEIGHT = CELL_SIZE * GRID_SIZE

    COLOR_BLACK = (0, 0, 0)
    COLOR_BLUE = (0, 0, 255)
    COLOR_GREEN = (0, 255, 0)
    COLOR_RED = (255, 0, 0)
    COLOR_YELLOW = (255, 255, 0)

class Snake:
    def __init__(self, initial_body):
        self.body = initial_body

    def inside_snake(self, coord):
        return coord in self.body

    def get_snake_head(self):
        return self.body[0]

def calculate_snake_move(snake, dx, dy):
    if not (dx == 0 and dy == 0):
        snake_head = snake[0]
        snake.insert(0,
            (min(max(0, snake_head[0] + dx), GameConfig.GRID_SIZE - 1),
             min(max(0, snake_head[1] + dy), GameConfig.GRID_SIZE - 1)))
    return snake

def render_snake(screen, snake, snake_length):
    for i in range(len(snake)):
        snake_element = snake[i]
        square = pygame.Rect((snake_element[0] * GameConfig.CELL_SIZE,
                              snake_element[1] * GameConfig.CELL_SIZE,
                              GameConfig.TOKEN_SIZE,
                              GameConfig.TOKEN_SIZE))
        pygame.draw.rect(screen,
                         GameConfig.COLOR_BLUE if i < snake_length else GameConfig.COLOR_BLACK, square)

def truncate_snake(snake, snake_length):
    while len(snake) > snake_length:
        snake.pop(-1)

def create_food():
    food_location = (random.randint(0, GameConfig.GRID_SIZE - 1),
                     random.randint(0, GameConfig.GRID_SIZE - 1))
    food_category = random.randint(0,2)
    return (food_location, food_category)

def render_food(screen, food):
    if food == None:
        return
    food_coords = food[0]
    food_category = food[1]
    food_color = [GameConfig.COLOR_GREEN, GameConfig.COLOR_YELLOW, GameConfig.COLOR_RED][food[1]]
    square = pygame.Rect((food_coords[0] * 27, food_coords[1] * 27, 25, 25))
    pygame.draw.rect(screen, food_color, square)

def check_food_eaten(snake, food):
    return snake[0] == food[0]

def main():
    screen = pygame.display.set_mode(
            (GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))

    # Define the game clock
    clock = pygame.time.Clock()
    FPS = 5

    # Define the snake and the snake movement
    snake = [(11, 11)]
    snake_length = 1
    dx = 0
    dy = 0

    # Define the food
    food = None

    keep_running = True
    while keep_running:
        if not food:
            food = create_food()
        snake = calculate_snake_move(snake, dx, dy)
        render_snake(screen, snake, snake_length)
        if check_food_eaten(snake, food):
            snake_length += food[1] + 1
            food = None
        render_food(screen, food)
        truncate_snake(snake, snake_length)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    dx, dy = -1, 0
                elif event.key == pygame.K_d:
                    dx, dy = 1, 0
                elif event.key == pygame.K_w:
                    dx, dy = 0, -1
                elif event.key == pygame.K_s:
                    dx, dy = 0, 1
                elif event.key == pygame.K_x:
                    dx, dy = 0, 0

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()
