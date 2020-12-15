'''
Advent of Code 2020 Day 11
Jana Goodman

TODO: This pretty icky looking
      maybe rethink for later
'''
import simplegrid

class Waiting:
    EMPTY_SEAT = 'L'
    OCCUPIED = '#'
    FLOOR = '.'

    def __init__(self, grid):
        self.grid = grid
        self.width = self.grid.width
        self.height = self.grid.height

    def is_empty_seat(self, x, y):
        return self.grid.get_display(x, y) == self.EMPTY_SEAT

    def is_occupied(self, x, y):
        return self.grid.get_display(x, y) == self.OCCUPIED

    def is_floor(self, x, y):
        return self.grid.is_clear(x, y)

    def neighbors_occupied(self, x, y):
        return sum([1 if self.is_occupied(x, y) else 0
                    for x, y in
                        self.grid.get_neighbors(x, y, self.OCCUPIED, True)])

    def get_seat(self, x, y):
        return self.grid.get_display(x, y)

    def set_seat(self, x, y, ch):
        self.grid.set_display(x, y, ch)

    def apply_rule(self, x, y, rule=1):
        if self.is_floor(x, y):
            return None
        if rule == 1:
            occupied = self.neighbors_occupied(x, y)
        else:
            occupied = self.visible_occupied_seats(x, y)
        if self.is_empty_seat(x, y):
            if occupied == 0:
                return self.OCCUPIED
            else:
                return self.EMPTY_SEAT
        else:
            mx_occ = 4
            if rule == 2:
                mx_occ = 5
            if occupied >= mx_occ:
                return self.EMPTY_SEAT
            else:
                return self.OCCUPIED

    def cycle(self, rule=1):
        new_area = Waiting(simplegrid.SimpleGrid(self.width, self.height))
        for y in range(0, self.height):
            for x in range(0, self.width):
                new_seat = self.apply_rule(x, y, rule)
                if new_seat != None:
                    new_area.set_seat(x, y, new_seat)
        return new_area

    def get_grid(self):
        return self.grid

    def occupied_seats(self):
        return sum([1 if self.is_occupied(x, y) else 0
                    for x in range(0, self.width)
                    for y in range(0, self.height)])

    def visible_up(self, x, y_start):
        for y in range(y_start, 0, -1):
            if y != y_start:
                if self.is_occupied(x, y):
                    return 1
                elif self.is_empty_seat(x, y):
                    return 0
        return 0

    def visible_right_up(self, x_start, y_start):
        x, y = x_start + 1, y_start - 1
        while x < self.width and y > 0:
            if self.is_occupied(x, y):
                return 1
            elif self.is_empty_seat(x, y):
                return 0
            x += 1
            y -= 1
        return 0

    def visible_right(self, x_start, y):
        for x in range(x_start, self.width - 1):
            if x != x_start:
                if self.is_occupied(x, y):
                    return 1
                elif self.is_empty_seat(x, y):
                    return 0
        return 0

    def visible_right_down(self, x_start, y_start):
        x, y = x_start + 1, y_start + 1
        while x < self.width and y < self.height - 1:
            if self.is_occupied(x, y):
                return 1
            elif self.is_empty_seat(x, y):
                return 0
            x += 1
            y += 1
        return 0

    def visible_down(self, x, y_start):
        for y in range(y_start, self.height - 1):
            if y != y_start:
                if self.is_occupied(x, y):
                    return 1
                elif self.is_empty_seat(x, y):
                    return 0
        return 0

    def visible_left_down(self, x_start, y_start):
        x, y = x_start - 1, y_start + 1
        while x > 0 and y < self.height - 1:
            if self.is_occupied(x, y):
                return 1
            elif self.is_empty_seat(x, y):
                return 0
            x -= 1
            y += 1
        return 0

    def visible_left(self, x_start, y):
        for x in range(x_start, 0, -1):
            if x != x_start:
                if self.is_occupied(x, y):
                    return 1
                elif self.is_empty_seat(x, y):
                    return 0
        return 0

    def visible_left_up(self, x_start, y_start):
        x, y = x_start - 1, y_start - 1
        while x > 0 and y > 0:
            if self.is_occupied(x, y):
               return 1
            elif self.is_empty_seat(x, y):
                return 0
            x -= 1
            y -= 1
        return 0

    def visible_occupied_seats(self, x, y):
        result = 0
        result += self.visible_up(x, y)
        result += self.visible_right_up(x, y)
        result += self.visible_right(x, y)
        result += self.visible_right_down(x, y)
        result += self.visible_down(x, y)
        result += self.visible_left_down(x, y)
        result += self.visible_left(x, y)
        result += self.visible_left_up(x, y)
        return result

    def __eq__(self, other):
        return self.grid == other.grid

    def __repr__(self):
        return str(self.grid)

def get_data(file_name):
    def parse_line(string):
        return string

    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(parse_line(line.strip()))
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def part1(grid):
    waiting_area = Waiting(grid).cycle()
    while True:
        new_area = waiting_area.cycle()
        if new_area == waiting_area:
            return waiting_area.occupied_seats()
        waiting_area = Waiting(new_area.get_grid())

def part2(grid):
    waiting_area = Waiting(grid).cycle(2)
    print(waiting_area)
    while True:
        new_area = waiting_area.cycle(2)
        if new_area == waiting_area:
            return waiting_area.occupied_seats()
        waiting_area = Waiting(new_area.get_grid())

def main():
    data = get_data('aoc11.txt')
    width = len(data[0])
    height = len(data)
    grid = simplegrid.SimpleGrid(width, height, data)
    grid.add_border('.')

    # Part 1
    print(f'PART 1--Answer: {part1(grid)}')

    # Part 2
    print(f'PART 2--Answer: {part2(grid)}')

if __name__ == '__main__':
    main()
