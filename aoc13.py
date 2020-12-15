'''
Advent of Code 2020 Day 13
Jana Goodman

'''
import math

def get_data(file_name):
    def parse_line(string):
        if ',' in string:
            return [int(_) if _ != 'x' else 'x' for _ in list(string.split(','))]
        return int(string)

    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(parse_line(line.strip()))
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def part1(arrive, busses):
    min_time = 10 ** 20
    for bus_id in busses:
        if bus_id == 'x':
            continue
        time = arrive - (arrive % bus_id) + bus_id
        if min_time > time:
            min_time = time
            min_bus = bus_id
    return min_bus * (min_time - arrive)

def mod_inverse(a, m):
    return pow(a, m - 2, m)

def solve(ais, mis):
    N = math.prod(mis)
    nis = [N // _ for _ in mis]
    his = [mod_inverse(ni, mi) for ni, mi in zip(nis, mis)]
    return sum((hi * ni * ai) % N
               for hi, ni, ai in zip(his, nis, ais)) % N

def part2(busses):
# using method for solving system of linear congruences
#   NOTE: all the bus_ids are prime -- much easier
#         Fermat's little theorem
# t == ai mod mi where for this problem:
# mi is bus_id
# bus_id - minutes after 0
    bus_ids = []
    minutes = []
    for minute, bus_id in enumerate(busses):
        if bus_id != 'x':
            bus_ids.append(bus_id)
            minutes.append(bus_id - minute)
    minutes[0] = 0
    return solve(minutes, bus_ids)

def main():
    time, busses = get_data('aoc13.txt')

    # Part 1
    print(f'PART 1--Answer: {part1(time, busses)}')

    # Part 2
    print(f'PART 2--Answer: {part2(busses)}')

if __name__ == '__main__':
    main()
