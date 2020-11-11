from enum import Enum


class LineColors(Enum):
    YELLOW = "bounceOff"
    WHITE = "openThru"
    RED = "closedThru"
    GREEN = "spinThru"
    BLUE = "deathWhileOn"
    PINK = "deathThru"


class Switch:
    def __init__(self):
        self.obstacle_type = "switch"
        self.coordinates = None

    def add_coordinate(self, x: int, y: int):
        self.coordinates = CoordinatePair(
            number=1,
            x=x,
            y=y
        )

    def to_gm(self) -> str:
        line_type = f'<obj>{self.obstacle_type}'
        line_coordinates = self.coordinates.to_gm()
        return '%s%s' % (line_type, line_coordinates)


class Wall(Switch):
    def __init__(self):
        super().__init__()
        self.obstacle_type = "line"
        self.obstacle_color = LineColors.YELLOW
        self.coordinates = []

    def set_color(self, color: LineColors):
        self.obstacle_color = color

    def add_coordinate(self, x: int, y: int):
        self.coordinates.append(CoordinatePair(
            number=len(self.coordinates) + 1,
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
            obstacle_color: LineColors
    ):
        super().__init__()
        self.obstacle_type = "line"
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


class Pinwheel(Obstacle):
    def __init__(
            self,
            rotation: str,
            obstacle_color: LineColors
    ):
        super().__init__(obstacle_color=obstacle_color)
        self.obstacle_type = "pinwheel"
        self.rotation = rotation

    def to_gm(self) -> str:
        line_type = f'<obj>{self.obstacle_type}'
        line_color = f'<m>{self.obstacle_color.value}'
        line_rotation = f'<direction>{self.rotation}'
        line_coordinates = ""
        for coord in self.coordinates:
            line_coordinates += coord.to_gm()
        return '%s%s%s%s' % (line_type, line_color, line_rotation, line_coordinates)


class GravityWell(Wall):
    def __init__(self):
        super().__init__()
        self.obstacle_type = "gravityWell"


class Turret(Wall):
    def __init__(self):
        super().__init__()
        self.obstacle_type = "turret"


class MovingLine(Obstacle):
    def __init__(
            self,
            obstacle_color: LineColors
    ):
        super().__init__(obstacle_color=obstacle_color)
        self.obstacle_type = "movingLine"
        self.starting_coordinate = {}
        self.ending_coordinate = {}

    def set_starting_coordinate(self, x: int, y: int):
        self.starting_coordinate = {
            "x": x,
            "y": y
        }

    def set_ending_coordinate(self, x: int, y: int):
        self.ending_coordinate = {
            "x": x,
            "y": y
        }

    def to_gm(self) -> str:
        line_type = f'<obj>{self.obstacle_type}'
        line_color = f'<m>{self.obstacle_color.value}'
        line_coordinates = ""
        for coord in self.coordinates:
            line_coordinates += coord.to_gm()
        line_start_coord = f'<startX>{self.starting_coordinate["x"]}<startY>{self.starting_coordinate["y"]}'
        line_end_coord = f'<endX>{self.ending_coordinate["x"]}<endY>{self.ending_coordinate["y"]}'
        return '%s%s%s%s%s' % (line_type, line_color, line_coordinates, line_start_coord, line_end_coord)


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

