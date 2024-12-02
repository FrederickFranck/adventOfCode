from santa_helpers.helpers import read_input
import time

_input = read_input(False)
levels = _input.splitlines()


# PART 1
# Functions checks contraits of a given level
def is_level_safe(level_list):

    # Copy list and shift by one
    shifted_list = level_list.copy()
    shifted_list.pop(0)
    shifted_list.append(0)

    # Calculate difference between previous value and store in list
    diff = []
    for level_value, shifted_value in zip(level_list, shifted_list):
        diff.append(level_value - shifted_value)
    diff.pop()

    # Check requirements
    for index, value in enumerate(diff):
        if abs(value) == 0:
            return False
        elif abs(value) > 3:
            return False
        elif index != 0 and (value * diff[index - 1]) <= 0:
            return False
    return True


start = time.perf_counter()
safe_reports_1 = 0
for level in levels:
    level_list = list(map(int, level.split()))
    if is_level_safe(level_list):
        safe_reports_1 = safe_reports_1 + 1

end = time.perf_counter()
print(f"Part 1 solution: {safe_reports_1}, took {(end-start)*1000} ms")


# PART 2
# Checks all possible versions of levels with 1 item removed
# until it finds one that matches the constraints
def problem_dampener(_level):
    for i, v in enumerate(_level):
        copy_level = _level.copy()
        copy_level.pop(i)
        if is_level_safe(copy_level):
            return True
    return False


start = time.perf_counter()

safe_reports_2 = 0
for level in levels:
    level_list = list(map(int, level.split()))
    if problem_dampener(level_list):
        safe_reports_2 = safe_reports_2 + 1

end = time.perf_counter()
print(f"Part 2 solution: {safe_reports_2}, took {(end-start)*1000} ms")
