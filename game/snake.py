from .config import GameConfig
from typing import Tuple

import pygame

class Snake:
    def __init__(self, initial_coord):
        self.body = initial_coord
        self.length = 1

    def inside_snake(self, coord) -> bool:
        return coord in self.body

    def get_snake_head(self) -> Tuple[int,int]:
        return self.body[0]

    def truncate_snake(self) -> None:
        while len(self.body) > self.length:
            self.body.pop(-1)

    def render_snake(self, screen) -> None:
        for i in range(len(self.body)):
            snake_element = self.body[i]
            square = pygame.Rect((snake_element[0] * GameConfig.CELL_SIZE,
                                  snake_element[1] * GameConfig.CELL_SIZE,
                                  GameConfig.TOKEN_SIZE,
                                  GameConfig.TOKEN_SIZE))
            pygame.draw.rect(screen,
                             GameConfig.COLOR_BLUE if i < self.length else GameConfig.COLOR_BLACK, square)

    def calculate_snake_move(self, game_state) -> None:
        dx, dy = game_state.dx, game_state.dy
        if not (dx == 0 and dy == 0):
            snake_head = self.body[0]
            self.body.insert(0,
                (min(max(0, snake_head[0] + dx), GameConfig.GRID_SIZE - 1),
                 min(max(0, snake_head[1] + dy), GameConfig.GRID_SIZE - 1)))
