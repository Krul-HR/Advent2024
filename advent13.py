import os


def load_file(file_path):
    if not os.path.exists(file_path):
        print("error the file does not exist. ")
        return None
    else:
        text_file = open(file_path, "r")
        content = text_file.readlines()
        return content


def part2_find_min_cost(a: tuple, b: tuple, find: tuple):

    # b = (Xtot/26-Ytot/66)/(67/26-21/66)
    # a = (Xtot - 67*b)/26
    clicksb = (find[0] / a[0] - find[1] / a[1]) / \
        (b[0] / a[0] - b[1] / a[1])
    clicksa = (find[0] - b[0] * clicksb) / a[0]

    # if clicksa.is_integer() and clicksb.is_integer():
    #     # valid!
    #     x_a = clicksa * a[0]
    #     y_a = clicksa * a[1]
    #     x_b = clicksb * b[0]
    #     y_b = clicksb * b[1]

    #     x = x_a + x_b
    #     y = y_a + y_b
    #     print(clicksa, clicksb, "valid")
    #     if x == find[0] and y == find[1]:
    #         print("calculation check valid")
    #         return (clicksa * 3) + clicksb
    #     else:
    #         print("calculation check FAILED")

    # else:
    #     epsilon = 0.00001
    #     if abs(round(clicksa) - clicksa) < epsilon or abs(round(clicksb) - clicksb) < epsilon:
    #         clicksa = round(clicksa)
    #         clicksb = round(clicksb)
    #         x_a = clicksa * a[0]
    #         y_a = clicksa * a[1]
    #         x_b = clicksb * b[0]
    #         y_b = clicksb * b[1]

    #         x = x_a + x_b
    #         y = y_a + y_b
    #         print(clicksa, clicksb, "valid")
    #         if x == find[0] and y == find[1]:
    #             print("correction calculation check valid")
    #             return (clicksa * 3) + clicksb
    #         else:
    #             print("correiotn calculation check FAILED")
    #         print(clicksa, clicksb, "corrected")

    #     print(clicksa, clicksb, "not valid")

    clicksa = round(clicksa)
    clicksb = round(clicksb)
    x_a = clicksa * a[0]
    y_a = clicksa * a[1]
    x_b = clicksb * b[0]
    y_b = clicksb * b[1]

    x = x_a + x_b
    y = y_a + y_b
    print(clicksa, clicksb, "check")
    if x == find[0] and y == find[1]:
        print("calculation check valid")
        return (clicksa * 3) + clicksb
    else:
        print("calculation check FAILED", x, find[0], y, find[1])

    return 0


def find_min_cost(a: tuple, b: tuple, find: tuple):

    a = (69, 23)
    b = (27, 71)
    find = (10000000018641, 10000000010279)

    possible_a = []
    for amount in range(100):
        multiplyx = a[0] * amount
        multiplyy = a[1] * amount
        if multiplyx > find[0] or multiplyy > find[1]:
            break
        possible_a.append((multiplyx, multiplyy))

    possible_b = []
    for amount in range(100):
        multiplyx = b[0] * amount
        multiplyy = b[1] * amount
        if multiplyx > find[0] or multiplyy > find[1]:
            break
        possible_b.append((multiplyx, multiplyy))

    # print("possible A presses")
    # print(possible_a)
    # print("possible B presses")
    # print(possible_b)

    found_costs = []
    for i, a in enumerate(possible_a):
        a_x, a_y = a
        for j, b in enumerate(possible_b):
            b_x, b_y = b
            if a_x + b_x == find[0] and a_y + b_y == find[1]:
                print(f"Found combination at a: {i}, b: {j}")
                found_costs.append((i * 3) + (j))

    return min(found_costs, default=0)


def get_button_numbers(line):
    _, x, y = line.split("+")
    return (int(x[:2]), int(y[:2]))


def get_prize_numbers(line):
    _, x, y = line.split("=")
    x = int(''.join(filter(str.isdigit, x)))
    y = int(''.join(filter(str.isdigit, y)))
    return (x, y)


def part1(content):
    all_puzzles = []
    for line_number, item in enumerate(content):
        if "A" in item:
            a = get_button_numbers(content[line_number])
            b = get_button_numbers(content[line_number + 1])
            p = get_prize_numbers(content[line_number + 2])
            all_puzzles.append([a, b, p])

    print(all_puzzles)
    all_costs = []

    for q, w, e in all_puzzles:
        all_costs.append(find_min_cost(q, w, e))

    print(all_costs)
    print(sum(all_costs))
    # find_min_cost((), (), ())


def part2(content):
    all_puzzles = []
    for line_number, item in enumerate(content):
        if "A" in item:
            a = get_button_numbers(content[line_number])
            b = get_button_numbers(content[line_number + 1])
            p = get_prize_numbers(content[line_number + 2])
            p = (p[0] + 10000000000000, p[1] + 10000000000000)
            all_puzzles.append([a, b, p])

    # print(all_puzzles)
    all_costs = []

    for q, w, e in all_puzzles:
        all_costs.append(part2_find_min_cost(q, w, e))

    # print(all_costs)
    print(sum(all_costs))
    # find_min_cost((), (), ())


if __name__ == "__main__":
    content = load_file("advent13.txt")
    # part1(content)
    part2(content)
