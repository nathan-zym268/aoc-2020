# day 16
from collections import defaultdict
from functools import reduce


def find_invalid_ticket(input_str):
    # some duplicates with part1
    parts = [part for part in input_str.split('\n\n') if part]
    valid_parts = [line for line in parts[0].split('\n') if line]
    valid_nums = []
    for line in valid_parts:
        for ran in line.split(':')[1].strip().split('or'):
            nums = [int(num.strip()) for num in ran.strip().split('-')]
            valid_nums += list(range(nums[0], nums[1] + 1))
    valid_num_set = set(valid_nums)
    nearby_tickets = parts[2].split('\n')[1:]
    invalid_rate = 0
    for tkts in nearby_tickets:
        for num in tkts.split(','):
            if not num:
                continue
            if int(num) not in valid_num_set:
                invalid_rate += int(num)

    return invalid_rate


def find_invalid_ticket_part2(input_str):
    parts = [part for part in input_str.split('\n\n') if part]
    valid_parts = [line for line in parts[0].split('\n') if line]
    valid_nums = []
    valid_num_dict = {}
    for line in valid_parts:
        k = line.split(':')[0].strip()
        v_nums = []
        for ran in line.split(':')[1].strip().split('or'):
            nums = [int(num.strip()) for num in ran.strip().split('-')]
            v_nums += list(range(nums[0], nums[1] + 1))
        valid_nums += v_nums
        valid_num_dict[k] = set(v_nums)
    # print(valid_num_dict)
    valid_num_set = set(valid_nums)
    nearby_tickets = parts[2].split('\n')[1:]
    my_ticket = parts[1].split('\n')[1]
    valid_tickets = [my_ticket]
    for tkts in nearby_tickets:
        for num in tkts.split(','):
            if not num:
                break
            if int(num) not in valid_num_set:
                break
        else:
            valid_tickets.append(tkts)
    # making valid ticket into 2d array/list
    valid_tickets_array = [
        [int(item) for item in tkts.split(',')]
        for tkts in valid_tickets
    ]
    idx_set = {}
    for idx in range(len(valid_tickets_array[0])):
        idx_set[idx] = {row[idx] for row in valid_tickets_array}
    # print(idx_set)

    mapping_dict = defaultdict(set)
    for key, value in valid_num_dict.items():
        for idx in range(len(valid_tickets_array[0])):
            if idx_set[idx].issubset(value):
                mapping_dict[key].add(idx)

    final_mapping = {}
    cur_set = set()
    # build the match from the one we know for sure
    for i in range(1, 22):
        for key, value in mapping_dict.items():
            if len(value) == i:
                final_mapping[key] = list(value.difference(cur_set))[0]
                cur_set = value

    departure_idx = [
        value for key, value
        in final_mapping.items() if key.startswith('departure')
    ]
    my_ticket_departure_num = [
        int(tkt) for idx, tkt in enumerate(
            my_ticket.split(','),
        ) if idx in departure_idx
    ]
    return reduce((lambda x, y: x * y), my_ticket_departure_num)


def main():
    with open('./input_folder/day16.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    assert find_invalid_ticket(input_text) == 30869
    # part2
    assert find_invalid_ticket_part2(input_text) == 4381476149273
    print('success!!')


if __name__ == '__main__':
    main()
