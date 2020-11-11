from os import path
from logic import settings


def tofile(planets: [], config: settings.Settings):
    level_directory = path.join(config.directory, "ReadOnlyFiles")
    for planet in planets:
        try:
            file = open(path.join(level_directory, planet.name + ".planet"), "w")
            file.write(planet.to_gm() + '\n')
            for level in planet.levels:
                file.write(level.to_gm() + '\n')
                for wall in level.walls:
                    file.write(wall.to_gm() + '\n')
                for obstacle in level.inside:
                    file.write(obstacle.to_gm() + '\n')
            file.close()
        except Exception as err:
            print("Something went wrong")
            print(err)
