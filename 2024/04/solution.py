from santa_helpers.helpers import read_input
from rich import print

_input = read_input(False)


WORD = "XMAS"


# Function that will read a word and create a dictionary
# for each letter with the coordinates [0,0]
def count_coordinates(word, _input):
    input_list = _input.splitlines()
    input_matrix = []
    for item in input_list:
        input_matrix.append(list(item))

    characters = list(word)
    coordinates = {c: [] for c in characters}

    for char in characters:
        for index_y, i in enumerate(input_matrix):
            for index_x, value in enumerate(i):
                if value == char:
                    coordinates[char].append([index_x, index_y])
    # print(coordinates)
    return coordinates


# Part 1
# Calculate neighbouring coordinates of a character for the starting character
# or if given a direction will give the next coordinate in that direction
def calculate_neighbours(coord, direction=None):
    x = coord[0]
    y = coord[1]

    neighbours = []
    if direction is None:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                neighbours.append([x + j, y + i])
        neighbours.remove(coord)

    else:
        if "up" in direction:
            y = y - 1
        elif "down" in direction:
            y = y + 1
        if "left" in direction:
            x = x - 1
        elif "right" in direction:
            x = x + 1
    neighbours.append([x, y])
    return neighbours


# Calculates direction inbetween 2 coordinates
def get_direction(coord1, coord2):
    direction = ""
    diff = [x - y for x, y in zip(coord1, coord2)]

    x = diff[0]
    y = diff[1]
    if y > 0:
        direction = direction + "up"
    elif y < 0:
        direction = direction + "down"
    if x == 0:
        return direction
    else:
        direction = direction + "_"
    if x < 0:
        direction = direction + "right"
    elif x > 0:
        direction = direction + "left"

    return direction


# Loop over coordinates from first letter ,
# if you find a neighbour in second letter coordinates
# Get the direction and continue for the next letter in sequence
# We use a global total because return True will do an early exit and miss
# words using the same starting letter
total = 0


def find_rec(coord, index, coordinates, direction=None) -> bool:
    characters = list(coordinates.keys())
    lenght = len(characters)
    if index >= lenght:
        global total
        total = total + 1
    else:
        if direction is None:
            next_char = characters[index]
            for neighbour in calculate_neighbours(coord):
                if neighbour in coordinates[next_char]:
                    if find_rec(
                        neighbour,
                        index + 1,
                        coordinates,
                        get_direction(coord, neighbour),
                    ):
                        return True

            return False
        else:
            next_char = characters[index]
            for neighbour in calculate_neighbours(coord, direction):
                if neighbour in coordinates[next_char]:
                    if find_rec(neighbour, index + 1, coordinates, direction):
                        return True
                return False


def main(coordinates):
    characters = list(coordinates.keys())
    for coord in coordinates[characters[0]]:
        find_rec(coord, 1, coordinates)

    return


c = count_coordinates(WORD, _input)
main(c)
print(f"Part 1 solution {total}")


# Part 2
# Check cross pair neighbours for requirements
def x_neighbours(coord):
    x = coord[0]
    y = coord[1]

    pair_1 = ([x - 1, y - 1], [x + 1, y + 1])
    pair_2 = ([x - 1, y + 1], [x + 1, y - 1])

    return pair_1, pair_2


_m = c["M"]
_s = c["S"]

total_2 = 0
for coord in c["A"]:
    p1, p2 = x_neighbours(coord)

    if ((p1[0] in _m and p1[1] in _s) or (p1[1] in _m and p1[0] in _s)) and (
        (p2[0] in _m and p2[1] in _s) or (p2[1] in _m and p2[0] in _s)
    ):
        total_2 = total_2 + 1


print(f"Part 2 solution {total_2}")
