import re


def parse_rule(rule_str):
    parts = rule_str.split('bag')
    k_part = parts[0].strip()
    v_parts = {}
    for part in parts[1:]:
        marker = re.search('[0-9]+', part)
        if not marker:
            continue
        num = marker[0]
        b_col = part.split(num)[1].strip()
        v_parts[b_col] = num
    return k_part, v_parts


def process_rules(input_str):
    contain_dict = {}
    for line in input_str.split('\n'):
        if not line:
            continue
        k, v = parse_rule(line)
        contain_dict[k] = v
    return contain_dict


def find_child_node(query, contain_dict):
    entry = contain_dict[query]
    if not entry:
        return 0
    return sum([
        int(value)*(find_child_node(key, contain_dict)+1)
        for key, value in contain_dict[query].items()
    ])


def find_contains(query, contain_dict, bags):
    # find the keys
    parent_nodes = [
        key for key, value in contain_dict.items()
        if query in value
    ]
    bags += parent_nodes
    if not parent_nodes:
        return bags
    for node in parent_nodes:
        bags = find_contains(node, contain_dict, bags)
    return bags


def main():
    with open('./input_folder/day7.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    rule_dict = process_rules(input_text)
    # part1
    assert len(set(find_contains('shiny gold', rule_dict, []))) == 226
    # part2
    assert find_child_node('shiny gold', rule_dict) == 9569
    print('success!!')


if __name__ == '__main__':
    main()
