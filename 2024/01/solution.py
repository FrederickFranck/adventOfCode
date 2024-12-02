#from rich import print

# Read Input and create 2 sorted lists
from santa_helpers.helpers import read_input
_input = read_input()


_input = _input.replace("\n", "   ")
_input = _input.split("   ")

list1 = []
list2 = []

for index, location in enumerate(_input):
    if index % 2 == 0:
        list1.append(int(location))
    else:
        list2.append(int(location))

list1.sort()
list2.sort()

# Part 1
solution_1 = 0

for location_1, location_2 in zip(list1, list2):
    diff = abs(location_1 - location_2)
    solution_1 = solution_1 + diff

print(list1)
print(list2)
print(f"Part 1 solution : {solution_1}")


# Part 2
solution_2 = 0
for location_1 in list1:
    simil = location_1 * list2.count(location_1)
    solution_2 = solution_2 + simil

print(f"Part 2 solution : {solution_2}")
