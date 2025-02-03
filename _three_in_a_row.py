import random


def three_in_a_row(old, new, level):
    if new[0] == 6:
        if (level[new[1]][new[0]] == level[new[1]][new[0] + 1] and
                level[new[1]][new[0]] == level[new[1]][new[0] + 2]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            for i in range(new[1]):
                symbol_level1 = level[new[1] - 1 - i][new[0]]
                symbol_level2 = level[new[1] - 1 - i][new[0] + 1]
                symbol_level3 = level[new[1] - 1 - i][new[0] + 2]

                level[new[1] - i] = level[new[1] - i][:6] + symbol_level1 + symbol_level2 + symbol_level3
            level[0] = level[0][:6] + symbol_new1 + symbol_new2 + symbol_new3
    if new[0] == 2:
        if (level[new[1]][new[0]] == level[new[1]][new[0] - 1] and
                level[new[1]][new[0]] == level[new[1]][new[0] - 2]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            for i in range(new[1]):
                symbol_level1 = level[new[1] - 1 - i][new[0]]
                symbol_level2 = level[new[1] - 1 - i][new[0] - 1]
                symbol_level3 = level[new[1] - 1 - i][new[0] - 2]

                level[new[1] - i] = symbol_level3 + symbol_level2 + symbol_level1 + level[new[1] - i][3:]
            level[0] = symbol_new1 + symbol_new2 + symbol_new3 + level[0][3:]
    if new[0] < 6:
        if (level[new[1]][new[0]] == level[new[1]][new[0] + 1] and
                level[new[1]][new[0]] == level[new[1]][new[0] + 2]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])

            for i in range(new[1]):
                symbol_level1 = level[new[1] - 1 - i][new[0]]
                symbol_level2 = level[new[1] - 1 - i][new[0] + 1]
                symbol_level3 = level[new[1] - 1 - i][new[0] + 2]

                level[new[1] - i] = (level[new[1] - i][:new[0]] + symbol_level1 +
                                     symbol_level2 + symbol_level3 + level[new[1] - i][new[0] + 3:])
            level[0] = (level[0][:new[0]] + symbol_new1 +
                        symbol_new2 + symbol_new3 + level[0][new[0] + 3:])
    if new[0] > 2:
        if (level[new[1]][new[0]] == level[new[1]][new[0] - 1] and
                level[new[1]][new[0]] == level[new[1]][new[0] - 2]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])

            for i in range(new[1]):
                symbol_level1 = level[new[1] - 1 - i][new[0]]
                symbol_level2 = level[new[1] - 1 - i][new[0] - 1]
                symbol_level3 = level[new[1] - 1 - i][new[0] - 2]

                level[new[1] - i] = (level[new[1] - i][:new[0] - 2] + symbol_level3 + symbol_level2
                                     + symbol_level1 + level[new[1] - i][new[0] + 1:])

            level[0] = level[0][:new[0] - 2] + symbol_new1 + symbol_new2 + symbol_new3 + level[0][new[0] + 1:]
    if 1 <= new[0] <= 7:
        if (level[new[1]][new[0]] == level[new[1]][new[0] - 1] and
                level[new[1]][new[0]] == level[new[1]][new[0] + 1]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])

            for i in range(new[1]):
                symbol_level1 = level[new[1] - 1 - i][new[0] - 1]
                symbol_level2 = level[new[1] - 1 - i][new[0]]
                symbol_level3 = level[new[1] - 1 - i][new[0] + 1]

                level[new[1] - i] = (level[new[1] - i][:new[0] - 1] + symbol_level1 +
                                     symbol_level2 + symbol_level3 + level[new[1] - i][new[0] + 2:])
            level[0] = (level[0][:new[0] - 1] + symbol_new1 +
                        symbol_new2 + symbol_new3 + level[0][new[0] + 2:])
    if new[1] == 2:
        if (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_new1 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_new2 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_new3 + level[new[1]][new[0] + 1:]

    #ошибка была вот здесь в new[1] == 5 в sym_level

    if new[1] == 5:
        if (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            # вот это уже исправлено!!!
            symbol_level1 = level[new[1] - 5][new[0]]
            symbol_level2 = level[new[1] - 4][new[0]]
            symbol_level3 = level[new[1] - 3][new[0]]
            #
            level[new[1]] = level[new[1]][:new[0]] + symbol_level3 + level[new[1]][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level2 + level[new[1] - 1][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_level1 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_new1 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_new2 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 5] = level[new[1] - 5][:new[0]] + symbol_new3 + level[new[1] - 5][new[0] + 1:]
    if new[1] == 8:
        if (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 3][new[0]]
            symbol_level2 = level[new[1] - 4][new[0]]
            symbol_level3 = level[new[1] - 5][new[0]]
            symbol_level4 = level[new[1] - 6][new[0]]
            symbol_level5 = level[new[1] - 7][new[0]]
            symbol_level6 = level[new[1] - 8][new[0]]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level1 + level[new[1]][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level2 + level[new[1] - 1][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_level3 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_level4 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_level5 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 5] = level[new[1] - 5][:new[0]] + symbol_level6 + level[new[1] - 5][new[0] + 1:]
            level[new[1] - 6] = level[new[1] - 6][:new[0]] + symbol_new1 + level[new[1] - 6][new[0] + 1:]
            level[new[1] - 7] = level[new[1] - 7][:new[0]] + symbol_new2 + level[new[1] - 7][new[0] + 1:]
            level[new[1] - 8] = level[new[1] - 8][:new[0]] + symbol_new3 + level[new[1] - 8][new[0] + 1:]
    if new[1] == 0:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] + 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            level[new[1] + 2] = level[new[1] + 2][:new[0]] + symbol_new1 + level[new[1] + 2][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_new2 + level[new[1] + 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_new3 + level[new[1]][new[0] + 1:]
    if new[1] == 3:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] + 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 3][new[0]]
            symbol_level2 = level[new[1] - 2][new[0]]
            symbol_level3 = level[new[1] - 1][new[0]]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_new1 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_new2 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_new3 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level1 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level2 + level[new[1] + 1][new[0] + 1:]
            level[new[1] + 2] = level[new[1] + 2][:new[0]] + symbol_level3 + level[new[1] + 2][new[0] + 1:]
    if new[1] == 6:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] + 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 6][new[0]]
            symbol_level2 = level[new[1] - 5][new[0]]
            symbol_level3 = level[new[1] - 4][new[0]]
            symbol_level4 = level[new[1] - 3][new[0]]
            symbol_level5 = level[new[1] - 2][new[0]]
            symbol_level6 = level[new[1] - 1][new[0]]
            level[new[1] - 6] = level[new[1] - 6][:new[0]] + symbol_new1 + level[new[1] - 6][new[0] + 1:]
            level[new[1] - 5] = level[new[1] - 5][:new[0]] + symbol_new2 + level[new[1] - 5][new[0] + 1:]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_new3 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_level1 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_level2 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level3 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level4 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level5 + level[new[1] + 1][new[0] + 1:]
            level[new[1] + 2] = level[new[1] + 2][:new[0]] + symbol_level6 + level[new[1] + 2][new[0] + 1:]

    #NEW

    if new[1] == 1:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 1][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_new1 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_new2 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_new3 + level[new[1] + 1][new[0] + 1:]
    if new[1] == 2:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 1][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 2][new[0]]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_new1 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_new2 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_new3 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level1 + level[new[1] + 1][new[0] + 1:]
    if new[1] == 3:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 1][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 2][new[0]]
            symbol_level2 = level[new[1] - 3][new[0]]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_new1 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_new2 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_new3 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level2 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level1 + level[new[1] + 1][new[0] + 1:]
    if new[1] == 4:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 1][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 2][new[0]]
            symbol_level2 = level[new[1] - 3][new[0]]
            symbol_level3 = level[new[1] - 4][new[0]]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_new1 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_new2 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_new3 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level3 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level2 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level1 + level[new[1] + 1][new[0] + 1:]
    if new[1] == 5:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 1][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 2][new[0]]
            symbol_level2 = level[new[1] - 3][new[0]]
            symbol_level3 = level[new[1] - 4][new[0]]
            symbol_level4 = level[new[1] - 5][new[0]]
            level[new[1] - 5] = level[new[1] - 5][:new[0]] + symbol_new1 + level[new[1] - 5][new[0] + 1:]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_new2 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_new3 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_level4 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level3 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level2 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level1 + level[new[1] + 1][new[0] + 1:]
    if new[1] == 6:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 1][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 2][new[0]]
            symbol_level2 = level[new[1] - 3][new[0]]
            symbol_level3 = level[new[1] - 4][new[0]]
            symbol_level4 = level[new[1] - 5][new[0]]
            symbol_level5 = level[new[1] - 6][new[0]]
            level[new[1] - 6] = level[new[1] - 6][:new[0]] + symbol_new1 + level[new[1] - 6][new[0] + 1:]
            level[new[1] - 5] = level[new[1] - 5][:new[0]] + symbol_new2 + level[new[1] - 5][new[0] + 1:]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_new3 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_level5 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_level4 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level3 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level2 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level1 + level[new[1] + 1][new[0] + 1:]
    if new[1] == 7:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 1][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 2][new[0]]
            symbol_level2 = level[new[1] - 3][new[0]]
            symbol_level3 = level[new[1] - 4][new[0]]
            symbol_level4 = level[new[1] - 5][new[0]]
            symbol_level5 = level[new[1] - 6][new[0]]
            symbol_level6 = level[new[1] - 7][new[0]]
            level[new[1] - 7] = level[new[1] - 7][:new[0]] + symbol_new1 + level[new[1] - 7][new[0] + 1:]
            level[new[1] - 6] = level[new[1] - 6][:new[0]] + symbol_new2 + level[new[1] - 6][new[0] + 1:]
            level[new[1] - 5] = level[new[1] - 5][:new[0]] + symbol_new3 + level[new[1] - 5][new[0] + 1:]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_level6 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_level5 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_level4 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level3 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level2 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level1 + level[new[1] + 1][new[0] + 1:]
    if new[1] == 1:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] + 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 1][new[0]]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_new1 + level[new[1] - 1][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_new2 + level[new[1] + 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_new3 + level[new[1]][new[0] + 1:]
            level[new[1] + 2] = level[new[1] + 2][:new[0]] + symbol_level1 + level[new[1] + 2][new[0] + 1:]
    if new[1] == 2:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] + 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 1][new[0]]
            symbol_level2 = level[new[1] - 2][new[0]]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_new1 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_new2 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_new3 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level2 + level[new[1] + 1][new[0] + 1:]
            level[new[1] + 2] = level[new[1] + 2][:new[0]] + symbol_level1 + level[new[1] + 2][new[0] + 1:]
    if new[1] == 4:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] + 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 1][new[0]]
            symbol_level2 = level[new[1] - 2][new[0]]
            symbol_level3 = level[new[1] - 3][new[0]]
            symbol_level4 = level[new[1] - 4][new[0]]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_new1 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_new2 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_new3 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level4 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level3 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level2 + level[new[1] + 1][new[0] + 1:]
            level[new[1] + 2] = level[new[1] + 2][:new[0]] + symbol_level1 + level[new[1] + 2][new[0] + 1:]
    if new[1] == 5:
        if (level[new[1]][new[0]] == level[new[1] + 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] + 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 1][new[0]]
            symbol_level2 = level[new[1] - 2][new[0]]
            symbol_level3 = level[new[1] - 3][new[0]]
            symbol_level4 = level[new[1] - 4][new[0]]
            symbol_level5 = level[new[1] - 5][new[0]]
            level[new[1] - 5] = level[new[1] - 5][:new[0]] + symbol_new1 + level[new[1] - 5][new[0] + 1:]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_new2 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_new3 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_level5 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level4 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level3 + level[new[1]][new[0] + 1:]
            level[new[1] + 1] = level[new[1] + 1][:new[0]] + symbol_level2 + level[new[1] + 1][new[0] + 1:]
            level[new[1] + 2] = level[new[1] + 2][:new[0]] + symbol_level1 + level[new[1] + 2][new[0] + 1:]
    if new[1] == 3:
        if (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 3][new[0]]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_new1 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_new2 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_new3 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level1 + level[new[1]][new[0] + 1:]
    if new[1] == 4:
        if (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 3][new[0]]
            symbol_level2 = level[new[1] - 4][new[0]]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_new1 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_new2 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_new3 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level2 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level1 + level[new[1]][new[0] + 1:]
    if new[1] == 6:
        if (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 3][new[0]]
            symbol_level2 = level[new[1] - 4][new[0]]
            symbol_level3 = level[new[1] - 5][new[0]]
            symbol_level4 = level[new[1] - 6][new[0]]
            level[new[1] - 6] = level[new[1] - 6][:new[0]] + symbol_new1 + level[new[1] - 6][new[0] + 1:]
            level[new[1] - 5] = level[new[1] - 5][:new[0]] + symbol_new2 + level[new[1] - 5][new[0] + 1:]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_new3 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_level4 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_level3 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level2 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level1 + level[new[1]][new[0] + 1:]
    if new[1] == 7:
        if (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 3][new[0]]
            symbol_level2 = level[new[1] - 4][new[0]]
            symbol_level3 = level[new[1] - 5][new[0]]
            symbol_level4 = level[new[1] - 6][new[0]]
            symbol_level5 = level[new[1] - 7][new[0]]
            level[new[1] - 7] = level[new[1] - 7][:new[0]] + symbol_new1 + level[new[1] - 7][new[0] + 1:]
            level[new[1] - 6] = level[new[1] - 6][:new[0]] + symbol_new2 + level[new[1] - 6][new[0] + 1:]
            level[new[1] - 5] = level[new[1] - 5][:new[0]] + symbol_new3 + level[new[1] - 5][new[0] + 1:]
            level[new[1] - 4] = level[new[1] - 4][:new[0]] + symbol_level5 + level[new[1] - 4][new[0] + 1:]
            level[new[1] - 3] = level[new[1] - 3][:new[0]] + symbol_level4 + level[new[1] - 3][new[0] + 1:]
            level[new[1] - 2] = level[new[1] - 2][:new[0]] + symbol_level3 + level[new[1] - 2][new[0] + 1:]
            level[new[1] - 1] = level[new[1] - 1][:new[0]] + symbol_level2 + level[new[1] - 1][new[0] + 1:]
            level[new[1]] = level[new[1]][:new[0]] + symbol_level1 + level[new[1]][new[0] + 1:]

    '''////////////////////////////////////////////////////////////////////////////////////////////////////'''

    if old[0] == 6:
        if (level[old[1]][old[0]] == level[old[1]][old[0] + 1] and
                level[old[1]][old[0]] == level[old[1]][old[0] + 2]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])
            for i in range(old[1]):
                symbol_level1 = level[old[1] - 1 - i][old[0]]
                symbol_level2 = level[old[1] - 1 - i][old[0] + 1]
                symbol_level3 = level[old[1] - 1 - i][old[0] + 2]

                level[old[1] - i] = level[old[1] - i][:6] + symbol_level1 + symbol_level2 + symbol_level3
            level[0] = level[0][:6] + symbol_old1 + symbol_old2 + symbol_old3
    if old[0] == 2:
        if (level[old[1]][old[0]] == level[old[1]][old[0] - 1] and
                level[old[1]][old[0]] == level[old[1]][old[0] - 2]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])
            for i in range(old[1]):
                symbol_level1 = level[old[1] - 1 - i][old[0]]
                symbol_level2 = level[old[1] - 1 - i][old[0] - 1]
                symbol_level3 = level[old[1] - 1 - i][old[0] - 2]

                level[old[1] - i] = symbol_level3 + symbol_level2 + symbol_level1 + level[old[1] - i][3:]
            level[0] = symbol_old1 + symbol_old2 + symbol_old3 + level[0][3:]
    if old[0] < 6:
        if (level[old[1]][old[0]] == level[old[1]][old[0] + 1] and
                level[old[1]][old[0]] == level[old[1]][old[0] + 2]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])

            for i in range(old[1]):
                symbol_level1 = level[old[1] - 1 - i][old[0]]
                symbol_level2 = level[old[1] - 1 - i][old[0] + 1]
                symbol_level3 = level[old[1] - 1 - i][old[0] + 2]

                level[old[1] - i] = (level[old[1] - i][:old[0]] + symbol_level1 +
                                     symbol_level2 + symbol_level3 + level[old[1] - i][old[0] + 3:])
            level[0] = (level[0][:old[0]] + symbol_old1 +
                        symbol_old2 + symbol_old3 + level[0][old[0] + 3:])
    if old[0] > 2:
        if (level[old[1]][old[0]] == level[old[1]][old[0] - 1] and
                level[old[1]][old[0]] == level[old[1]][old[0] - 2]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])

            for i in range(old[1]):
                symbol_level1 = level[old[1] - 1 - i][old[0]]
                symbol_level2 = level[old[1] - 1 - i][old[0] - 1]
                symbol_level3 = level[old[1] - 1 - i][old[0] - 2]

                level[old[1] - i] = (level[old[1] - i][:old[0] - 2] + symbol_level3 + symbol_level2
                                     + symbol_level1 + level[old[1] - i][old[0] + 1:])

            level[0] = level[0][:old[0] - 2] + symbol_old1 + symbol_old2 + symbol_old3 + level[0][old[0] + 1:]
    if 1 <= old[0] <= 7:
        if (level[old[1]][old[0]] == level[old[1]][old[0] - 1] and
                level[old[1]][old[0]] == level[old[1]][old[0] + 1]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])

            for i in range(old[1]):
                symbol_level1 = level[old[1] - 1 - i][old[0] - 1]
                symbol_level2 = level[old[1] - 1 - i][old[0]]
                symbol_level3 = level[old[1] - 1 - i][old[0] + 1]

                level[old[1] - i] = (level[old[1] - i][:old[0] - 1] + symbol_level1 +
                                     symbol_level2 + symbol_level3 + level[old[1] - i][old[0] + 2:])
            level[0] = (level[0][:old[0] - 1] + symbol_old1 +
                        symbol_old2 + symbol_old3 + level[0][old[0] + 2:])
    if old[1] == 2:
        if (level[old[1]][old[0]] == level[old[1] - 1][old[0]] and
                level[old[1]][old[0]] == level[old[1] - 2][old[0]]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])
            level[old[1] - 2] = level[old[1] - 2][:old[0]] + symbol_old1 + level[old[1] - 2][old[0] + 1:]
            level[old[1] - 1] = level[old[1] - 1][:old[0]] + symbol_old2 + level[old[1] - 1][old[0] + 1:]
            level[old[1]] = level[old[1]][:old[0]] + symbol_old3 + level[old[1]][old[0] + 1:]
    if old[1] == 5:
        if (level[old[1]][old[0]] == level[old[1] - 1][old[0]] and
                level[old[1]][old[0]] == level[old[1] - 2][old[0]]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[old[1] - 1][old[0]]
            symbol_level2 = level[old[1] - 2][old[0]]
            symbol_level3 = level[old[1] - 3][old[0]]
            level[old[1]] = level[old[1]][:old[0]] + symbol_level3 + level[old[1]][old[0] + 1:]
            level[old[1] - 1] = level[old[1] - 1][:old[0]] + symbol_level2 + level[old[1] - 1][old[0] + 1:]
            level[old[1] - 2] = level[old[1] - 2][:old[0]] + symbol_level1 + level[old[1] - 2][old[0] + 1:]
            level[old[1] - 3] = level[old[1] - 3][:old[0]] + symbol_old1 + level[old[1] - 3][old[0] + 1:]
            level[old[1] - 4] = level[old[1] - 4][:old[0]] + symbol_old2 + level[old[1] - 4][old[0] + 1:]
            level[old[1] - 5] = level[old[1] - 5][:old[0]] + symbol_old3 + level[old[1] - 5][old[0] + 1:]
    if old[1] == 8:
        if (level[old[1]][old[0]] == level[old[1] - 1][old[0]] and
                level[old[1]][old[0]] == level[old[1] - 2][old[0]]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[old[1] - 3][old[0]]
            symbol_level2 = level[old[1] - 4][old[0]]
            symbol_level3 = level[old[1] - 5][old[0]]
            symbol_level4 = level[old[1] - 6][old[0]]
            symbol_level5 = level[old[1] - 7][old[0]]
            symbol_level6 = level[old[1] - 8][old[0]]
            level[old[1]] = level[old[1]][:old[0]] + symbol_level1 + level[old[1]][old[0] + 1:]
            level[old[1] - 1] = level[old[1] - 1][:old[0]] + symbol_level2 + level[old[1] - 1][old[0] + 1:]
            level[old[1] - 2] = level[old[1] - 2][:old[0]] + symbol_level3 + level[old[1] - 2][old[0] + 1:]
            level[old[1] - 3] = level[old[1] - 3][:old[0]] + symbol_level4 + level[old[1] - 3][old[0] + 1:]
            level[old[1] - 4] = level[old[1] - 4][:old[0]] + symbol_level5 + level[old[1] - 4][old[0] + 1:]
            level[old[1] - 5] = level[old[1] - 5][:old[0]] + symbol_level6 + level[old[1] - 5][old[0] + 1:]
            level[old[1] - 6] = level[old[1] - 6][:old[0]] + symbol_old1 + level[old[1] - 6][old[0] + 1:]
            level[old[1] - 7] = level[old[1] - 7][:old[0]] + symbol_old2 + level[old[1] - 7][old[0] + 1:]
            level[old[1] - 8] = level[old[1] - 8][:old[0]] + symbol_old3 + level[old[1] - 8][old[0] + 1:]
    if old[1] == 0:
        if (level[old[1]][old[0]] == level[old[1] + 1][old[0]] and
                level[old[1]][old[0]] == level[old[1] + 2][old[0]]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])
            level[old[1] + 2] = level[old[1] + 2][:old[0]] + symbol_old1 + level[old[1] + 2][old[0] + 1:]
            level[old[1] + 1] = level[old[1] + 1][:old[0]] + symbol_old2 + level[old[1] + 1][old[0] + 1:]
            level[old[1]] = level[old[1]][:old[0]] + symbol_old3 + level[old[1]][old[0] + 1:]
    if old[1] == 3:
        if (level[old[1]][old[0]] == level[old[1] + 1][old[0]] and
                level[old[1]][old[0]] == level[old[1] + 2][old[0]]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[old[1] - 3][old[0]]
            symbol_level2 = level[old[1] - 2][old[0]]
            symbol_level3 = level[old[1] - 1][old[0]]
            level[old[1] - 3] = level[old[1] - 3][:old[0]] + symbol_old1 + level[old[1] - 3][old[0] + 1:]
            level[old[1] - 2] = level[old[1] - 2][:old[0]] + symbol_old2 + level[old[1] - 2][old[0] + 1:]
            level[old[1] - 1] = level[old[1] - 1][:old[0]] + symbol_old3 + level[old[1] - 1][old[0] + 1:]
            level[old[1]] = level[old[1]][:old[0]] + symbol_level1 + level[old[1]][old[0] + 1:]
            level[old[1] + 1] = level[old[1] + 1][:old[0]] + symbol_level2 + level[old[1] + 1][old[0] + 1:]
            level[old[1] + 2] = level[old[1] + 2][:old[0]] + symbol_level3 + level[old[1] + 2][old[0] + 1:]
    if old[1] == 6:
        if (level[old[1]][old[0]] == level[old[1] + 1][old[0]] and
                level[old[1]][old[0]] == level[old[1] + 2][old[0]]):
            symbol_old1 = random.choice(['.', '@', '#', '*'])
            symbol_old2 = random.choice(['.', '@', '#', '*'])
            symbol_old3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[old[1] - 6][old[0]]
            symbol_level2 = level[old[1] - 5][old[0]]
            symbol_level3 = level[old[1] - 4][old[0]]
            symbol_level4 = level[old[1] - 3][old[0]]
            symbol_level5 = level[old[1] - 2][old[0]]
            symbol_level6 = level[old[1] - 1][old[0]]
            level[old[1] - 6] = level[old[1] - 6][:old[0]] + symbol_old1 + level[old[1] - 6][old[0] + 1:]
            level[old[1] - 5] = level[old[1] - 5][:old[0]] + symbol_old2 + level[old[1] - 5][old[0] + 1:]
            level[old[1] - 4] = level[old[1] - 4][:old[0]] + symbol_old3 + level[old[1] - 4][old[0] + 1:]
            level[old[1] - 3] = level[old[1] - 3][:old[0]] + symbol_level1 + level[old[1] - 3][old[0] + 1:]
            level[old[1] - 2] = level[old[1] - 2][:old[0]] + symbol_level2 + level[old[1] - 2][old[0] + 1:]
            level[old[1] - 1] = level[old[1] - 1][:old[0]] + symbol_level3 + level[old[1] - 1][old[0] + 1:]
            level[old[1]] = level[old[1]][:old[0]] + symbol_level4 + level[old[1]][old[0] + 1:]
            level[old[1] + 1] = level[old[1] + 1][:old[0]] + symbol_level5 + level[old[1] + 1][old[0] + 1:]
            level[old[1] + 2] = level[old[1] + 2][:old[0]] + symbol_level6 + level[old[1] + 2][old[0] + 1:]
