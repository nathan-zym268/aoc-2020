import numpy as np


def digitalize_map(input_string):
    array = []
    for line in input_string.split('\n'):
        if not line:
            continue
        row = [int(i) for i in line.replace('.', '0').replace('#', '1')]
        array.append(row)
    return array


def toboggan_trajectory(array):
    # this solution might be a bit slow
    concat_array = array
    x_idx = 0
    y_idx = 0
    num_trees = 0
    while y_idx < len(array)-1:
        x_idx += 3
        y_idx += 1
        if x_idx >= len(concat_array[0]):
            concat_array = np.concatenate((concat_array, array), axis=1)
        num_trees += concat_array[y_idx][x_idx]
    return num_trees


def toboggan_trajectory_part2(array, r_move, d_move):
    concat_array = array
    x_idx = 0
    y_idx = 0
    num_trees = 0
    while y_idx < len(array)-1:
        x_idx += r_move
        y_idx += d_move
        if x_idx >= len(concat_array[0]):
            concat_array = np.concatenate((concat_array, array), axis=1)
        num_trees += concat_array[y_idx][x_idx]
    return num_trees


def main():
    with open('./input_folder/day3.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    array = digitalize_map(input_text)
    # part1
    assert toboggan_trajectory(array) == 187
    # part2
    assert toboggan_trajectory_part2(array, 1, 1) * \
        toboggan_trajectory_part2(array, 3, 1) * \
        toboggan_trajectory_part2(array, 5, 1) * \
        toboggan_trajectory_part2(array, 7, 1) * \
        toboggan_trajectory_part2(array, 1, 2) == 4723283400
    print('success!!')


if __name__ == '__main__':
    main()
