# day 8
def handling_halting(instr):
    acc = 0
    idx = 0
    executed_idx = set()
    while idx < len(instr):
        ins = instr[idx]
        if idx in executed_idx:
            return acc, False
        executed_idx.add(idx)
        if ins.startswith('acc'):
            acc += int(ins.split()[1])
            idx += 1
        elif ins.startswith('nop'):
            idx += 1
        elif ins.startswith('jmp'):
            idx += int(ins.split()[1])
    return acc, True


def fix_console(input_str):
    instr = [item for item in input_str.split('\n') if item]
    possible_fixes = []
    for idx, item in enumerate(instr):
        copy_instr = instr[:]
        if item.startswith('nop'):
            copy_instr[idx] = item.replace('nop', 'jmp')
            possible_fixes.append(copy_instr)
        elif item.startswith('jmp'):
            copy_instr[idx] = item.replace('jmp', 'nop')
            possible_fixes.append(copy_instr)
    for fix in possible_fixes:
        acc, fix = handling_halting(fix)
        if fix:
            return acc


def main():
    with open('./input_folder/day8.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    instr = [item for item in input_text.split('\n') if item]
    assert handling_halting(instr) == (1563, False)
    # part2
    assert fix_console(input_text) == 767
    print('success!!')


if __name__ == '__main__':
    main()
