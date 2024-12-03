import os
import re


def load_file(file_path):
    if not os.path.exists(file_path):
        print("error the file does not exist. ")
        return None
    else:
        text_file = open(file_path, "r")
        content = text_file.readlines()
        return content


def line_counter(one_line) -> int:
    regex = "mul\([0-9]+,[0-9]+\)"
    total = 0
    matches = re.findall(regex, one_line)
    for match in matches:
        first_four_removed = match[4:]
        last_removed = first_four_removed[:-1]
        g1, g2 = last_removed.split(",")
        # print(g1, g2)
        total += int(g1) * int(g2)
    return total


def part1(content):
    total = 0

    for line in content:
        total += line_counter(line)
    return total


def part2(content):
    total = 0
    for i in range(len(content)):
        # split on the don't() and do()
        content[i] = content[i].replace("don't()", "SPLITTERN")
        content[i] = content[i].replace("do()", "SPLITTERY")
        splitted = content[i].split("SPLITTER")

        # if last item start with N, add it to the next line
        if splitted[-1].startswith("N") and i < len(content) - 1:
            content[i + 1] = "SPLITTERN" + content[i + 1]

        # remove the dont()s
        splitted = list(filter(lambda x: not x.startswith("N"), splitted))

        # join back and calculate
        back_together = "".join(splitted)
        line_total = line_counter(back_together)
        total += line_total

    return total


if __name__ == "__main__":
    content = load_file("advent3.txt")
    # print(content)

    print("Part 1: ", part1(content))
    print("Part 2: ", part2([elem for elem in content]))
