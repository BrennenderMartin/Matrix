import numpy as np 
import math
import pygame as pg # type: ignore
from src.matrix.data import (
    constants as c, # type: ignore
    colours as co # type: ignore
)

class PlayerMatrix:
    def __init__(self, m: list[list[float | int]] = [[0, 0], [0, 0]], width: int = 0) -> None:
        self.direction: np.ndarray = np.array(m[0]) # Guckrichtung
        self.position: np.ndarray = np.array(m[1]) # Position
        self.pov: np.ndarray = np.add(self.direction / 2, self.position) # Blickpunkt (einfache Vektoraddition von pos + dir; wofür die / 2, bzw was verändert das?)

        self.FOVwidth: int = width # Winkel, wie weit man nach links und rechts gucken kann
        #self.FOVpoints: np.ndarray = self.getFOVPoints()


    def rotate(self, angle: int, direction: list[bool] = [False, False]) -> np.ndarray:
        r: np.ndarray = self.rotationsmatrix(math.radians(angle)) # Wird nach dem Winkel (angle) erstellt, zu erklären

        self.direction = self.getRotatedMatrix(r) # Multiplikation von den beiden Matrizen
        self.pov = np.add(self.direction / 2, self.position) # Neue Berechnung des POV, da sich die Richtung ändert

        return self.direction

    def getRotatedMatrix(self, rotating: np.ndarray, toRotate: np.ndarray | None = None) -> np.ndarray:
        if toRotate is None: toRotate = self.direction
        return np.matmul(rotating, toRotate) # Multiplikation von den zwei Matrizen

    def rotationsmatrix(self, angle: float) -> np.ndarray:
        return np.array([
                [round(math.cos(angle), 6), round(-math.sin(angle), 6)],
                [round(math.sin(angle), 6), round(math.cos(angle), 6)]
        ])



    def move(self, m: tuple[float, float]) -> np.ndarray: # Addition des Bewegungsvektor und der einzelnen Matrizen (Position, POV und FOV Punkte)
        self.position = np.add(self.position, np.array(m))
        self.pov = np.add(self.pov, np.array(m))
        self.FOVpoints = np.add(self.FOVpoints, np.repeat([np.array(m)], len(self.FOVpoints), axis=0)) # erklären!!
        return self.position