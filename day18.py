# extremely messy solution...on a headache day
def operation_order(input_str):
    strip_str = ''.join([item.strip() for item in input_str.split()])
    # split it into parts
    parts = []
    cur_part = ''
    bracket_balance = 0
    for i in strip_str:
        if i == '(':
            if bracket_balance == 0:
                if cur_part:
                    parts.append(cur_part)
                    cur_part = '('
                else:
                    cur_part += '('
            else:
                cur_part += '('
            bracket_balance += 1
        elif i == ')':
            if bracket_balance - 1 == 0:
                if cur_part:
                    parts.append(cur_part + ')')
                    cur_part = ''
            else:
                cur_part += ')'
            bracket_balance -= 1
        else:
            cur_part += i
    if cur_part:
        parts.append(cur_part)

    final_parts = []
    for part in parts:
        if part.startswith('('):
            final_parts.append(part[1:-1])
        else:
            final_parts += list(part)
    # print(final_parts)
    result = 0
    for i in range(int((len(final_parts) - 1) / 2)):
        idx = 2 * i + 1
        left = final_parts[idx - 1] if idx == 1 else result
        left = int(str(left)) if str(left).isdigit() else operation_order(left)
        right = final_parts[idx + 1]
        right = int(str(right)) if str(
            right,
        ).isdigit() else operation_order(right)
        if final_parts[idx] == '+':
            result = left + right
        if final_parts[idx] == '*':
            result = left * right

    return result


def split_string(input_str):
    strip_str = ''.join([item.strip() for item in input_str.split()])
    # split it into parts
    parts = []
    cur_part = ''
    bracket_balance = 0
    for i in strip_str:
        if i == '(':
            if bracket_balance == 0:
                if cur_part:
                    parts.append(cur_part)
                    cur_part = '('
                else:
                    cur_part += '('
            else:
                cur_part += '('
            bracket_balance += 1
        elif i == ')':
            if bracket_balance - 1 == 0:
                if cur_part:
                    parts.append(cur_part+')')
                    cur_part = ''
            else:
                cur_part += ')'
            bracket_balance -= 1
        else:
            cur_part += i
    if cur_part:
        parts.append(cur_part)
    final_parts = []
    for part in parts:
        if part.startswith('('):
            final_parts.append(part)
        else:
            final_parts += list(part)
    if len(final_parts) == 1:
        final_parts = split_string(final_parts[0][1:-1])
    return final_parts


def operation_order_part2(input_str):
    # the idea for part2 is to basically add parentheses to add operator
    # but it's easy said than done ....
    final_parts = split_string(input_str)
    result = 0
    idx_plus = [idx for idx, item in enumerate(final_parts) if item == '+']
    # find consecutive groups
    if idx_plus:
        idx_groups = []
        min_idx = idx_plus[0]
        max_idx = idx_plus[0]
        for i in range(1, len(idx_plus)):
            if idx_plus[i] - idx_plus[i - 1] == 2:
                max_idx = idx_plus[i]
            else:
                idx_groups.append((min_idx, max_idx))
                min_idx = idx_plus[i]
                max_idx = idx_plus[i]
        idx_groups.append((min_idx, max_idx))

        for group in idx_groups:
            id1 = group[0] - 1
            id2 = group[1] + 1
            final_parts[id1] = '(' + final_parts[id1]
            final_parts[id2] = final_parts[id2] + ')'
        final_str = ''.join(final_parts)
        final_parts = split_string(final_str)

    for i in range(int((len(final_parts) - 1) / 2)):
        idx = 2 * i + 1
        left = final_parts[idx - 1] if idx == 1 else result
        left = int(str(left)) if str(
            left,
        ).isdigit() else operation_order_part2(left)
        right = final_parts[idx + 1]
        right = int(str(right)) if str(
            right,
        ).isdigit() else operation_order_part2(right)
        if final_parts[idx] == '+':
            result = left + right
        if final_parts[idx] == '*':
            result = left * right

    return result


def homework(input_str):
    lines = [line for line in input_str.split('\n') if line]

    result_part1 = sum([operation_order(line) for line in lines])
    result_part2 = sum([operation_order_part2(line) for line in lines])
    return result_part1, result_part2


def main():
    with open('./input_folder/day18.txt', encoding='UTF-8') as fh:
        input_text = fh.read()

    part1, part2 = homework(input_text)
    # part1
    assert part1 == 6923486965641
    # part2
    assert part2 == 70722650566361
    print('success!!')


if __name__ == '__main__':
    main()
