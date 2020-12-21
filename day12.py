# day12
import re


def move_ship(pos, direction, num_steps):
    if direction == 'E':
        pos[0] += num_steps
        return pos
    if direction == 'W':
        pos[0] -= num_steps
        return pos
    if direction == 'N':
        pos[1] += num_steps
        return pos
    if direction == 'S':
        pos[1] -= num_steps
        return pos
    return pos


def change_facing(original_facing, move, degree):
    directions = ['E', 'S', 'W', 'N']
    mv = int(degree / 90)
    for i in range(len(directions)):
        if directions[i] == original_facing:
            if move == 'R':
                if i + mv > len(directions) - 1:
                    return directions[i + mv - len(directions)]
                return directions[i + mv]
            if move == 'L':
                return directions[i - mv]


def evade_storm(input_str):
    pos = [0, 0]
    facing = 'E'
    lines = [line for line in input_str.split('\n') if line]
    # E +, W -, N +, S -
    for line in lines:
        move = re.search('[A-Z]+', line)[0]
        num_steps = int(re.search('[0-9]+', line)[0])
        if move == 'F':
            pos = move_ship(pos, facing, num_steps)
        if move in {'L', 'R'}:
            facing = change_facing(facing, move, num_steps)
        if move in {'N', 'S', 'E', 'W'}:
            pos = move_ship(pos, move, num_steps)
    man_dist = abs(pos[0]) + abs(pos[1])
    return man_dist


def change_waypoint(waypoint, move, degree):
    mv = int(degree/90)
    if move == 'R':
        if mv == 1:
            return [waypoint[1], -waypoint[0]]
        if mv == 2:
            return [-waypoint[0], -waypoint[1]]
        if mv == 3:
            return [-waypoint[1], waypoint[0]]
    if move == 'L':
        if mv == 1:
            return [-waypoint[1], waypoint[0]]
        if mv == 2:
            return [-waypoint[0], -waypoint[1]]
        if mv == 3:
            return [waypoint[1], -waypoint[0]]


def evade_storm_part2(input_str):
    pos = [0, 0]
    waypoint = [10, 1]
    lines = [line for line in input_str.split('\n') if line]
    for line in lines:
        move = re.search('[A-Z]+', line)[0]
        num_steps = int(re.search('[0-9]+', line)[0])
        if move == 'F':
            pos = [a + num_steps * b for a, b in zip(pos, waypoint)]
        if move in {'L', 'R'}:
            waypoint = change_waypoint(waypoint, move, num_steps)
        if move in {'N', 'S', 'E', 'W'}:
            waypoint = move_ship(waypoint, move, num_steps)
    man_dist = abs(pos[0]) + abs(pos[1])
    return man_dist


def main():
    with open('./input_folder/day12.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    assert evade_storm(input_text) == 1133
    # part2
    assert evade_storm_part2(input_text) == 61053
    print('success!!')


if __name__ == '__main__':
    main()
