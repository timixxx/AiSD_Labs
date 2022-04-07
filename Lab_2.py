import random
import re

print("Task 1:")

with open("test_file.txt", "w") as f:
    for i in range(10):
        number = random.randint(-50, 50)
        f.write(str(number) + " ")

with open("test_file.txt", "r") as f:
    count = 0
    for line in f:
        for i in line.split():
            if int(i) < 0:
                count+=1

print(count)

print("Task 2:")
with open("test2_file.txt", "w") as f:
    print("12 345 123 432 123 111", file=f)
    f.seek(random.randint(0, 20))
    print(str(input()), file=f)

with open("test_file.txt", "r") as f:
    print(f.read())

print("Task 3:")
with open("task3_file.txt", 'r') as f:
    n = int(input("input n number of line: "))
    line_count = 0
    for line in f.readlines():
        line_count += 1
        if (line_count == n):
            print(line)


def find_all_indexes(input_str, search_str):
    l1 = []
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(search_str, index)
        if i == -1:
            return l1
        l1.append(i)
        index = i + 1
    return l1

print("Task 4:")
# with open("task3_file.txt", 'r') as f:
#     n = str(input("what substring are we looking for?: "))
#     line_count = 0
#     for line in f.readlines():
#         for l in line:
#             print(find_all_indexes(l, n))
n = input("input substring: ")
file = open("task3_file.txt", "r")
line = file.readlines()
i = 0
for l in line:
    print(find_all_indexes(l, n))
file.close()

print("Task 5:")
file = open("task3_file.txt", "r")
line = file.readlines()
data = {}

for l in line:
    for key in l.split():
        data[key] = data.setdefault(key, 0) + 1

print(data)

with open("task3_file.txt", "r") as f:
    for line in f.readlines():
        print(re.sub(r'[^\w\s]','', line))

