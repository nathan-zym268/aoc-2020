# day 6
def count_yes(entry):
    answer = ''.join(entry.split())
    return len(set(answer))


def count_yes_part2(entry):
    setlist = [set(line) for line in entry.split()]
    final_set = set.intersection(*setlist)
    return len(set(final_set))


def count_all_group(input_str):
    lines = [line for line in input_str.split('\n\n') if line]
    count_group = [count_yes(line) for line in lines]
    count_group_part2 = [count_yes_part2(line) for line in lines]
    return sum(count_group), sum(count_group_part2)


def main():
    with open('./input_folder/day6.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1 and part2
    assert count_all_group(input_text) == (6534, 3402)
    print('success!!')


if __name__ == '__main__':
    main()
