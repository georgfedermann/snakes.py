# Grid is say 21 x 21 cells
# Each cell is 25 x 25
# Padding around cell is 2

from game.config import GameConfig
from game.food import Food
from game.state import GameState

import pygame
import random

def main():
    screen = pygame.display.set_mode(
            (GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))

    # Define the game clock
    clock = pygame.time.Clock()
    FPS = 5

    # Initialize the game's state and variables
    game_state = GameState()

    keep_running = True
    while keep_running:
        game_state.snake.calculate_snake_move(game_state)
        game_state.snake.render_snake(screen)
        if game_state.check_food_eaten():
            game_state.snake.length += game_state.food.category + 1
            game_state.food = None
        while not game_state.food or game_state.snake.inside_snake(game_state.food.coords):
            game_state.food = Food.create_random_food()
        game_state.food.render_food(screen)
        game_state.snake.truncate_snake()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game_state.dx, game_state.dy = -1, 0
                elif event.key == pygame.K_d:
                    game_state.dx, game_state.dy = 1, 0
                elif event.key == pygame.K_w:
                    game_state.dx, game_state.dy = 0, -1
                elif event.key == pygame.K_s:
                    game_state.dx, game_state.dy = 0, 1
                elif event.key == pygame.K_x:
                    game_state.dx, game_state.dy = 0, 0
                elif eventkey == pygame.K_q:
                    keep_running = False

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()
