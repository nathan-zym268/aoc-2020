import re


def password_validation(input_text):
    # part1
    count_valid = 0
    for line in input_text.split('\n'):
        if not line:
            continue
        l_bound = int(line.split()[0].split('-')[0])
        u_bound = int(line.split()[0].split('-')[1])
        letter = line.split()[1].strip(':')
        password = line.split()[2]
        num_match = len(re.findall(letter, password))
        if l_bound <= num_match <= u_bound:
            count_valid += 1
    return count_valid


def password_validation_part2(input_text):
    # part2
    count_valid = 0
    for line in input_text.split('\n'):
        if not line:
            continue
        idx1 = int(line.split()[0].split('-')[0])-1
        idx2 = int(line.split()[0].split('-')[1])-1
        letter = line.split()[1].strip(':')
        password = line.split()[2]
        if int(password[idx1] == letter) + int(password[idx2] == letter) == 1:
            count_valid += 1
    return count_valid


def main():
    with open('./input_folder/day2.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    assert password_validation(input_text) == 603
    # part2
    assert password_validation_part2(input_text) == 404
    print('success!!')


if __name__ == '__main__':
    main()
