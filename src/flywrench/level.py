class Level:
    def __init__(self):
        self.title = None
        self.enter_point = None
        self.exit_point = None
        self.walls = []
        self.inside = []

    def set_title(self, name: str):
        self.title = name

    def set_enter(self, x: int, y: int):
        self.enter_point = Entrance(x=x, y=y)

    def set_exit(self, x: int, y: int):
        self.exit_point = Exit(x=x, y=y)

    def add_wall(self, wall: {}):
        self.walls.append(wall)

    def add_inside(self, inside: {}):
        self.inside.append(inside)

    def to_gm(self):
        level_title = f'<title>{self.title}'
        level_enter = self.enter_point.to_gm()
        level_exit = self.exit_point.to_gm()
        return "%s\n%s\n%s" % (level_title, level_enter, level_exit)


class Entrance:
    def __init__(
            self,
            x: int,
            y: int
    ):
        self.object = "shipEntrance"
        self.coordinate = CoordinatePair(x=x, y=y)

    def to_gm(self) -> str:
        line_object = f'<obj>{self.object}'
        line_coordinates = self.coordinate.to_gm()
        return "%s%s" % (line_object, line_coordinates)


class Exit(Entrance):
    def __init__(
            self,
            x: int,
            y: int
    ):
        super().__init__(x=x, y=y)
        self.object = "shipExit"


class CoordinatePair:
    def __init__(
            self,
            x: int,
            y: int
    ):
        self.x = x
        self.y = y

    def to_gm(self) -> str:
        x = f'<x1>{self.x}'
        y = f'<y1>{self.y}'
        return "%s%s" % (x, y)
