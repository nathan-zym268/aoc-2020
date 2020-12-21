def digitalize_seat(input_string):
    array = []
    for line in input_string.split('\n'):
        if not line:
            continue
        row = [int(i) for i in line.replace('.', '0').replace('L', '1')]
        array.append(row)
    return array


def adjacent_seats(idx_i, idx_j, input_array):
    count_occupied = 0
    for i in range(max(idx_i-1, 0), min(idx_i+2, len(input_array))):
        for j in range(max(idx_j-1, 0), min(idx_j+2, len(input_array[0]))):
            if i == idx_i and j == idx_j:
                continue
            if input_array[i][j] == 1:
                count_occupied += 1
    return count_occupied


def change_seat(input_array):
    tmp_array = []
    for i in range(len(input_array)):
        row = []
        for j in range(len(input_array[0])):
            count_occupied = adjacent_seats(i, j, input_array)
            if input_array[i][j] == -1 and count_occupied == 0:
                row.append(1)
            elif input_array[i][j] == 1 and count_occupied > 3:
                row.append(-1)
            else:
                row.append(input_array[i][j])
        tmp_array.append(row)
    return tmp_array


def stop_chaos(input_array):
    old_array = input_array
    new_array = change_seat(old_array)
    rounds = 0
    while new_array != old_array:
        if rounds > 1000:
            print('Something is wrong')
            return False
        tmp = change_seat(new_array)

        old_array = new_array
        new_array = tmp
        rounds += 1
    occupied_seats = 0
    for i in range(len(new_array)):
        occupied_seats += sum([item for item in new_array[i] if item == 1])
    return occupied_seats


def adjacent_seats_part2(idx_i, idx_j, input_array):
    count_occupied = 0
    direction = [-1, 0, 1]

    for i_dir in direction:
        for j_dir in direction:
            if i_dir == 0 and j_dir == 0:
                continue
            # start position
            i = idx_i + i_dir
            j = idx_j + j_dir
            while 0 <= i < len(input_array) and 0 <= j < len(input_array[0]):
                if input_array[i][j] == 1:
                    count_occupied += 1
                    break
                if input_array[i][j] == -1:
                    break
                i += i_dir
                j += j_dir
    return count_occupied


def change_seat_part2(input_array):
    tmp_array = []
    for i in range(len(input_array)):
        row = []
        for j in range(len(input_array[0])):
            count_occupied = adjacent_seats_part2(i, j, input_array)
            if input_array[i][j] == -1 and count_occupied == 0:
                row.append(1)
            elif input_array[i][j] == 1 and count_occupied > 4:
                row.append(-1)
            else:
                row.append(input_array[i][j])
        tmp_array.append(row)
    return tmp_array


def stop_chaos_part2(input_array):
    old_array = input_array
    new_array = change_seat_part2(old_array)
    rounds = 0
    while new_array != old_array:
        if rounds > 1000:
            print('Something is wrong')
            return False
        tmp = change_seat_part2(new_array)

        old_array = new_array
        new_array = tmp
        rounds += 1
    occupied_seats = 0
    for i in range(len(new_array)):
        occupied_seats += sum([item for item in new_array[i] if item == 1])
    return occupied_seats


def main():
    with open('./input_folder/day11.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    input_array = digitalize_seat(input_text)
    assert stop_chaos(input_array) == 2126
    # part2
    input_array = digitalize_seat(input_text)

    assert stop_chaos_part2(input_array) == 1914
    print('success!!')


if __name__ == '__main__':
    main()
