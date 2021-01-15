'''
Advent of Code 2020 Day 24
Jana Goodman

'''

import collections
import itertools

BLACK = 1
WHITE = 0

# got these from websites googling hex grid
# started w/ www.redblobgames.com/grids/hexagons
DELTAS = [(1, 0), (1, -1), (0, -1),
          (-1, 0), (-1, 1), (0, 1)]


class Floor():
    def __init__(self):
        self.__tiles__ = collections.defaultdict(lambda: 0)
        # reference tile
        self.__tiles__[(0, 0)] = WHITE
        self.__right__, self.__bottom__, self.__left__, self.__top__ = 0, 0, 0, 0

    def __update_bounds__(self, x, y):
        if x > self.__right__:
            self.__right__ = x
        elif x < self.__left__:
            self.__left__ = x
        if y > self.__top__:
            self.__top__ = y
        elif y < self.__bottom__:
            self.__bottom__ = y

    def flip_tile(self, x, y):
        self.__tiles__[(x, y)] = (self.__tiles__[(x, y)] + 1) % 2
        self.__update_bounds__(x, y)

    def get_tile_color(self, x, y):
        return self.__tiles__[(x, y)]

    def black_tiles_count(self):
        return sum(self.__tiles__[t] for t in self.__tiles__)

    def ranges(self):
        return itertools.product(range(self.__left__ - 1, self.__right__ + 2),
                                 range(self.__bottom__ - 1, self.__top__ + 2))

    def black_neighbors(self, x, y):
        return sum(self.__tiles__[(x + dx, y + dy)]
                   for dx, dy in DELTAS
                   if self.__tiles__[(x + dx, y + dy)] == BLACK)


def get_id_messages(file_name):
    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(line.strip())
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')


def part1(id_messages):
    def identify_tile(x0, y0, s):
        d = ''
        x, y = x0, y0
        for ch in s:
            d += ch
            if ch == 'n' or ch == 's':
                continue
            x, y = x + dx_dys[d][0], y + dx_dys[d][1]
            d = ''
        if d != '':
            x, y = x + dx_dys[d][0], y + dx_dys[d][1]
        return x, y

    dx_dys = dict()
    for dir, coord in zip(['e', 'se', 'sw', 'w', 'nw', 'ne'],
                          DELTAS):
        dx_dys[dir] = coord

    floor = Floor()
    for msg in id_messages:
        x, y = identify_tile(0, 0, msg)
        floor.flip_tile(x, y)
    return floor.black_tiles_count(), floor


def part2(days, floor):
    for _ in range(0, days):
        flips = set()
        for x, y in floor.ranges():
            check = floor.black_neighbors(x, y)
            if floor.get_tile_color(x, y) == BLACK:
                if check == 0 or check > 2:
                    flips.add((x, y))
            else:
                if check == 2:
                    flips.add((x, y))
        for x, y in flips:
            floor.flip_tile(x, y)
    return floor.black_tiles_count()


def main():
    id_messages = get_id_messages('aoc24.txt')
    black_tiles, floor = part1(id_messages)
    print(f'PART 1--Number of BLACK tiles: {black_tiles}')
    days = 100
    print(f'PART 2--Number of BLACK tiles: {part2(days, floor)}')


if __name__ == '__main__':
    main()
