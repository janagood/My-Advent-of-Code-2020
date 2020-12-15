'''
Advent of Code 2020 Day 2
Jana Goodman

'''
import re


def get_data(file_name):
    def parse_line(string):
        # 1-13 r: gqdrspndrpsrjfjx
        policy = string.split(': ')[0]
        password = string.split(': ')[1]
        letter = policy[-1]
        [low, high] = list(map(int, re.findall('\d+', policy.split(' ')[0])))
        return low, high, letter, password

    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(parse_line(line.strip()))
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')


def is_good(lo, hi, ltr, pw):
    return lo <= pw.count(ltr) <= hi


def part1(arr):
    return [is_good(low, high, letter, password)
            for low, high, letter, password in arr].count(True)


def is_really_good(x, y, ltr, pw):
    return [pw[x - 1] == ltr, pw[y - 1] == ltr].count(True) == 1


def part2(arr):
    return [is_really_good(i, j, letter, password)
            for i, j, letter, password in arr].count(True)


def main():
    lines = get_data('aoc02.txt')
    print(lines)
    # Part 1
    print(f'PART 1--Number of good passwords: {part1(lines)}')

    # Part 2
    print(f'PART 2--Number of good passwords: {part2(lines)}')


if __name__ == '__main__':
    main()
