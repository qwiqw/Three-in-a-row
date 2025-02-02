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
    if new[1] == 5:
        if (level[new[1]][new[0]] == level[new[1] - 1][new[0]] and
                level[new[1]][new[0]] == level[new[1] - 2][new[0]]):
            symbol_new1 = random.choice(['.', '@', '#', '*'])
            symbol_new2 = random.choice(['.', '@', '#', '*'])
            symbol_new3 = random.choice(['.', '@', '#', '*'])
            symbol_level1 = level[new[1] - 1][new[0]]
            symbol_level2 = level[new[1] - 2][new[0]]
            symbol_level3 = level[new[1] - 3][new[0]]
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
