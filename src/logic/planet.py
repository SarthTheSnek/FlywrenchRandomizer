class Planet:
    def __init__(
            self,
            name: str
    ):
        self.name = name
        self.published_file_id = None
        self.levels = []

    def add_level(self, level: {}):
        self.levels[level['name']] = level['objects']

    def add_published_file_id(self, file_id: str):
        self.published_file_id = file_id


class Level:
    def __init__(
            self,
            name: str
    ):
        self.name = name
        self.obstacles = []

    def add_obstacle(self, obstacle: {}):
        self.obstacles.append(obstacle)


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

