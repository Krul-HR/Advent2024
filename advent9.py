import os


class blokje:
    def __init__(self, id) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"[{self.id}]"

    def __repr__(self) -> str:
        return f"[{self.id}]"


def load_file(file_path):
    if not os.path.exists(file_path):
        print("error the file does not exist. ")
        return None
    else:
        text_file = open(file_path, "r")
        content = text_file.readlines()
        return content


def part1(line):
    # print(line)
    # build the visual represensation
    line = list(map(int, list(line.rstrip().strip())))
    represensation = []
    id_counter = 0

    for i in range(len(line)):
        if i % 2 == 0:
            for i in range(line[i]):
                represensation.append(blokje(id_counter))
            id_counter += 1
        else:
            for i in range(line[i]):
                represensation.append(blokje("."))
    # print(represensation)

    visualized = represensation.copy()

    # sum van alle puntjes
    aantal_puntjes = sum(1 for p in visualized if p.id == ".")

    for i in range(len(visualized) - aantal_puntjes):
        if visualized[i].id == ".":
            last = visualized.pop()
            while last.id == ".":
                last = visualized.pop()
            visualized[i] = last

    # print(visualized)

    # calculate the sum
    result = 0
    for i, v in enumerate(visualized):
        if v.id == ".":
            continue
        result += i * v.id

    print(result)


# doesnt work, don't know, don't care anymore
def part2(line):
    line = list(map(int, list(line.rstrip().strip())))
    represensation = []
    id_counter = 0
    storage = []
    empty_spaces = []

    for i in range(len(line)):
        if i % 2 == 0:
            for _ in range(line[i]):
                represensation.append(blokje(id_counter))
            storage.append((id_counter, line[i]))
            id_counter += 1
        else:
            empty_spaces.append((len(represensation), line[i]))
            for _ in range(line[i]):
                represensation.append(blokje("."))

    print(storage)
    print(empty_spaces)
    print(represensation)

    # Don't go moving the first one
    storage.pop(0)
    # Reverse for easier finding
    storage.reverse()
    # empty_spaces.reverse()

    for id, length in storage:
        # met index om te poppen
        found_spot = find_spot(empty_spaces, length)
        if found_spot > 0:
            # print(f"found a spot for {id} at {found_spot}")
            for i in range(length):
                represensation[found_spot + i] = blokje(id)

            remove_replaced_blokjes(represensation, found_spot + length, id)
        # print(represensation)
        # print(empty_spaces)
        # exit()

        # calculate the sum
    result = 0
    for i, v in enumerate(represensation):
        if v.id == ".":
            continue
        result += i * v.id

    print(result)


def find_spot(empty_spaces, length):
    for index, item in enumerate(empty_spaces):
        position, empty_length = item
        # found a spot
        if length <= empty_length:
            aantal_plekken_over = empty_length - length
            # remove the spot
            empty_spaces.pop(index)
            # places remaining?
            # print(aantal_plekken_over, "pver")
            if aantal_plekken_over > 0:
                # make new spot
                t = (position + length, aantal_plekken_over)
                empty_spaces.insert(index, t)
            return position
    return -1


def remove_replaced_blokjes(line, start_position, id):
    while start_position < len(line):
        # print(f"searching for remove at {start_position}")
        if line[start_position].id == id:
            # print(f"Found a {id} to remove at {start_position}")
            line.pop(start_position)
            line.insert(start_position, blokje("."))
            start_position -= 1
        start_position += 1


if __name__ == "__main__":
    content = load_file("advent9.txt")
    # part1(content[0])
    part2(content[0])

    # print("Part 2: ", part2([elem for elem in content]))
