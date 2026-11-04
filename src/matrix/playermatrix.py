import pandas as pd # type: ignore
import math
import pygame as pg # type: ignore
import src.matrix.var.constants as c

class PlayerMatrix:
    def __init__(self, direction: list[list[float]] = [[0],[0]], position: list[list[float]] = [[0],[0]], width: int = 0): # type: ignore
        self.rotation: pd.DataFrame = pd.DataFrame(direction, index=["x", "y"])
        self.position: pd.DataFrame = pd.DataFrame(position, index=["x", "y"])
        self.direction: pd.DataFrame = self.getDirection()
        self.leftBorder, self.rightBorder = self.getFOV(width)


    def rotate(self, angle: float):
        r: pd.DataFrame = self.rotationsmatrix(math.radians(angle))
        
        #print(f"Vorherige Richtung: {self.tupleOfMatrix(self.rotation)}")
        #print(f"Rotationsmatrix für eine Drehung von {angle} Grad: \n{r}")

        self.rotation = self.getRotatedMatrix(r) # type: ignore
        self.direction = self.getDirection()

        #print(f"Neue Richtung: {self.tupleOfMatrix(self.rotation)}\n")
        return self.rotation

    def move(self, m: tuple[float, float]):
        self.position = pd.DataFrame([
                [self.position.at["x", 0] + m[0]], # type: ignore
                [self.position.at["y", 0] + m[1]]  # type: ignore
            ], index=["x", "y"]
        )
        return self.position
    
    def getPosition(self, vektor = None): # type: ignore
        if vektor is None: vektor = self.position
        return (
            c.SCREEN_MID_WIDTH + vektor.at["x", 0] * 100, # type: ignore
            c.SCREEN_MID_HEIGHT - vektor.at["y", 0] * 100 # type: ignore
        ) # type: ignore

    def getDirection(self):
        return pd.DataFrame([
            [self.position.at["x", 0] + self.rotation.at["x", 0]], # type: ignore
            [self.position.at["y", 0] + self.rotation.at["y", 0]]  # type: ignore
        ], index=["x", "y"]
        )

    def drawChar(self, screen, color): # type: ignore
        pg.draw.circle(screen, color, self.getPosition(), 5) # type: ignore
        pg.draw.circle(screen, color, self.getPosition(self.direction), 2) # type: ignore
        pg.draw.line(screen, color, self.getPosition(), self.getPosition(self.direction), width=3) # type: ignore







    def getDirectionVektor(self, position = None, direction = None): # type: ignore
        if position is None: position = self.position
        if direction is None: direction = self.rotation
        return self.getPosition(pd.DataFrame([ # type: ignore
            [position.at["x", 0] + direction.at["x", 0]], # type: ignore
            [position.at["y", 0] + direction.at["y", 0]]  # type: ignore
        ], index=["x", "y"]
        ))


    def checkIfPointInFOV(self, point: pd.DataFrame):
        relativePosition = self.getRelativePostion(point) # type: ignore
        print(self.getAngleOfTwoDirections(relativePosition)) # type: ignore
        return 

    def getRelativePostion(self, point: pd.DataFrame, origin = None): # type: ignore
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

    def getAngleOfTwoDirections(self, direction: pd.DataFrame, rotation = None): # type: ignore
        if rotation is None: rotation = self.norm(self.rotation)
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


    def getRotatedMatrix(self, rotating: pd.DataFrame, toRotate = None): # type: ignore
        if toRotate is None: toRotate = self.rotation
        return pd.DataFrame([
            [round(rotating.at["x", 0] * toRotate.at["x", 0] + rotating.at["x", 1] * toRotate.at["y", 0], 6)], # type: ignore
            [round(rotating.at["y", 0] * toRotate.at["x", 0] + rotating.at["y", 1] * toRotate.at["y", 0], 6)]  # type: ignore
            ], index=["x", "y"]
        )


    def rotationsmatrix(self, angle: float):
        m = pd.DataFrame([
                [round(math.cos(angle), 6), round(-math.sin(angle), 6)],
                [round(math.sin(angle), 6), round(math.cos(angle), 6)]
            ], index=["x", "y"]
        )
        return m 


    def tupleOfMatrix(self, m: pd.DataFrame):
        return (float(m.at["x", 0]), float(m.at["y", 0])) # type: ignore

if "__main__" == __name__:

    p = PlayerMatrix(
        direction=[[1],[1]],
        position=[[1],[2]]
    )

    p.getFOV(30)
    p.rotate(-30)
    p.getFOV(30)
    p.checkIfPointInFOV(pd.DataFrame([[5],[5]], index=["x", "y"]))
