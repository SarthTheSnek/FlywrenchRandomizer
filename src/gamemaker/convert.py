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
                    if line.strip():
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
                if object_dict['obj'] == "gravityWell":
                    gravity = obstacle.GravityWell()
                    gravity.add_coordinate(x=int(object_dict['x1']), y=int(object_dict['y1']))
                    gravity.add_coordinate(x=int(object_dict['x2']), y=int(object_dict['y2']))
                    lvl.add_wall(gravity)
                elif object_dict['obj'] == "pinwheel":
                    pinwheel = obstacle.Pinwheel(object_dict['direction'], obstacle.LineColors(value=object_dict['m']))
                    pinwheel.add_coordinate(x=int(object_dict['x1']), y=int(object_dict['y1']))
                    pinwheel.add_coordinate(x=int(object_dict['x2']), y=int(object_dict['y2']))
                    lvl.add_pinwheel(pinwheel)
                elif object_dict['obj'] == "turret":
                    turret = obstacle.Turret()
                    turret.add_coordinate(x=int(object_dict['x1']), y=int(object_dict['y1']))
                    turret.set_color(obstacle.LineColors(value=object_dict['m']))
                    lvl.add_turret(turret)
                elif object_dict['obj'] == "switch":
                    switch = obstacle.Switch()
                    switch.add_coordinate(x=int(object_dict['x1']), y=int(object_dict['y1']))
                    lvl.add_switch(switch)
                elif object_dict['obj'] == "movingLine":
                    movingline = obstacle.MovingLine(obstacle.LineColors(value=object_dict['m']))
                    movingline.add_coordinate(x=int(object_dict['x1']), y=int(object_dict['y1']))
                    movingline.add_coordinate(x=int(object_dict['x2']), y=int(object_dict['y2']))
                    movingline.set_starting_coordinate(x=int(object_dict['startX']), y=int(object_dict['startY']))
                    movingline.set_ending_coordinate(x=int(object_dict['endX']), y=int(object_dict['endY']))
                    lvl.add_movingline(movingline)
                elif object_dict['m'] == "bounceOff":
                    wall = obstacle.Wall()
                    wall.add_coordinate(x=int(object_dict['x1']), y=int(object_dict['y1']))
                    wall.add_coordinate(x=int(object_dict['x2']), y=int(object_dict['y2']))
                    lvl.add_wall(wall)
                else:
                    obst = obstacle.Obstacle(obstacle_color=obstacle.LineColors(value=object_dict['m']))
                    obst.add_coordinate(x=int(object_dict['x1']), y=int(object_dict['y1']))
                    obst.add_coordinate(x=int(object_dict['x2']), y=int(object_dict['y2']))
                    lvl.add_inside(obst)
    return lvl


def convert_str_to_list(obj: str) -> {}:
    new_object = obj.replace('<', ',').replace('>', ',').split(',')
    new_object.pop(0)
    keys = new_object[::2]
    values = new_object[1::2]
    values[-1] = values[-1].strip()
    object_dict = dict(zip(keys, values))
    return object_dict
