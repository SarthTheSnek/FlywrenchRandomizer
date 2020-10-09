from PySide2.QtWidgets import QMessageBox

from .convert import *
from .settings import Settings


def randomize_levels(settings: Settings):
    print("Made it into the thing")
    level_directory = settings.directory + "/ReadOnlyFiles/"
    print("Level directory:" + level_directory)
    msgBox = QMessageBox()
    msgBox.setText("Congrats! This is a thing!")
    msgBox.exec_()
    print("Finished")
    # game = convert_levels(settings)


def convert_levels(filepath: str) -> {}:
    return {}
