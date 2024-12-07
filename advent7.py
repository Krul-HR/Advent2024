import os


def load_file(file_path):
    if not os.path.exists(file_path):
        print("error the file does not exist. ")
        return None
    else:
        text_file = open(file_path, "r")
        content = text_file.readlines()
        return content


def recursive_lambda(result, numbers, lam):
    # Last number and we found it?
    if len(numbers) == 1:
        if result == numbers[0]:
            return True
        return False

    between = lam(numbers[0], numbers[1])

    # did we already find it? prevent last recursion
    if result == between and len(numbers) == 2:
        return True

    # too high, not possible anymore
    if between > result:
        return False

    # remove first two items from the list and at the between
    numbers.pop(0)
    numbers.pop(0)
    numbers.insert(0, between)

    # damn reference types
    first_loop = [elem for elem in numbers]
    second_loop = [elem for elem in numbers]

    # lambda
    plus = lambda x, y: x + y
    multiply = lambda x, y: x * y

    # recursion
    if recursive_lambda(result, first_loop, multiply):
        # print("plus -> recursion multi", numbers)
        return True
    if recursive_lambda(result, second_loop, plus):
        # print("plus -> recursion plus", numbers)
        return True
    return False


def recursive_first(result, numbers):

    # don't make easy recursion
    if len(numbers) == 2:
        if result == numbers[0] * numbers[1]:
            return True
        if result == numbers[0] + numbers[1]:
            return True
        return False

    # damn reference types
    first_loop = [elem for elem in numbers]
    second_loop = [elem for elem in numbers]

    plus = lambda x, y: x + y
    multiply = lambda x, y: x * y

    if recursive_lambda(result, first_loop, multiply):
        # print("x true")
        return True
    if recursive_lambda(result, second_loop, plus):
        # print("+ true")
        return True

    return False


def part1_recursive(content):
    # print("recur start")
    total = 0
    for line in content:
        result, numbers = line
        x = recursive_first(result, numbers)
        print(x, result)
        if x:
            total += result

    print("total part 1: ", total)


if __name__ == "__main__":
    content = load_file("advent7.txt")
    splitted = []
    for line in content:
        r, numbers = line.rstrip().split(":")
        numbers = [int(n) for n in numbers.strip().split()]
        splitted.append((int(r), numbers))
    print("Part 1: ", part1_recursive(splitted))

    # content = load_file("advent7.txt")
    # splitted = []
    # for line in content:
    #     splitted.append(list(line.rstrip()))
    # start_time = datetime.now()
    # print("Part 2: ", part2(splitted))
    # end_time = datetime.now()
    # print('Duration: {}'.format(end_time - start_time))
