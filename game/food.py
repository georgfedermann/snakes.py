from __future__ import annotations
from .config import GameConfig

import pygame
import random

class Food:
    def __init__(self, coords, category):
        self.coords = coords
        self.category = category

    def render_food(self, screen) -> None:
        food_color = [GameConfig.COLOR_GREEN, GameConfig.COLOR_YELLOW, GameConfig.COLOR_RED][self.category]
        square = pygame.Rect((self.coords[0] * GameConfig.CELL_SIZE,
                              self.coords[1] * GameConfig.CELL_SIZE,
                              GameConfig.TOKEN_SIZE,
                              GameConfig.TOKEN_SIZE))
        pygame.draw.rect(screen, food_color, square)

    @classmethod
    def create_random_food(cls) -> Food:
        coord = (random.randint(0, GameConfig.GRID_SIZE - 1),
                 random.randint(0, GameConfig.GRID_SIZE - 1))
        category = random.randint(0,2)
        return cls(coord, category)
