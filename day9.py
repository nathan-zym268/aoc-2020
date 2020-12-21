# day9
def find_pair(seq, num):
    set_seq = set(seq)
    for item in seq:
        if num - item in set_seq:
            return True
    else:
        return False


def preamble_sequence(input_str, seq_len):
    seq = [int(item) for item in input_str.split('\n') if item]

    i = 0
    while i + seq_len + 1 < len(seq):
        preamble_seq = seq[i:i+seq_len]
        if not find_pair(preamble_seq, seq[i+seq_len]):
            return seq[i+seq_len]
        i += 1
    return True


def find_contiguous_set(input_str, num):
    seq = [int(item) for item in input_str.split('\n') if item]
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if sum(seq[i:j]) > num:
                break
            if sum(seq[i:j]) == num:
                return min(seq[i:j]) + max(seq[i:j])


def main():
    with open('./input_folder/day9.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    part1_result = preamble_sequence(input_text, 25)
    assert part1_result == 776203571
    # part2
    assert find_contiguous_set(input_text, part1_result) == 104800569
    print('success!!')


if __name__ == '__main__':
    main()
