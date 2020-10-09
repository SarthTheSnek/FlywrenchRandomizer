from .planet import *


def convert_planet_to_dict(file) -> Planet:
    try:
        f = open(file, "r")
    except FileNotFoundError:
        print("Could not open file")
    except Exception:
        print("Something happened")
    else:
        return None

    # Grab line by line and group by level
    f.close()

    return None
