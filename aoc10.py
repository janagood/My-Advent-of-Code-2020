'''
Advent of Code 2020 Day 10
Jana Goodman

'''
import itertools
import math

def get_data(file_name):
    def parse_line(string):
        return int(string)

    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(parse_line(line.strip()))
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def part1(adapters):
    difs = [0] * 4
    max_adapter = max(adapters)
    lookup = [False] * (max_adapter + 1)
    for adapter in adapters:
        lookup[adapter] = True
    jolt = 0
    while True:
        for dif in [1, 2, 3]:
            adapter = jolt + dif
            if lookup[adapter]:
                difs[dif] += 1
                jolt = adapter
                break
        if jolt == max_adapter:
            difs[3] += 1
            break
    return difs[1] * difs[3]

def get_skips(arr):
    arr.append(0)
    arr.append(max(arr) + 3)
    arr.sort()
    result = []
    group_len = 0
    for i in range(1, len(arr) - 1):
        if arr[i] - arr[i - 1] == 3 or arr[i + 1] - arr[i] == 3:
            if group_len > 0:
                if group_len == 1:
                    result.append(1)
                elif group_len == 2:
                    result.append(3)
                elif group_len == 3:
                    result.append(6)
                group_len = 0
        else:
            group_len += 1
    return result

def part2(adapters):
    skips = get_skips(adapters)
    result = 1
    for choose in range(1, len(skips) + 1):
        choices = list(itertools.combinations(skips, choose))
        possibilities = list(map(math.prod, choices))
        result += sum(possibilities)
    return result

def main():
    data = get_data('aoc10.txt')

    # Part 1
    print(f'PART 1--Answer: {part1(data)}')

    # Part 2
    print(f'PART 2--Answer: {part2(data)}')

if __name__ == '__main__':
    main()
