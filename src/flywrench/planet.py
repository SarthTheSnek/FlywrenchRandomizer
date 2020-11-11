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
        self.published_file_id = file_id.strip()

    def to_gm(self):
        return f'<published file id>{self.published_file_id}'
