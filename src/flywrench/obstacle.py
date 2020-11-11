from enum import Enum


class LineColors(Enum):
    YELLOW = "bounceOff"
    WHITE = "openThru"
    RED = "closedThru"
    GREEN = "spinThru"
    BLUE = "deathWhileOn"
    PINK = "deathThru"


class Wall:
    def __init__(self):
        self.obstacle_type = "line"
        self.obstacle_color = LineColors.YELLOW
        self.coordinates = []

    def set_color(self, color: LineColors):
        self.obstacle_color = color

    def add_coordinate(self, x: int, y: int):
        self.coordinates.append(CoordinatePair(
            number=len(self.coordinates)+1,
            x=x,
            y=y
        ))

    def to_gm(self) -> str:
        line_type = f'<obj>{self.obstacle_type}'
        line_color = f'<m>{self.obstacle_color.value}'
        line_coordinates = ""
        for coord in self.coordinates:
            line_coordinates += coord.to_gm()
        return '%s%s%s' % (line_type, line_color, line_coordinates)


class Obstacle(Wall):
    def __init__(
            self,
            obstacle_type: str,
            obstacle_color: LineColors
    ):
        super().__init__()
        self.obstacle_type = obstacle_type
        self.obstacle_color = obstacle_color
        self.coordinates = []

    def add_coordinate(self, x: int, y: int):
        self.coordinates.append(
            CoordinatePair(
                number=len(self.coordinates) + 1,
                x=x,
                y=y
            )
        )


class CoordinatePair:
    def __init__(
            self,
            number: int,
            x: int,
            y: int
    ):
        self.number = number
        self.x = x
        self.y = y

    def to_gm(self) -> str:
        x = f'<x{self.number}>{self.x}'
        y = f'<y{self.number}>{self.y}'
        return '%s%s' % (x, y)
