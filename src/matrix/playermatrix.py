import numpy as np 
import math
import pygame as pg
from src.matrix.data import (
    constants as c,
    colours as co # type: ignore
)

class PlayerMatrix:
    def __init__(self, m: list[list[float | int]] = [[0, 0], [0, 0]], width: int = 0) -> None:
        self.direction: np.ndarray = np.array(m[0]) # Guckrichtung
        self.position: np.ndarray = np.array(m[1]) # Position
        self.pov: np.ndarray = np.add(self.direction / 2, self.position) # Blickpunkt (einfache Vektoraddition von pos + dir; wofür die / 2, bzw was verändert das?)

        self.FOVwidth: int = width # winkel, wie weit man nach links und rechts gucken kann
        self.FOVpoints: np.ndarray = self.getFOVPoints()

        self.kleft: bool = False
        self.kright: bool = False



    def rotate(self, angle: int, direction: list[bool] = [False, False]) -> np.ndarray:
        self.kleft = direction[0]
        self.kright = direction[1]
        # Boolischer Wert, der überprüft, ob in diese Richtung gedreht wird

        r: np.ndarray = self.rotationsmatrix(math.radians(angle)) # Wird nach dem Winkel (angle) erstellt, zu erklären

        #print(f"Vorherige Richtung: {self.direction}")
        #print(f"Rotationsmatrix für eine Drehung von {angle} Grad: \n{r}")

        self.direction = self.getRotatedMatrix(r) # Multiplikation von den beiden Matrizen
        self.pov = np.add(self.direction / 2, self.position) # Neue Berechnung des POV, da sich die Richtung ändert

        #print(f"Neue Richtung: {self.direction}\n")
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



    def drawChar(self, screen: pg.Surface, color: pg.Color) -> None:
        pg.draw.circle(screen, color, self.getPosition(), 5) # type: ignore
        #pg.draw.circle(screen, color, self.getPosition(self.pov), 2) # type: ignore
        pg.draw.line(screen, color, self.getPosition(), self.getPosition(self.pov), width=3) # type: ignore
        pg.draw.polygon(screen, color, self.getFOVPointsToDraw(), 2) # type: ignore

    def getFOVPoints(self, scale: int | None = None) -> np.ndarray:
        if scale is None: scale = 100
        return np.array([
            self.position,
            np.add(self.position, scale * self.getRotatedMatrix(self.rotationsmatrix(math.radians(self.FOVwidth)))),
            np.add(self.position, scale * self.getRotatedMatrix(self.rotationsmatrix(math.radians(-self.FOVwidth))))
        ])

    def getFOVPointsToDraw(self) -> list[np.ndarray]:
        return [self.getPosition(item) for item in self.getFOVPoints()]

    def getPosition(self, vector: np.ndarray | None = None) -> np.ndarray:
        if vector is None: vector = self.position
        return np.array([
            c.SCREEN_MID_WIDTH + vector[0] * 100,
            c.SCREEN_MID_HEIGHT - vector[1] * 100
        ])



    def checkAngle(self, point: np.ndarray) -> float:
        v = np.subtract(point, self.position)

        scaleProduct = np.dot(self.direction, v)
        totalLength = round(np.linalg.norm(self.direction), 6) * round(np.linalg.norm(v), 6)

        acos = round(scaleProduct / totalLength, 5)
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
