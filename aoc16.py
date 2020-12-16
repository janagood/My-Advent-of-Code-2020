'''
Advent of Code 2020 Day 16
Jana Goodman

'''
import math

def get_data(file_name):
    def parse_line(string):
        return string

    def really_parse(data):
        fields = dict()
        my_ticket = []
        nearbys = []
        get_mine = False
        get_nearby = False
        for line in data:
            if len(line) == 0:
                continue
            if line == 'your ticket:':
                get_mine = True
            elif line == 'nearby tickets:':
                get_mine = False
                get_nearby = True
                nearbys = []
            elif get_mine:
                my_ticket = list(map(int, line.split(',')))
            elif get_nearby:
                nearbys.append(list(map(int, line.split(','))))
            else:
                [field, ranges] = line.split(': ')
                [range1, range2] = ranges.split(' or ')
                [(x1, x2), (y1, y2)] = range1.split('-'), range2.split('-')
                fields[field] = [(int(x1), int(x2)), (int(y1), int(y2))]
        ranges = [v for w in fields.values() for v in w]
        return fields, my_ticket, nearbys, ranges

    data = []
    try:
        for line in open(file_name, 'r').readlines():
            data.append(parse_line(line.strip()))
    except FileNotFoundError:
        print(f'File {file_name} not found.')
    return really_parse(data)

def is_good_value(x, rs):
    return any(a <= x <= b for a, b in rs)

def part1(fields, nearbys, ranges):
    return sum(v for t in nearbys
              for v in t if not is_good_value(v, ranges))

def part2(fields, my_ticket, nearbys, ranges):
    nearbys = [ticket for ticket in nearbys
               if all(is_good_value(x, ranges)
                      for x in ticket)]

    positions = [set() for _ in fields.keys()]
    for pos in range(0, len(my_ticket)):
        ticket_values = [_[pos] for _ in nearbys]
        for key in fields.keys():
            if all(is_good_value(v, fields[key]) for v in ticket_values):
                positions[pos].add(key)

    field_indices = dict()
    while True:
        for index, possibles in enumerate(positions):
            if len(possibles) == 1:
                key = list(possibles)[0]
                field_indices[key] = index
                for i in range(0, len(positions)):
                    if key in positions[i]:
                        positions[i].remove(key)
        if all(len(_) == 0 for _ in positions):
            break

    return math.prod([my_ticket[index]
                    for field, index in zip(field_indices.keys(), field_indices.values())
                    if field[0:9] == 'departure'])


def main():
    fields, my_ticket, nearbys, ranges = get_data('aoc16.txt')

    # Part 1
    print(f'PART 1--Answer: {part1(fields, nearbys, ranges)}')

    # Part 2
    print(f'PART 2--Answer: {part2(fields, my_ticket, nearbys, ranges)}')


if __name__ == '__main__':
    main()
