import pandas as pd
import math

class PlayerMatrix:
    def __init__(self, direction: list[list[int]] = [[0],[0]], position: list[list[int]] = [[0],[0]]):
        self.rotation: pd.DataFrame = pd.DataFrame(direction, index=["x", "y"])
        self.position: pd.DataFrame = pd.DataFrame(position, index=["x", "y"])

    def rotate(self, angle: int):
        r: pd.DataFrame = self.rotationsmatrix(math.radians(angle))
        
        print(f"Vorherige Richtung: {self.tupleOfMatrix(self.rotation)}")
        print(f"Rotationsmatrix für eine Drehung von {angle} Grad: \n{r}")

        self.rotation: pd.DataFrame = pd.DataFrame([
            [float(r.at["x", 0] * self.rotation.at["x", 0]) + float(r.at["x", 1] * self.rotation.at["y", 0])],
            [float(r.at["y", 0] * self.rotation.at["x", 0]) + float(r.at["y", 1] * self.rotation.at["y", 0])]
            ], index=["x", "y"]
        )

        print(f"Neue Richtung: {self.tupleOfMatrix(self.rotation)}")
        return self.rotation

    def getFOV(self, width):
        return width
    
    def rotationsmatrix(self, angle: float):
        m = pd.DataFrame([
                [round(math.cos(angle)), round(-math.sin(angle))],
                [round(math.sin(angle)), round(math.cos(angle))]
            ], index=["x", "y"]
        )
        return m 

    def tupleOfMatrix(self, m: pd.DataFrame):
        return (int(m.at["x", 0]), int(m.at["y", 0]))

player = PlayerMatrix(
    direction=[[0],[1]],
    position=[[1],[-1]])

player.rotate(90)