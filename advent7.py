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
    third_loop = [elem for elem in numbers]

    # lambda
    plus = lambda x, y: x + y
    multiply = lambda x, y: x * y
    merge = lambda x, y: int(str(x) + str(y))

    if recursive_lambda(result, first_loop, multiply):
        return True
    elif recursive_lambda(result, second_loop, plus):
        return True
    # part 2
    elif recursive_lambda(result, third_loop, merge):

        return True
    return False


def recursive_first(result, numbers):

    # don't make easy recursion
    if len(numbers) == 2:
        if result == numbers[0] * numbers[1]:
            return True
        if result == numbers[0] + numbers[1]:
            return True
        if result == int(str(numbers[0]) + str(numbers[1])):
            return True
        return False

    # damn reference types
    first_loop = [elem for elem in numbers]
    second_loop = [elem for elem in numbers]
    third_loop = [elem for elem in numbers]

    plus = lambda x, y: x + y
    multiply = lambda x, y: x * y
    merge = lambda x, y: int(str(x) + str(y))

    if recursive_lambda(result, first_loop, multiply):
        return True
    elif recursive_lambda(result, second_loop, plus):
        return True
    # part 2
    elif recursive_lambda(result, third_loop, merge):

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

    print("total: ", total)


if __name__ == "__main__":
    content = load_file("advent7.txt")
    splitted = []
    for line in content:
        r, numbers = line.rstrip().split(":")
        numbers = [int(n) for n in numbers.strip().split()]
        splitted.append((int(r), numbers))
    print("Part 2: ", part1_recursive(splitted))
