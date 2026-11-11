import pandas as pd # type: ignore
import numpy as np 
import math
import pygame as pg # type: ignore
import src.matrix.data.constants as c

class PlayerMatrix:
    def __init__(self, m: list[list[float | int]] = [[0, 0], [0, 0]], width: int = 0):
        self.direction: np.ndarray = np.array(m[0])
        self.position: np.ndarray = np.array(m[1])
        self.pov: np.ndarray = np.add(self.direction, self.position)

        self.FOVwidth: int = width

        self.kleft: bool = False
        self.kright: bool = False



    def rotate(self, angle: int, direction: list[bool] = [False, False]) -> np.ndarray:
        self.kleft = direction[0]
        self.kright = direction[1]

        r: np.ndarray = self.rotationsmatrix(math.radians(angle))

        #print(f"Vorherige Richtung: {self.direction}")
        #print(f"Rotationsmatrix für eine Drehung von {angle} Grad: \n{r}")

        self.direction = self.getRotatedMatrix(r) 
        self.pov = np.add(self.direction, self.position)

        #print(f"Neue Richtung: {self.direction}\n")
        return self.direction

    def getRotatedMatrix(self, rotating: np.ndarray, toRotate: np.ndarray | None = None) -> np.ndarray:
        if toRotate is None: toRotate = self.direction
        return np.matmul(rotating, toRotate)

    def rotationsmatrix(self, angle: float) -> np.ndarray:
        return np.array([
                [round(math.cos(angle), 6), round(-math.sin(angle), 6)],
                [round(math.sin(angle), 6), round(math.cos(angle), 6)]
        ])



    def move(self, m: tuple[float, float]) -> np.ndarray:
        self.position = np.add(self.position, np.array(m))
        self.pov = np.add(self.pov, np.array(m))
        return self.position



    def drawChar(self, screen, color) -> None: # type: ignore
        pg.draw.circle(screen, color, self.getPosition(), 5) # type: ignore
        pg.draw.circle(screen, color, self.getPosition(self.pov), 2) # type: ignore
        pg.draw.line(screen, color, self.getPosition(), self.getPosition(self.pov), width=3) # type: ignore

    def getPosition(self, vektor: np.ndarray | None = None) -> np.ndarray:
        if vektor is None: vektor = self.position
        return np.array([
            c.SCREEN_MID_WIDTH + vektor[0] * 100, # type: ignore
            c.SCREEN_MID_HEIGHT - vektor[1] * 100 # type: ignore
        ])



    def checkAngle(self, point: np.ndarray) -> float:
        v = np.subtract(point, self.position)
        scaleProduct = np.dot(self.direction, v)
        totalLength = round(np.linalg.norm(self.direction), 6) * round(np.linalg.norm(v), 6)
        acos = round(scaleProduct / totalLength, 5)
        #print(acos)
        if acos > 1: math.floor(acos)
        return round(math.degrees(math.acos(acos)), 3)

    def checkIfPointInFOV(self, point: np.ndarray) -> bool:
        return self.checkAngle(point) < self.FOVwidth


if "__main__" == __name__:
    p = PlayerMatrix([[0, 1], [1, 1]], 30)
    print(p.rotate(-30))
    print(p.checkAngle(np.array([3, 3])))

"""
ToDo:
- FOV zeichnen
- Turn based oder multi threated?
- Hindernisse
"""
