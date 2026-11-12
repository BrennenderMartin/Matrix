import numpy as np 
#import math
import pygame as pg
import src.matrix.data.constants as c

class Obstacle:
    def __init__(self, verticies: list[list[float | int]]) -> None:
        self.verticies: np.ndarray = np.array(verticies)

    def draw(self, screen: pg.Surface, color: pg.Color) -> None:
        pg.draw.polygon(screen, color, self.getVerticiesPostitions()) # type: ignore

    def getVerticiesPostitions(self) -> list[np.ndarray]:
        return [self.getPosition(item) for item in self.verticies]
    
    def getPosition(self, vector: np.ndarray) -> np.ndarray:
        return np.array([
            c.SCREEN_MID_WIDTH + vector[0] * 100,
            c.SCREEN_MID_HEIGHT - vector[1] * 100
        ])

if "__main__" == __name__:
    o = Obstacle([[1, 1], [2, 1], [2, 2], [1, 2]])
    print(o.verticies)