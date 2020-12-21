# day17
from collections import Counter
from itertools import product


def conway_cube_part1(input_str):
    # initial status, z = 0
    cur_active_cubes = set()
    lines = [line for line in input_str.split() if line]
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] == '#':
                cur_active_cubes.add((x, y, 0))

    for i in range(6):
        new_active_cubes = set()
        neighbour_cur_inactive = []
        for cube in cur_active_cubes:
            x, y, z = cube
            all_neighbours = list(
                product(
                    range(x - 1, x + 2), range(y - 1, y + 2),
                    range(z - 1, z + 2),
                ),
            )
            neighbour_active = [
                item for item in all_neighbours
                if item in cur_active_cubes and item != cube
            ]
            neighbour_inactive = [
                item for item in all_neighbours
                if item not in cur_active_cubes and item != cube
            ]
            neighbour_cur_inactive += neighbour_inactive
            if len(neighbour_active) in (2, 3):
                new_active_cubes.add(cube)
        inactive_counter = Counter(neighbour_cur_inactive)
        new_active_cubes = new_active_cubes.union(
            {key for key, value in inactive_counter.items() if value == 3},
        )
        cur_active_cubes = new_active_cubes

    return len(cur_active_cubes)


def conway_cube_part2(input_str):
    # again, lots of copy pasting...
    # but I will just leave my code like this for now
    # initial status, z = 0, w = 0
    cur_active_cubes = set()
    lines = [line for line in input_str.split() if line]
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] == '#':
                cur_active_cubes.add((x, y, 0, 0))

    for i in range(6):
        new_active_cubes = set()
        neighbour_cur_inactive = []
        for cube in cur_active_cubes:
            x, y, z, w = cube
            all_neighbours = list(
                product(
                    range(x - 1, x + 2), range(y - 1, y + 2),
                    range(z - 1, z + 2), range(w - 1, w + 2),
                ),
            )
            neighbour_active = [
                item for item in all_neighbours
                if item in cur_active_cubes and item != cube
            ]
            neighbour_inactive = [
                item for item in all_neighbours
                if item not in cur_active_cubes and item != cube
            ]
            neighbour_cur_inactive += neighbour_inactive
            if len(neighbour_active) in (2, 3):
                new_active_cubes.add(cube)
        inactive_counter = Counter(neighbour_cur_inactive)
        new_active_cubes = new_active_cubes.union(
            {key for key, value in inactive_counter.items() if value == 3},
        )
        cur_active_cubes = new_active_cubes

    return len(cur_active_cubes)


def main():
    with open('./input_folder/day17.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    assert conway_cube_part1(input_text) == 359
    # part2
    assert conway_cube_part2(input_text) == 2228
    print('success!!')


if __name__ == '__main__':
    main()
