# day 5
def binary_seating(seat_str):
    row_str = seat_str[:7].replace('B', '1').replace('F', '0')
    row = int(row_str, 2)
    col_str = seat_str[7:].replace('R', '1').replace('L', '0')
    col = int(col_str, 2)
    seat_id = row*8+col
    return seat_id


def highest_seat(input_str):
    lines = [line for line in input_str.split('\n') if line]
    seat_ids = [binary_seating(item) for item in lines]
    return max(seat_ids)


def find_my_seat(input_str):
    lines = [line for line in input_str.split('\n') if line]
    seat_ids = [binary_seating(item) for item in lines]
    seat_ids.sort()
    adjacent_seats = []
    for i in range(1, len(seat_ids)-1):
        if seat_ids[i] - 1 == seat_ids[i-1] \
                and seat_ids[i] + 1 == seat_ids[i+1]:
            continue
        else:
            adjacent_seats.append(seat_ids[i])
    assert adjacent_seats[0] + 2 == adjacent_seats[1]
    # the seat in between
    return adjacent_seats[0] + 1


def main():
    with open('./input_folder/day5.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    assert highest_seat(input_text) == 892
    # part2
    assert find_my_seat(input_text) == 625
    print('success!!')


if __name__ == '__main__':
    main()
