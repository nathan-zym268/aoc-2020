# day13
def first_bus(input_str):
    lines = [line for line in input_str.split('\n') if line]
    start_timestamp = int(lines[0].strip())
    bus_ids = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    i = 0
    while i < 10000000:
        for bus in bus_ids:
            if (start_timestamp + i) % bus == 0:
                return i * bus
        i += 1


def bus_sequence(input_str):
    # my best try for an iterative approach, but it won't finish...
    lines = [line for line in input_str.split('\n') if line]
    bus_ids = [bus for bus in lines[1].split(',')]
    max_bus = max([int(bus) for bus in lines[1].split(',') if bus != 'x'])
    max_bus_idx = bus_ids.index(str(max_bus))
    bus_id_valid = [
        (idx-max_bus_idx, int(bus))
        for idx, bus in enumerate(bus_ids) if bus != 'x'
    ]
    bus_id_valid.sort(key=lambda x: x[1], reverse=True)
    i = 0
    start = int(max_bus)
    while i < 100000000000000:
        i += 1
        for idx, bus in bus_id_valid[1:]:
            if not (start*i+idx) % bus:
                continue
            else:
                break
        else:
            return i*start-max_bus_idx


def main():
    with open('./input_folder/day13.txt', encoding='UTF-8') as fh:
        input_text = fh.read()
    # part1
    assert first_bus(input_text) == 2298
    # part2 maybe implement crt solution later
    print('success!!')


if __name__ == '__main__':
    main()
