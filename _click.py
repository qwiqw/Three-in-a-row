from _check import check

count_mouves = 0


def movement(old, new, level):
    global count_mouves
    if (old[0] < 0 or old[0] > 8 or old[1] < 0 or old[1] > 8
            or new[0] < 0 or new[0] > 8 or new[1] < 0 or new[1] > 8):
        return count_mouves

    if level[old[1]][old[0]] == level[new[1]][new[0]]:
        return count_mouves

    if old[0] == new[0] + 1 and old[1] == new[1]:
        level[old[1]] = (level[old[1]][:(new[0])] + level[old[1]][old[0]]
                         + level[new[1]][new[0]] + level[old[1]][(new[0] + 2):])
        count_mouves += 1

    if old[0] == new[0] - 1 and old[1] == new[1]:
        level[old[1]] = (level[old[1]][:(old[0])] + level[new[1]][new[0]] + level[old[1]][old[0]]
                         + level[old[1]][(old[0] + 2):])
        count_mouves += 1

    if old[1] == new[1] - 1 and old[0] == new[0] or old[1] == new[1] + 1 and old[0] == new[0]:
        oldfish = level[old[1]][old[0]]
        level[old[1]] = level[old[1]][:(old[0])] + level[new[1]][new[0]] + level[old[1]][(old[0] + 1):]
        level[new[1]] = level[new[1]][:(new[0])] + oldfish + level[new[1]][(new[0] + 1):]
        count_mouves += 1
    check(level)
    return count_mouves
