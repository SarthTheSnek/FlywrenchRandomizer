class Planet:
    def __init__(
            self,
            name: str
    ):
        self.name = name
        self.published_file_id = None
        self.levels = []

    def add_level(self, level):
        self.levels.append(level)

    def add_published_file_id(self, file_id: str):
        self.published_file_id = file_id


class Level:
    def __init__(self):
        self.title = None
        self.enter_point = None
        self.exit_point = None
        self.walls = []
        self.inside = []

    def add_title(self, name: str):
        self.title = name

    def add_enter(self, entrance: {}):
        self.enter_point = entrance

    def add_exit(self, exit_point: {}):
        self.exit_point = exit_point

    def add_wall(self, wall: {}):
        self.walls.append(wall)

    def add_inside(self, inside: {}):
        self.inside.append(inside)


class Obstacle:
    def __init__(
            self,
            obstacle_type: str,
    ):
        self.obstacle_type = obstacle_type
        self.obstacle_color = None
        self.coordinates = []

    def add_color(self, color: str):
        self.obstacle_color = color

    def add_coordinates(self, x: int, y: int):
        length = len(self.coordinates) + 1
        x_name = "x" + str(length)
        y_name = "y" + str(length)
        coordinates = {
            x_name: x,
            y_name: y
        }
        self.coordinates.append(coordinates)
