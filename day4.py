# day4
import re

p_keys_need = {
    'byr',
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}


def parse_passport_info(input_str):
    lines = [line for line in input_str.split('\n\n') if line]
    entries = []
    for line in lines:
        entry = {
            pair.split(':')[0]: pair.split(':')[1]
            for pair in line.split() if pair
        }
        entries.append(entry)
    return entries


def count_valid(entries):
    count = 0
    for entry in entries:
        if p_keys_need.issubset(set(entry.keys())):
            count += 1
    return count


def hgt_rule(hgt):
    if re.search('cm', hgt):
        num = int(re.search('[0-9]+', hgt)[0])
        return 150 <= num <= 193
    if re.search('in', hgt):
        num = int(re.search('[0-9]+', hgt)[0])
        return 59 <= num <= 76
    return False


def count_valid_part2(entries):
    count = 0
    for entry in entries:
        if not p_keys_need.issubset(set(entry.keys())):
            continue
            # apply a set of rules
        byr = 1920 <= int(entry['byr']) <= 2002
        iyr = 2010 <= int(entry['iyr']) <= 2020
        eyr = 2020 <= int(entry['eyr']) <= 2030

        hgt = hgt_rule(entry['hgt'])

        hcl = bool(re.fullmatch('#[0-9a-f]{6}', entry['hcl']))
        ecl = entry['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        pid = bool(re.fullmatch('[0-9]{9}', entry['pid']))
        sum_score = int(byr) + int(iyr) + int(eyr) + \
            int(hgt) + int(hcl) + int(ecl) + int(pid)
        if sum_score == 7:
            count += 1
    return count


def main():
    with open('./input_folder/day4.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    entries = parse_passport_info(input_text)
    # part1
    assert count_valid(entries) == 235
    # part2
    assert count_valid_part2(entries) == 194
    print('success!!')


if __name__ == '__main__':
    main()
