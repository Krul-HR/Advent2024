import os
from datetime import datetime
start_time = datetime.now()


def check_if_valid_increment(line: list):
    for i in range(len(line) - 1):
        difference = line[i + 1] - line[i]
        if difference > 3 or difference < 1:
            return False
    return True


def check_if_valid_decrement(line: list):
    for i in range(len(line) - 1):
        difference = line[i] - line[i + 1]
        if difference > 3 or difference < 1:
            return False
    return True


def check_valid_line(oneline: list):
    if oneline == sorted(oneline):
        print("increment", check_if_valid_increment(oneline))
        return check_if_valid_increment(oneline)
    elif oneline == sorted(oneline, reverse=True):
        print("decrement", check_if_valid_decrement(oneline))
        return check_if_valid_decrement(oneline)
    print("not sorted thus invalid", oneline)
    return False


filename = "advent2.txt"
if not os.path.exists(filename):
    print("error the file does not exist. ")
else:
    text_file = open(filename, "r")
    content = text_file.readlines()


safe_counter = 0

# part 1
# for line in content:
#     line_list = [int(x) for x in line.split()]
#     if line_list == sorted(line_list):
#         if check_if_valid_increment(line_list):
#             safe_counter += 1
#     elif line_list == sorted(line_list, reverse=True):
#         if check_if_valid_decrement(line_list):
#             safe_counter += 1
#     else:
#         print("not sorted valid")

# print(safe_counter)


# part 2
safe_dampener = 0

for fds in content:
    line_list = [int(x) for x in fds.split()]

    remove_index = 0
    valid_line = check_valid_line(line_list)
    while valid_line == False and remove_index < len(line_list):
        newList = [elem for elem in line_list]
        newList.pop(remove_index)
        print(newList)
        valid_line = check_valid_line(newList)
        remove_index += 1

    if valid_line:
        safe_dampener += 1


print(safe_dampener)


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
