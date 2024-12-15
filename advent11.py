import os
from collections import Counter


def load_file(file_path):
    if not os.path.exists(file_path):
        print("error the file does not exist. ")
        return None
    else:
        text_file = open(file_path, "r")
        content = text_file.readlines()
        return content


def part1_one_blink(line):
    new_line = []
    for item in line:
        if item == 0:
            new_line.append(1)
        elif len(str(item)) % 2 == 0:
            str_item = str(item)
            halfway = len(str_item) // 2
            new_line.append(int(str_item[:halfway]))
            new_line.append(int(str_item[halfway:]))
        else:
            new_line.append(item * 2024)
    return new_line


def part1(line):

    for _ in range(25):
        line = part1_one_blink(line)
        # print(line)
        print(f"calculated blink {_}")
    print(len(line))


def part2(line):
    d = Counter(line)
    print(d)
    for _ in range(75):
        d = part2_one_blink(d)
        # print(line)
        print(f"calculated blink {_+1}")
        # print(d)
    print(sum(d.values()))


def part2_one_blink(line: dict):
    new_dict = dict()
    for k, v in line.items():
        if k == 0:
            new_dict[1] = new_dict.get(1, 0) + v
        elif len(str(k)) % 2 == 0:
            str_item = str(k)
            halfway = len(str_item) // 2
            left = int(str_item[:halfway])
            right = int(str_item[halfway:])
            new_dict[left] = new_dict.get(left, 0) + v
            new_dict[right] = new_dict.get(right, 0) + v
        else:
            newkey = k * 2024
            new_dict[newkey] = new_dict.get(newkey, 0) + v
    return new_dict


if __name__ == "__main__":
    content = load_file("advent11.txt")
    line = [int(x) for x in content[0].rstrip().split()]
    print(line)
    part2(line)
    # part1(content[0])
    # print("Part 2: ", part2([elem for elem in content]))
