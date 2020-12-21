def jolt_part1(input_str):
    jolt_list = [int(item) for item in input_str.split('\n') if item]
    jolt_list.sort()
    jolt_list.insert(0, 0)
    count_diff1 = 0
    count_diff3 = 1
    for i in range(1, len(jolt_list)):
        if jolt_list[i] - jolt_list[i-1] == 1:
            count_diff1 += 1
        if jolt_list[i] - jolt_list[i-1] == 3:
            count_diff3 += 1

    return count_diff1*count_diff3


def get_jolt_diff(input_str):
    # return a list of diffs of the jolt list
    # so [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    # will become [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]
    jolt_list = [int(item) for item in input_str.split('\n') if item]
    jolt_list.sort()
    jolt_list.insert(0, 0)
    jolt_list.append(jolt_list[-1]+3)
    diffs = []
    for i in range(1, len(jolt_list)):
        diffs.append(jolt_list[i]-jolt_list[i-1])
    return diffs


def jolt_part2(diff):
    # from observation
    # count how many consecutive diff 1 appears before diff 3 appears
    count = 1
    count_1 = 0
    for i in range(len(diff)):
        if diff[i] == 1:
            count_1 += 1
            i += 1
        if diff[i] == 3:
            # if only one diff 1, there is only one case
            # if 2 diff 1, there are two cases
            # e.g.,  1 2 3 6 -> 1 3 6, 1 2 3 6
            if count_1 == 2:
                count = count * 2
            # if 3 diff 1, there are 4 cases
            # e.g.,  1 2 3 4 7 -> 1 2 3 4 7, 1 3 4 7, 1 2 4 7, 1 4 7
            if count_1 == 3:
                count = count * 4
            # if 4 diff 1, there are 7 cases
            # e.g.,  1 2 3 4 5 8 -> 1 2 3 4 5 8, 1 3 4 5 8, 1 4 5 8, 1 2 4 5 8,
            # 1 2 3 5 8, 1 3 5 8, 1 2 5 8
            if count_1 == 4:
                count = count * 7
            # if 5 diff 1, there are 13 cases
            if count_1 == 5:
                count = count * 13
            # luckily the puzzle input does not contain
            # more consecutive one cases
            # otherwise, it continues like a tribonacci
            count_1 = 0
    return count


def main():
    with open('./input_folder/day10.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    assert jolt_part1(input_text) == 2368
    # part2
    diffs = get_jolt_diff(input_text)
    assert jolt_part2(diffs) == 1727094849536
    print('success!!')


if __name__ == '__main__':
    main()
