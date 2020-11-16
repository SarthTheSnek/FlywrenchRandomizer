import random
import sys

from os import listdir, path
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
        planet_level = convert.ToObj(level_directory, planet)
        game.append(planet_level)
    return game


def randomize_level_names(game_levels: []):
    if getattr(sys, 'frozen', False):
        application_path = path.join(path.dirname(sys.executable), "flywrench", "space_words.txt")
    elif __file__:
        application_path = path.join(path.dirname(__file__), "../", "flywrench", "space_words.txt")

    with open(application_path) as f:
        lines = f.readlines()
        for planet in game_levels:
            for lvl in planet.levels:
                new_level_name = f'{random.choice(lines).strip()}_{random.choice(lines).strip()}'
                print(new_level_name)
                lvl.set_title(name=new_level_name)


def randomize_walls(game_levels: []):
    wall_colors = [LineColors.YELLOW, LineColors.PINK]
    for planet in game_levels:
        for lvl in planet.levels:
            for wall in lvl.walls:
                wall.obstacle_color = random.choice(wall_colors)
