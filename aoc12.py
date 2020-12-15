'''
Advent of Code 2020 Day 12
Jana Goodman

'''
class Ferry:
    def __init__(self, x, y, heading, course, rule=1):
        self.x = 0
        self.y = 0
        self.directions = {'E': (1, 0), 'S': (0, 1), 'W': (-1, 0), 'N': (0, -1)}
        self.heading = heading
        self.dx = self.directions[heading][0]
        self.dy = self.directions[heading][1]
        self.course = [_ for _ in course]
        if rule == 2:
            self.waypt = Waypoint(10, 1)

    def change_position(self, x, y):
        self.x += x
        self.y += y

    def turn(self, degrees):
        headings = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for _ in range(0, degrees // 90):
            ndx =  headings.index((self.dx, self.dy))
            self.dx, self.dy = headings[(ndx + 1) % 4]

    def follow_instruction(self, action, value, rule=1):
        if rule == 2:
            self.follow_instruction_part_2(action, value)
            return
        if action == 'F':
            self.change_position(value * self.dx, value * self.dy)
        elif action == 'R':
            self.turn(value)
        elif action == 'L':
            self.turn(360 - value)
        else:
            save_x, save_y = self.dx, self.dy
            self.dx, self.dy = self.directions[action]
            self.change_position(value * self.dx, value * self.dy)
            self.dx, self.dy = save_x, save_y

    def follow_instruction_part_2(self, action, value):
        if action == 'F':
            for _ in range(0, value):
                self.change_position(self.waypt.x, self.waypt.y)
                self.waypt.reset(self.x, self.y)
        elif action in 'RL':
            self.waypt.rotate(action, value)
        else:
            for _ in range(0, value):
                self.waypt.move(action, value)
        print(action, value, self.x, self.y, self.waypt.x, self.waypt.y)

    def follow_course(self, rule=1):
        for action, value in self.course:
            self.follow_instruction(action, value, rule)

    def manhattan_position(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f'({self.x}, {self.y}) heading: {self.dx},{self.dy}'

class Waypoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_offset = x
        self.y_offset = y

    def move(self, dir, value):
        if dir == 'E':
            self.x += value
        elif dir == 'S':
            self.y += value
        elif dir == 'W':
            self.x -= value
        elif dir == 'N':
            self.y -= 1

    def reset(self, x, y):
        self.x = x + self.x_offset
        self.y = y + self.y_offset

    def rotate(self, rl, degrees):
        if rl == 'R':
            if degrees == 90:
                self.x_offset, self.y_offset = self.y_offset, self.x_offset
            elif degrees == 180:
                self.x_offset, self.y_offset = -self.x_offset, self.y_offset
            elif degrees == 270:
                self.x_offset, self.y_offset = self.y_offset, -self.x_offset
        else:
            if degrees == 90:
                self.x_offset, self.y_offset = self.y_offset, -self.x_offset
            elif degrees == 180:
                self.x_offset, self.y_offset = -self.x_offset, self.y_offset
            elif degrees == 270:
                self.x_offset, self.y_offset = self.y_offset, self.x_offset

    def __repr__(self):
        return f'({self.x}, {self.y}) heading: {self.dx},{self.dy}'

def get_data(file_name):
    def parse_line(string):
        return (string[0], int(string[1:]))

    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(parse_line(line.strip()))
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def part1(ferry):
    ferry.follow_course()
    return ferry.manhattan_position()

def part2(ferry):
    ferry.follow_course(2)
    return ferry.manhattan_position()

def main():
#    ferry = Ferry(0, 0, 'E', get_data('aoc12.txt'))

    # Part 1
#    print(f'PART 1--Answer: {part1(ferry)}')

    # Part 2
    ferry = Ferry(0, 0, 'E', get_data('aoc12.txt'), 2)
    print(f'PART 2--Answer: {part2(ferry)}')

if __name__ == '__main__':
    main()
