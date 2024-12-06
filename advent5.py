import os


def load_file(file_path):
    if not os.path.exists(file_path):
        print("error the file does not exist. ")
        return None
    else:
        text_file = open(file_path, "r")
        content = text_file.readlines()
        return content


def build_dict_from_list(content) -> dict:
    d = dict()
    for line in content:
        if "|" in line:
            first, second = line.rstrip().split("|")
            second = int(second)
            first = int(first)
            if second not in d:
                d[second] = set()
            d[second].add(first)

    return d


def check_line(line: str, rules: dict) -> bool:
    values = list(map(int, line.rstrip().split(",")))
    # print(values)
    for i, v in enumerate(values):
        if i == 0:
            continue

        if not set(values[:i]).issubset(rules.get(int(v), set())):
            return False
    return True


def fix_incorrect_lines(lines: list, rules: dict):
    fixed_lines = []

    for line in lines:
        values = list(map(int, line.rstrip().split(",")))

        something_changed = True
        while something_changed:
            changed = 0
            for i in range(len(values) - 1):
                if values[i + 1] in rules.get(values[i], set()):
                    tmp1 = values[i]
                    tmp2 = values[i + 1]
                    values[i] = tmp2
                    values[i + 1] = tmp1
                    changed = 1
                    print("switched", tmp1, tmp2)
            if changed == 0:
                something_changed = False
        fixed_lines.append(values)
    return fixed_lines


def get_avg(correct_lines):
    avg_correct = 0

    for line in correct_lines:
        middle = len(line) // 2
        avg_correct += line[middle]

    return avg_correct


def part1(content):
    rules = build_dict_from_list(content)
    correct_lines = []
    incorrect_lines = []

    for l in content:
        if "," in l:
            if check_line(l, rules):
                correct_lines.append(l)
            else:
                incorrect_lines.append(l)

    correct_lines_splitted = []
    for line in correct_lines:
        correct_lines_splitted.append(list(map(int, line.rstrip().split(","))))
    print("part 1", get_avg(correct_lines_splitted))

    fixed = fix_incorrect_lines(incorrect_lines, rules)
    print("part 2", get_avg(fixed))


if __name__ == "__main__":
    content = load_file("advent5.txt")
    part1(content)
    # print("Part 2: ", part2([elem for elem in content]))
