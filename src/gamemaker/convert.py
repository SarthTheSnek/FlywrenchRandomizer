from flywrench import planet, level, obstacle


def ToObj(directory: str, file: str) -> planet.Planet:
    game_planet = planet.Planet(name=file.replace(".planet", ""))
    try:
        with open(directory + file, "r") as f:
            level_strings = []
            file_lines = f.readlines()
            for index, line in enumerate(file_lines):
                if "title" in line:
                    if index != 1:
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


def ToGamemaker(game: []):
    for p in game:
        print(p.to_gm())
        for lvl in p.levels:
            print(lvl.to_gm())
            for wall in lvl.walls:
                print(wall.to_gm())
            for inside in lvl.inside:
                print(inside.to_gm())


def setup_level(obj: []):
    lvl = level.Level()
    for line in obj:
        object_dict = convert_str_to_list(line)
        if 'title' in object_dict.keys():
            lvl.set_title(name=object_dict['title'])
        else:
            if object_dict['obj'] == 'shipEntrance':
                lvl.set_enter(x=int(object_dict['x1']), y=int(object_dict['y1']))
            elif object_dict['obj'] == 'shipExit':
                lvl.set_exit(x=int(object_dict['x1']), y=int(object_dict['y1']))
            else:
                if object_dict['m'] == "bounceOff":
                    wall = obstacle.Wall()
                    wall.set_color(obstacle.LineColors(value=object_dict['m']))
                    wall.add_coordinate(x=int(object_dict['x1']), y=int(object_dict['y1']))
                    wall.add_coordinate(x=int(object_dict['x2']), y=int(object_dict['y2']))
                    lvl.add_wall(wall)
                else:
                    temp = obstacle.Obstacle(
                        obstacle_type=object_dict['obj'],
                        obstacle_color=obstacle.LineColors(value=object_dict['m'])
                    )
                    temp.add_coordinate(x=int(object_dict['x1']), y=int(object_dict['y1']))
                    temp.add_coordinate(x=int(object_dict['x2']), y=int(object_dict['y2']))
                    lvl.add_inside(temp)
    return lvl


def convert_str_to_list(obj: str) -> {}:
    new_object = obj.replace('<', ',').replace('>', ',').split(',')
    new_object.pop(0)
    keys = new_object[::2]
    values = new_object[1::2]
    values[-1] = values[-1].strip()
    object_dict = dict(zip(keys, values))
    return object_dict
