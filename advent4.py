import os


def load_file(file_path):
    if not os.path.exists(file_path):
        print("error the file does not exist. ")
        return None
    else:
        text_file = open(file_path, "r")
        content = text_file.readlines()
        return content


def check_for_vertical(grid, i, j):
    found = 0
    possible_down = (i + 3) >= 0 and (i + 3) < len(grid)
    possible_up = (i - 3) >= 0 and (i - 3) < len(grid)
    # diagonal up
    if possible_up:
        if grid[i - 1][j] == "M" and grid[i - 2][j] == "A" and grid[i - 3][j] == "S":
            found += 1

    # diagonal down
    if possible_down:
        if grid[i + 1][j] == "M" and grid[i + 2][j] == "A" and grid[i + 3][j] == "S":
            found += 1

    return found


def check_for_diagonal(grid, i, j):
    found = 0
    possible_down = (i + 3) >= 0 and (i + 3) < len(grid)
    possible_up = (i - 3) >= 0 and (i - 3) < len(grid)
    possible_left = (j - 3) >= 0 and (j - 3) < len(grid[i])
    possible_right = (j + 3) >= 0 and (j + 3) < len(grid[i])

    if possible_up and possible_left:
        if grid[i - 1][j - 1] == "M" and grid[i - 2][j - 2] == "A" and grid[i - 3][j - 3] == "S":
            found += 1
            # print("found diagonal up left", i, j)

    if possible_up and possible_right:
        # diagonal up right
        if grid[i - 1][j + 1] == "M" and grid[i - 2][j + 2] == "A" and grid[i - 3][j + 3] == "S":
            found += 1
            # print("Found diagional up right", i, j)

    if possible_down and possible_right:
        # diagonal down left
        if grid[i + 1][j + 1] == "M" and grid[i + 2][j + 2] == "A" and grid[i + 3][j + 3] == "S":
            found += 1
            # print("found diagonal down right", i, j)

    if possible_down and possible_left:
        # diagonal down right
        if grid[i + 1][j - 1] == "M" and grid[i + 2][j - 2] == "A" and grid[i + 3][j - 3] == "S":
            found += 1
            # print("foud diagonal down left", i, j)

    return found


def part1(content):
    horizantal_counter = 0
    vertical_counter = 0
    diagonal_counter = 0

    grid = []

    for line in content:
        horizantal_counter += line.count("XMAS")
        horizantal_counter += line.count("SAMX")

    for line in content:
        grid.append(list(line))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                vertical_counter += check_for_vertical(grid, i, j)
                diagonal_counter += check_for_diagonal(grid, i, j)

    return horizantal_counter + vertical_counter + diagonal_counter


def is_cross(grid, i, j):
    possible_down = (i + 1) >= 0 and (i + 1) < len(grid)
    possible_up = (i - 1) >= 0 and (i - 1) < len(grid)
    possible_left = (j - 1) >= 0 and (j - 1) < len(grid[i])
    possible_right = (j + 1) >= 0 and (j + 1) < len(grid[i])

    if (all([possible_up, possible_down, possible_left, possible_right])):
        # up left must be m and down right must be s or m and s
        if not ((upleft(grid, i, j, "M") and downright(grid, i, j, "S")) or (upleft(grid, i, j, "S") and downright(grid, i, j, "M"))):
            return False
        if not ((upright(grid, i, j, "M") and downleft(grid, i, j, "S")) or (upright(grid, i, j, "S") and downleft(grid, i, j, "M"))):
            return False
        return True


def upleft(grid, i, j, check: str):
    return get_char(grid, i, j, ["up", "left"]) == check


def upright(grid, i, j, check):
    return get_char(grid, i, j, ["up", "right"]) == check


def downleft(grid, i, j, check):
    return get_char(grid, i, j, ["down", "left"]) == check


def downright(grid, i, j, check):
    return get_char(grid, i, j, ["down", "right"]) == check


def get_char(grid, i, j, direction: list) -> str:
    if direction[0] == "up":
        i -= 1
    if direction[0] == "down":
        i += 1
    if direction[1] == "left":
        j -= 1
    if direction[1] == "right":
        j += 1
    return grid[i][j]


def part2(content):
    grid = []
    for line in content:
        grid.append(list(line))

    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "A":
                if is_cross(grid, i, j):
                    total += 1

    return total


if __name__ == "__main__":
    content = load_file("advent4.txt")
    # print("Part 1: ", part1(content))
    print("Part 2: ", part2([elem for elem in content]))
