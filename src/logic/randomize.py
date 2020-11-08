import random

from os import listdir
from os.path import isfile, join

from .convert import planet_to_dict
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
            planet_level = planet_to_dict(level_directory, planet)
            game.append(planet_level)
        else:
            continue
    return game


def randomize_walls(game_levels: []):
    wall_colors = ['bounceOff', 'deathThru']
    for planet in game_levels:
        for level in planet.levels:
            for wall in level.walls:
                wall['m'] = random.choice(wall_colors)
