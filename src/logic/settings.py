class Settings:
    def __init__(self):
        self.seed = None
        self.walls = False
        self.allinternal = False
        self.movinglines = False
        self.turrets = False
        self.lines = False
        self.pinwheels = False
        self.names = False
        self.intros = False
        self.theme = ""
        self.random_theme = False
        self.directory = ""

    def am_i_randomizing(self):
        if self.walls:
            return True
        else:
            return False
