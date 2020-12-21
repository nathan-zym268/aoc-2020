import re


def bit_mask(bit_str, mask):
    new_bit_str = ''
    assert len(bit_str) == len(mask)
    for i, char in enumerate(mask):
        if char == 'X':
            new_bit_str += bit_str[i]
        else:
            new_bit_str += char
    return new_bit_str


def bitmasking(input_str, mem):
    lines = [line for line in input_str.split('\n') if line]
    mask = lines[0].split('=')[1].strip()
    for line in lines[1:]:
        pos = re.search('[0-9]+', line.split('=')[0])[0]
        num = int(re.search('[0-9]+', line.split('=')[1])[0])
        bit_str = f'{num:b}'
        bit_str_full = '0' * (len(mask) - len(bit_str)) + bit_str
        new_bit_str = bit_mask(bit_str_full, mask)
        mem[pos] = int(new_bit_str, 2)
    return mem


def bit_mask_part2(bit_str, mask):
    new_bit_str = ''
    assert len(bit_str) == len(mask)
    for i, char in enumerate(mask):
        if char == '0':
            new_bit_str += bit_str[i]
        else:
            new_bit_str += char
    return new_bit_str


def find_all_floating(bit_str):
    for i, char in enumerate(bit_str):
        if i + 1 == len(bit_str):
            if char == 'X':
                return [bit_str[0:i] + '0', bit_str[0:i] + '1']
            else:
                return [bit_str[0:i] + char]
        if char == 'X':
            return [
                bit_str[0:i]+'0'+item
                for item in find_all_floating(bit_str[i+1:])
            ] + \
                [
                bit_str[0:i]+'1' + item
                for item in find_all_floating(bit_str[i+1:])
                ]


def bitmasking_part2(input_str, mem):
    lines = [line for line in input_str.split('\n') if line]
    mask = lines[0].split('=')[1].strip()

    for line in lines[1:]:
        pos = int(re.search('[0-9]+', line.split('=')[0])[0])
        num = int(re.search('[0-9]+', line.split('=')[1])[0])
        bit_str = f'{pos:b}'
        bit_str_full = '0'*(len(mask)-len(bit_str)) + bit_str
        mem_pos = [
            int(item, 2) for item in find_all_floating(
                bit_mask_part2(bit_str_full, mask),
            )
        ]
        for pos in mem_pos:
            mem[pos] = num
    return mem


def bitmasking_multiple(input_str):
    parts = [line for line in input_str.split('mask') if line]
    mem_part1 = {}
    mem_part2 = {}
    for part in parts:
        mem_part1 = bitmasking(part, mem_part1)
        mem_part2 = bitmasking_part2(part, mem_part2)

    return sum(mem_part1.values()), sum(mem_part2.values())


def main():
    with open('./input_folder/day14.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1 and part2
    part1, part2 = bitmasking_multiple(input_text)
    assert part1 == 7817357407588
    assert part2 == 4335927555692
    print('success!!')


if __name__ == '__main__':
    main()
