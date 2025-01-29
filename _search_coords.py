from _generate_level import left, top, cell_size


def get_cell(mouse_pos):
    x, y = mouse_pos
    return ((x - left) // cell_size, (y - top) // cell_size)