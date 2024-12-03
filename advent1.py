import os
from datetime import datetime
start_time = datetime.now()

filename = "advent1.txt"
if not os.path.exists(filename):
    print("error the file does not exist. ")
else:
    text_file = open(filename, "r")
    content = text_file.readlines()

c1 = []
c2 = []

for line in content:
    v1, v2 = line.rstrip().split("   ")
    c1.append(int(v1))
    c2.append(int(v2))


c1.sort()
c2.sort()

total_distance = 0

for i in range(len(c1)):
    if c1[i] > c2[i]:
        total_distance += c1[i] - c2[i]
    else:
        total_distance += c2[i] - c1[i]

print("Total distance: ", total_distance)


start_time = datetime.now()

sim_score = 0

for num in c1:
    counter = c2.count(num)
    sim_score += num * counter

print("sim score: ", sim_score)


end_time = datetime.now()
print('Duration count: {}'.format(end_time - start_time))


start_time = datetime.now()

sim_score = 0

d = dict()

for num in c1:
    # count in second list
    count = 0
    for i in c2:
        if i == num:
            count += 1
    d[num] = count

for num2 in c1:
    sim_score += num2 * d[num2]

print("sim score: ", sim_score)


end_time = datetime.now()
print('Duration dict: {}'.format(end_time - start_time))
