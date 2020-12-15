'''
Advent of Code 2020 Day 1
Jana Goodman

'''
import time

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


def part1(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == 2020:
                return arr[i], arr[j]

def part2(arr):
    for i in range(0, len(arr) - 2):
        if arr[i] >= 2020:
            continue
        for j in range(i, len(arr) - 1):
            sum1 = arr[i] + arr[j]
            if sum1 >= 2020:
                continue
            for k in range(j, len(arr)):
                sum2 = sum1 + arr[k]
                if sum2 == 2020:
                    return arr[i], arr[j], arr[k]


def main():
    expenses = get_data('aoc01.txt')

    x, y = part1(expenses)
    print(f'PART 1--Expenses: {x} + {y} == 2020 with product: {x * y}')

    # Part 1

    # Part 2
    x, y, z = part2(expenses)
    print(f'PART 2--Expenses: {x} + {y} + {z} == 2020 with product: {x * y * z}')

if __name__ == '__main__':
    main()
