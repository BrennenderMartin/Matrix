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
        #self.direction: pd.DataFrame = self.getDirection()
        self.FOVwidth: int = width
        #self.leftBorder, self.rightBorder = self.getFOV(self.FOVwidth)


    def rotate(self, angle: int) -> np.ndarray:
        r: np.ndarray = self.rotationsmatrix(math.radians(angle))
        
        #print(f"Vorherige Richtung: {self.direction}")
        #print(f"Rotationsmatrix für eine Drehung von {angle} Grad: \n{r}")

        self.direction = self.getRotatedMatrix(r) 
        self.pov = np.add(self.direction, self.position)

        #print(f"Neue Richtung: {self.direction}\n")
        return self.direction

    def move(self, m: tuple[float, float]) -> np.ndarray:
        self.position = np.add(self.position, np.array(m))
        self.pov = np.add(self.pov, np.array(m))
        return self.position
    
    def getPosition(self, vektor: np.ndarray | None = None) -> np.ndarray:
        if vektor is None: vektor = self.position
        return (
            c.SCREEN_MID_WIDTH + vektor[0] * 100, # type: ignore
            c.SCREEN_MID_HEIGHT - vektor[1] * 100 # type: ignore
        )

    def drawChar(self, screen, color) -> None: # type: ignore
        pg.draw.circle(screen, color, self.getPosition(), 5) # type: ignore
        pg.draw.circle(screen, color, self.getPosition(self.pov), 2) # type: ignore
        pg.draw.line(screen, color, self.getPosition(), self.getPosition(self.pov), width=3) # type: ignore


    """
    def getDirectionVektor(self, position: pd.DataFrame | None = None, direction: pd.DataFrame | None = None) -> tuple[int | float]:
        if position is None: position = self.position
        if direction is None: direction = self.rotation
        return self.getPosition(pd.DataFrame([
            [position.at["x", 0] + direction.at["x", 0]], # type: ignore
            [position.at["y", 0] + direction.at["y", 0]]  # type: ignore
        ], index=["x", "y"]
        ))


    def checkIfPointInFOV(self, point: pd.DataFrame) -> bool:
        relativePosition = self.getRelativePostion(point)
        try:
            angle = self.getAngleOfTwoDirections(relativePosition)
        except:
            angle = 0
        
        
        print(angle)
        if angle == 0:
            return False
        elif angle < self.FOVwidth:
            return True
        else:
            return False


    def getRelativePostion(self, point: pd.DataFrame, origin: pd.DataFrame | None = None): # type: ignore
        if origin is None: origin = self.position

        dx = point.at["x", 0] - origin.at["x", 0] # type: ignore
        dy = point.at["y", 0] - origin.at["y", 0] # type: ignore
        return pd.DataFrame([
            [dx / (dx + dy)], # type: ignore
            [dy / (dx + dy)], # type: ignore
            ], index=["x", "y"]
        )

    def norm(self, m: pd.DataFrame):
        length: float = m.at["x", 0] + m.at["y", 0] # type: ignore
        return pd.DataFrame([
            [m.at["x", 0] / length], # type: ignore
            [m.at["y", 0] / length]  # type: ignore
            ],index=["x", "y"]
        )

    def getAngleOfTwoDirections(self, direction: pd.DataFrame, rotation: pd.DataFrame | None = None): 
        if rotation is None: rotation = self.norm(self.rotation)
        print(f"{direction}\n{rotation}")
        return math.degrees(
            math.acos(
                (
                    direction.at["x", 0] * rotation.at["x", 0] # type: ignore
                ) + (
                    direction.at["y", 0] * rotation.at["y", 0] # type: ignore
                )
            )
        )

    def getFOV(self, width: int):
        self.leftBorder: pd.DataFrame = self.getRotatedMatrix(self.rotationsmatrix(math.radians(width))) # type: ignore
        self.rightBorder: pd.DataFrame = self.getRotatedMatrix(self.rotationsmatrix(math.radians(-width))) # type: ignore

        #print(f"FOV border vectors for direction {self.tupleOfMatrix(self.rotation)}:\n{self.tupleOfMatrix(self.leftBorder)}\n{self.tupleOfMatrix(self.rightBorder)}\n")

        return self.leftBorder, self.rightBorder
    """

    def getRotatedMatrix(self, rotating: np.ndarray, toRotate: np.ndarray | None = None) -> np.ndarray:
        if toRotate is None: toRotate = self.direction
        #print(f"Rotating:\n{rotating}\n\nToRotate:\n{toRotate}")
        return np.matmul(rotating, toRotate)


    def rotationsmatrix(self, angle: float) -> np.ndarray:
        return np.array([
                [round(math.cos(angle), 6), round(-math.sin(angle), 6)],
                [round(math.sin(angle), 6), round(math.cos(angle), 6)]
        ])

if "__main__" == __name__:
    p = PlayerMatrix([[0, 1], [1, 1]], 30)
    print(p.rotate(-90))

    """
    p.getFOV(30)
    p.rotate(-30)
    p.getFOV(30)
    p.checkIfPointInFOV(pd.DataFrame([[5],[5]], index=["x", "y"]))"""
