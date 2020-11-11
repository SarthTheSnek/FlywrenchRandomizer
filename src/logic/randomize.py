import random

from os import listdir
from os.path import isfile, join

from gamemaker import convert
from flywrench.obstacle import LineColors
from .settings import Settings

game = []


def set_seed(seed: str):
    print("Setting seed to: " + seed)
    random.seed(seed)


def level_setup(settings: Settings):
    level_directory = settings.directory + "/ReadOnlyFiles/"
    planet_files = [f for f in listdir(level_directory) if isfile(join(level_directory, f))]
    for planet in planet_files:
        if "PLUTO" in planet:
            planet_level = convert.ToObj(level_directory, planet)
            game.append(planet_level)
        else:
            continue
    return game


def randomize_walls(game_levels: []):
    wall_colors = [LineColors.YELLOW, LineColors.PINK]
    for planet in game_levels:
        for lvl in planet.levels:
            for wall in lvl.walls:
                wall.obstacle_color = random.choice(wall_colors)
