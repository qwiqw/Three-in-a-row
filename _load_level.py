def load_level(filename):
    filename = "data/maps/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    return list(level_map)
