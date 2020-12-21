from collections import defaultdict


def memory_game(input_seq, end_turn):
    nums = [int(num) for num in input_seq.split(',')]
    num_turn = defaultdict(list)
    for idx, num in enumerate(nums):
        num_turn[num] = [idx + 1]
    i = len(nums) + 1
    while i < end_turn + 1:
        previous_turns = num_turn.get(nums[-1], [])
        if len(previous_turns) < 2:
            nums.append(0)
            num_turn[0].append(i)
        else:
            num = previous_turns[-1] - previous_turns[-2]
            nums.append(num)
            num_turn[num].append(i)
        i += 1
    return nums[-1]


def main():
    with open('./input_folder/day15.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    assert memory_game(input_text, 2020) == 260
    # part2
    # part2 takes a while, a few mins
    assert memory_game(input_text, 30000000) == 950
    print('success!!')


if __name__ == '__main__':
    main()
