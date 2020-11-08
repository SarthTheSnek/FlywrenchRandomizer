import os
from . import planet

WALLTYPES = ['bounceOff']


def planet_to_dict(directory: str, file: str) -> planet.Planet:
    game_planet = planet.Planet(name=file.replace(".planet", ""))
    try:
        with open(directory + file, "r") as f:
            level_strings = []
            file_lines = f.readlines()
            for index, line in enumerate(file_lines):
                if "title" in line:
                    new_level = setup_level(level_strings)
                    game_planet.add_level(new_level)
                    level_strings.clear()
                    level_strings.append(line)
                elif index+1 == len(file_lines):
                    level_strings.append(line)
                    new_level = setup_level(level_strings)
                    game_planet.add_level(new_level)
                elif not line.strip():
                    continue
                elif "published file id" in line:
                    game_planet.add_published_file_id(line.split('>')[1])
                else:
                    level_strings.append(line)
    except FileNotFoundError:
        print("Could not open file")
    except Exception as err:
        print(err)

    return game_planet


def setup_level(obj: []) -> planet.Level:
    level = planet.Level()
    for line in obj:
        object_dict = convert_str_to_list(line)
        if 'title' in object_dict.keys():
            level.add_title(object_dict['title'])
        else:
            if object_dict['obj'] == 'shipEntrance':
                level.add_enter(object_dict)
            elif object_dict['obj'] == 'shipExit':
                level.add_exit(object_dict)
            else:
                if object_dict['m'] in WALLTYPES:
                    level.add_wall(object_dict)
                else:
                    level.add_inside(object_dict)
    return level


def convert_str_to_list(obj: str) -> {}:
    new_object = obj.replace('<', ',').replace('>', ',').split(',')
    new_object.pop(0)
    keys = new_object[::2]
    values = new_object[1::2]
    values[-1] = values[-1].strip()
    object_dict = dict(zip(keys, values))
    return object_dict


def output_planet_to_file(obj: planet.Planet):
    print("Hello World")
