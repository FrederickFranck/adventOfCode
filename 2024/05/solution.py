from santa_helpers.helpers import read_input
from rich import print

_input = read_input(False)

rules = list(
    map(lambda x: list(map(int, x.split("|"))), _input.split("\n\n")[0].split())
)
updates = list(
    map(lambda x: list(map(int, x.split(","))), _input.split("\n\n")[1].split())
)


def get_update_coordinates(updates):
    u = []
    for update in updates:
        _u = {}
        for index, value in enumerate(update):
            _u[value] = index
        u.append(_u)
    return u


def check_rule(rule, update):
    first = rule[0]
    second = rule[1]
    pos_1 = None
    pos_2 = None

    # print(f"{first} in {update}")
    if first in update:
        pos_1 = update[first]
    # print(f"{second} in {update}")
    if second in update:
        pos_2 = update[second]
    # print(f"is {first}@[{pos_1}] before {second}@[{pos_2}]")
    if (pos_1 is not None) and (pos_2 is not None):
        # print(f"is {first}@[{pos_1}] before {second}@[{pos_2}]")
        # print(pos_1 - pos_2)
        if (pos_1 - pos_2) < 0:
            return True
        else:
            return False
    return True


def check_updates(rules, updates):
    correct_updates = []
    incorrect_updates = []
    for update in updates:
        incorrect = False
        for rule in rules:
            # print(f"Update {update}")
            # print(f"Rule {rule}")
            if check_rule(rule, update):
                continue
            else:
                incorrect = True
                break
        if not incorrect:
            # print(f"APP {update}")
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    return correct_updates, incorrect_updates


def get_result(correct_updates):
    total = 0
    for c in correct_updates:
        middle = int(len(c) / 2)
        for key, value in c.items():
            if value == middle:
                total = total + key

    return total


c = get_update_coordinates(updates)
# print(c)
# print(rules)
rc, ic = check_updates(rules, c)
# print(rc)
print(f"Part1 solution {get_result(rc)}")


def correct_reports(incorrect_reports):
    for update in incorrect_reports:
        index = 0
        while index < len(rules):
            rule = rules[index]
            # print(f"Update {update}")
            # print(f"Rule {rule}")
            if check_rule(rule, update):
                index = index + 1
                continue
            else:
                pos_1 = update[rule[0]]
                pos_2 = update[rule[1]]
                update[rule[0]] = pos_2
                update[rule[1]] = pos_1
                index = 0
    return incorrect_reports


# print(correct_reports(ic))
print(f"Part2 solution {get_result(correct_reports(ic))}")
