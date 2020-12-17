'''
Advent of Code 2020 Day 17
Jana Goodman

'''
import itertools


def get_data(file_name):
    def parse_line(string):
        return string

    data = []
    try:
        for line in open(file_name, 'r').readlines():
            data.append(parse_line(line.strip()))
        return data
    except FileNotFoundError:
        print(f'File {file_name} not found.')


def get_actives(data, act_ch, dim=3):
    return set((x, y, 0) if dim == 3 else (x, y, 0, 0)
               for x in range(0, len(data))
               for y in range(0, len(data))
               if data[y][x] == act_ch)


def active_neighbors(pt0, actives):
    return len([True for pt in
                itertools.product(*[(x - 1, x, x + 1) for x in pt0])
                if pt != pt0 and pt in actives])


def stay_or_set_active(pt, actives):
    if pt in actives:
        if active_neighbors(pt, actives) in {2, 3}:
            return True
    else:
        if active_neighbors(pt, actives) == 3:
            return True
    return False


def active_count(actives, sz, cycles, dim=3):
    start, end = -1, sz + 1
    for cycle in range(0, cycles):
        actives = set(_ for _ in set(pt for pt in
                                     itertools.product(*[range(start, end) for _ in range(0, dim)])
                                     if stay_or_set_active(pt, actives)))
        start -= 1
        end += 1
    return len(actives)


def main():
    initial = get_data('aoc17.txt')

    # Part 1
    actives = get_actives(initial, '#')
    print(f'PART 1--Answer: {active_count(actives, len(initial), 6)}')

    # Part 2

    actives = get_actives(initial, '#', 4)
    print(f'PART 2--Answer: {active_count(actives, len(initial), 6, 4)}')


if __name__ == '__main__':
    main()
