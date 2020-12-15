'''
Advent of Code 2020 Day 3
Jana Goodman

TODO: make this code better
'''


def get_data(file_name):
    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(line.strip())
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')


def toboggan_ride(arr, dx, dy):
    result = 0
    height = len(arr)
    width = len(arr[0])
    x, y = 0, 0
    while True:
        y += dy
        if y >= height:
            break
        x += dx
        if x >= width:
            x %= width
        if arr[y][x] == '#':
            result += 1
    return result


def part1(arr):
    return toboggan_ride(arr, 3, 1)


def part2(arr):
    result = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        result *= toboggan_ride(arr, dx, dy)
    return result


def main():
    grid = get_data('aoc03.txt')
    print(grid)

    # Part 1

    print(f'PART 1--Answer: {part1(grid)}')

    # Part 2
    print(f'PART 2--Answer: {part2(grid)}')


if __name__ == '__main__':
    main()
