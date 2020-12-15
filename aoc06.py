'''
Advent of Code 2020 Day 6
Jana Goodman
'''

import re

def get_data(file_name):
    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(line.strip())
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def get_groups(arr):
    groups = []
    group = []
    for line in arr:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    return groups

def part1(groups):
    result = 0
    for group in groups:
        answers = set()
        for form in group:
            for ch in form:
                answers.add(ch)
        result += len(answers)
    return result

def part2(groups):
    result = 0
    for group in groups:
        answers = [0] * 26
        for form in group:
            for ch in form:
                answers[ord(ch) - ord('a')] += 1
        result += answers.count(len(group))
    return result

def main():
    data = get_data('aoc06.txt')
    data.append('')
    groups = get_groups(data)

    # Part 1
    print(f'PART 1--Answer: {part1(groups)}')

    # Part 2
    print(f'PART 2--Answer: {part2(groups)}')

if __name__ == '__main__':
    main()
