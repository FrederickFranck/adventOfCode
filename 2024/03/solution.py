import re
from santa_helpers.helpers import read_input, _start, _stop
from rich import print


_input = read_input(False)


# Part 1
def calc_mults(_input):
    # Regex to find all mults from input
    list_mults = re.findall(r"mul\(\d+,\d+\)", _input)
    total = 0

    # Loop over all mul() , extract integers and calculate mult
    for mult in list_mults:
        _m = mult.split("(")[1]
        _m = _m.split(")")[0]
        x = list(map(int, _m.split(",")))
        total = total + (x[0] * x[1])

    return total


s = _start()
total = calc_mults(_input)
print(f"Part 1 Solution {total}")
_stop(s)


# Part 2
def dos_and_donts(_input):
    # Create list split on don't()
    donts = re.split(r"don't\(\)", _input)

    # Split on do() and throw away the first item excpet for the first item
    # that way we have removed all input between don't() _XXX_ do()
    dos = []
    for i, dont in enumerate(donts):
        do = re.split(r"do\(\)", dont)
        if i == 0:
            dos.extend(do)
        else:
            _do = do.copy()
            _do.pop(0)
            dos.extend(_do)

    input_to_be_executed = "".join(dos)
    return input_to_be_executed


s = _start()
total2 = calc_mults(dos_and_donts(_input))
print(f"Part 2 Solution {total2}")
_stop(s)
