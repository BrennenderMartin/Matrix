import numpy as np 
#import math
import pygame as pg
from src.matrix.playermatrix import PlayerMatrix
import src.matrix.data.constants as c

class Obstacle:
    def __init__(self, verticies: list[list[float | int]]) -> None:
        self.verticy: np.ndarray = np.array(verticies[0])
        self.directionx: np.ndarray = np.array(verticies[1])
        self.directiony: np.ndarray = np.array(verticies[2])



    def draw(self, screen: pg.Surface, color: pg.Color) -> None:
        pg.draw.polygon(screen, color, self.getVerticiesPostitions()) # type: ignore

    def getVerticies(self) -> np.ndarray:
        return np.array([
            [0, 0], 
            self.directionx, 
            self.directionx + self.directiony, 
            self.directiony
        ])

    def getVerticiesPostitions(self) -> np.ndarray:
        return np.array([self.getPosition(self.verticy + item) for item in self.getVerticies()])
    
    def getPosition(self, vector: np.ndarray) -> np.ndarray:
        return np.array([
            c.SCREEN_MID_WIDTH + vector[0] * 100,
            c.SCREEN_MID_HEIGHT - vector[1] * 100
        ])



    def checkTwoPlayers(self, p: PlayerMatrix, e: PlayerMatrix) -> tuple[bool, np.ndarray]:
        #print(np.array([e.position - p.position, self.directionx]))
        #print(np.array(self.verticy - p.position))

        solx: np.ndarray = np.linalg.solve(
            np.array([
                e.position - p.position,
                self.directionx
            ]), 
            np.array(self.verticy - p.position)
        )

        soly: np.ndarray = np.linalg.solve(
            np.array([
                e.position - p.position,
                self.directiony
            ]), 
            np.array(self.verticy - p.position)
        )

        sol: np.ndarray = np.array([solx, soly])

        if ((0 <= solx[0] <= 1) and (-1 <= solx[1] <= 1)) or ((0 <= soly[0] <= 1) and (-1 <= soly[1] <= 1)):
            return (True, sol)
        else:
            return (False, sol)


if "__main__" == __name__:
    o = Obstacle([[1, 1], [2, 1], [2, 2], [1, 2]])
    print(o.getVerticies())