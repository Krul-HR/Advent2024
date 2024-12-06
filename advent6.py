import os
# import time
from datetime import datetime
# clear = lambda: os.system('cls')


def load_file(file_path):
    if not os.path.exists(file_path):
        print("error the file does not exist. ")
        return None
    else:
        text_file = open(file_path, "r")
        content = text_file.readlines()
        return content


def find_gaurd(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return i, j
    return None, None


def printgrid(grid):
    # clear()
    # for line in grid:
    #     print(" ".join(line))
    # time.sleep(0.01)
    pass


def move(grid, i, j, direction):
    possible_down = (i + 1) >= 0 and (i + 1) < len(grid)
    possible_up = (i - 1) >= 0 and (i - 1) < len(grid)
    possible_left = (j - 1) >= 0 and (j - 1) < len(grid[i])
    possible_right = (j + 1) >= 0 and (j + 1) < len(grid[i])

    if direction == "up" and possible_up:
        return i - 1, j
    if direction == "down" and possible_down:
        return i + 1, j
    if direction == "left" and possible_left:
        return i, j - 1
    if direction == "right" and possible_right:
        return i, j + 1

    # not possible to move, set cross and exit
    grid[i][j] = "X"
    # printgrid(grid)
    return False


def get_facing_char(direction):
    if direction == "up":
        return "^"
    if direction == "down":
        return "/"
    if direction == "left":
        return "<"
    if direction == "right":
        return ">"


def change_facing(direction):
    if direction == "up":
        return "right"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"
    if direction == "right":
        return "down"


def find_next_obstacle(grid, i, j, facing):

    history = set()

    while True:
        history.add((i, j))
        # grid[i][j] = "X"
        new_position = move(grid, i, j, facing)
        if new_position != False:
            old_position = i, j
            i, j = new_position
        else:
            break
        if grid[i][j] != "#":
            grid[i][j] = get_facing_char(facing)
        else:
            i, j = old_position
            facing = change_facing(facing)
        # printgrid(grid)

    return history


def reset_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                # print("should have resetted")
                grid[i][j] == "."


def find_next_obstacle_part2(grid, i, j, facing):

    starting_i = i
    starting_j = j
    starting_facing = facing
    history = []

    # print("starting", starting_i, starting_j, facing)

    while True:
        history.append((i, j, facing))
        # grid[i][j] = "X"
        new_position = move(grid, i, j, facing)
        if new_position != False:
            old_position = i, j
            i, j = new_position

        else:
            # print("out of bounds")
            # reset_grid(grid)
            break

        if grid[i][j] != "#" and grid[i][j] != "0":
            # grid[i][j] = get_facing_char(facing)
            pass
        else:
            i, j = old_position
            facing = change_facing(facing)
        # printgrid(grid)
        if (i, j, facing) in history:
            # print("looped!")
            return True

    return False


def part1(grid):
    position_i = 0
    position_j = 0
    facing = "up"

    position_i, position_j = find_gaurd(grid)
    print("Gaurd found at: ", position_i, position_j)

    find_next_obstacle(grid, position_i, position_j, facing)

    count_x = 0
    for line in grid:
        for item in line:
            if item == "X":
                count_x += 1

    return count_x


def part2(grid):
    position_i = 0
    position_j = 0
    facing = "up"

    position_i, position_j = find_gaurd(grid)
    # print("Gaurd found at: ", position_i, position_j)

    possible_block = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # reset_grid(grid)
            if grid[i][j] != "^" and grid[i][j] != "#":
                grid[i][j] = "0"
                if find_next_obstacle_part2(grid, position_i, position_j, facing):
                    print("found a loop at ", i, j)
                    possible_block += 1
                else:
                    print("no loop at ", i, j)
                    pass
                grid[i][j] = "."

    print(possible_block)


if __name__ == "__main__":
    # content = load_file("advent6.txt")
    # splitted = []
    # for line in content:
    #     splitted.append(list(line.rstrip()))
    # print("Part 1: ", part1(splitted))

    content = load_file("advent6.txt")
    splitted = []
    for line in content:
        splitted.append(list(line.rstrip()))
    start_time = datetime.now()
    print("Part 2: ", part2(splitted))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
