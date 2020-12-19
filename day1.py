def report_repair(list_num):
    # part1: two sum
    num_set = set(list_num)
    for num in list_num:
        if 2020-num in num_set:
            return num*(2020-num)
    return 0


def report_repair_three_sum(list_num):
    # part2: three sum
    num_set = set(list_num)
    for num1 in list_num:
        two_sum = 2020 - num1
        for num2 in list_num:
            if num1 == num2:
                continue
            num3 = two_sum - num2
            if num3 in num_set and num3 != num1:
                return num1 * num2 * num3
    return 0


def main():
    with open('./input_folder/day1.txt', encoding='UTF-8') as fh:
        lines = fh.read().splitlines()
    list_num = [int(line) for line in lines]
    # part1
    assert report_repair(list_num) == 997899
    # part2
    assert report_repair_three_sum(list_num) == 131248694
    print('success!!')


if __name__ == '__main__':
    main()
