'''
Advent of Code 2020 Day 5
Jana Goodman

'''

class BoardingPass:
    FRONT = 'F'
    BACK = 'B'
    LEFT = 'L'
    RIGHT = 'R'

    def __init__(self, string):
        self.string = string
        self.row = self.decode(self.string[0:7], self.FRONT)
        self.col = self.decode(self.string[7:], self.LEFT)
        self.id = self.row * 8 + self.col

    def decode(self, string, first_half):
        n = len(string)
        low, high = 0, pow(2, n) - 1
        offset = pow(2, n - 1)
        for ch in string:
            if ch == first_half:
                high -= offset
            else:
                low += offset
            offset //= 2
        return low

    def at_front(self):
        return self.row == 0

    def at_back(self):
        return self.row == 127

def get_data(file_name):
    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(BoardingPass(line.strip()))
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def part1(passes):
    return max([_.id for _ in passes])

def part2(passes):
    max_seat = 908
    filled = [_.id for _ in passes
              if not _.at_front() and not _.at_back()]
    filled.sort()
    for x, y in zip(filled[0:-1], filled[1:]):
        if y - x > 1:
            return x + 1

def main():
    data = get_data('aoc05.txt')

    # Part 1

    print(f'PART 1--Answer: {part1(data)}')

    print(f'PART 2--Answer: {part2(data)}')

if __name__ == '__main__':
    main()
