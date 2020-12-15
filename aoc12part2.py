'''
Advent of Code 2020 Day 12
Jana Goodman

TODO: combine into single py file
      make classes better
      clean up code
'''
class Ship:
    def __init__(self, x, y, heading, course):
        self.x = 0
        self.y = 0
        self.heading = heading
        self.course = [_ for _ in course]
        self.waypt_x = 10
        self.waypt_y = 1
        self.rel_x = 10
        self.rel_y = 1

    def move(self, delta):
        (mult_x, mult_y) = self.heading
        if mult_x == 0:
            mult_x = 1
        self.x += delta * mult_x * self.rel_x
        if mult_y == 0:
            mult_y = 1
        self.y += delta * mult_y * self.rel_y
        self.reset_waypoint()

    def move_waypoint(self, dir, delta):
        if dir == 'E':
            self.waypt_x += delta
            self.rel_x += delta
        elif dir == 'S':
            self.waypt_y -= delta
            self.rel_y -= delta
        elif dir == 'W':
            self.waypt_x -= delta
            self.rel_x -= delta
        elif dir == 'N':
            self.waypt_y += delta
            self.rel_y += delta

    def reset_waypoint(self):
        self.waypt_x = self.x + self.rel_x
        self.waypt_y = self.y + self.rel_y

    def rotate_waypoint(self, degrees):
        for _ in range(0, degrees // 90):
            self.rel_x, self.rel_y = self.rel_y, -self.rel_x
        self.reset_waypoint()

    def follow_instruction(self, action, value):
        if action == 'F':
            self.move(value)
        elif action == 'R':
            self.rotate_waypoint(value)
        elif action == 'L':
            self.rotate_waypoint(360 - value)
        else:
            self.move_waypoint(action, value)


    def follow_course(self):
        for action, value in self.course:
            self.follow_instruction(action, value)

    def manhattan_position(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f'({self.x}, {self.y}) heading: {self.heading}'

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

def part2(ferry):
    ferry.follow_course()
    return ferry.manhattan_position()

def main():
    # Part 2
    ferry = Ship(0, 0, (1, 0), get_data('aoc12.txt'))
    print(f'PART 2--Answer: {part2(ferry)}')

if __name__ == '__main__':
    main()
