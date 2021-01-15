'''
Advent of Code 2020 Day 20
Jana Goodman


'''
import re
import math
import simplegrid

SIZE = 10

class Tile:
    def __init__(self, id, grid):
        self.id = id
        self.grid = [s for s in grid]
        self.width, self.height = len(grid[0]), len(grid)
        self.up, self.right, self.down, self.left = self.get_edges()
# used for arranging the tiles
        self.match_up, self.match_right, self.match_down, self.match_left = None, None, None, None
        self.visited = False

    def flip(self, s):
        return s[::-1]

    def int_repr(self, s):
        return int(s.replace('.','0').replace('#','1'), 2)

    def get_row(self, y):
        return self.int_repr(self.grid[y])

    def get_col(self, x):
        return ''.join([g for g in [self.grid[_][x]
                    for _ in range(0, self.height)]])

    def get_edges(self):
        # up, right, down, left
        result = []
        s = self.grid[0]
        result.append((self.int_repr(s), self.int_repr(self.flip(s))))
        s = self.get_col(self.width - 1)
        result.append((self.int_repr(s), self.int_repr(self.flip(s))))
        s = self.grid[self.height - 1]
        result.append((self.int_repr(self.flip(s)), self.int_repr(s)))
        s = self.get_col(0)
        result.append((self.int_repr(self.flip(s)), self.int_repr(s)))
        return result

    def matches(self):
        return sum(0 if m == None else 1
                   for m in [self.match_up, self.match_right,
                             self.match_down, self.match_left])

    def __repr__(self):
        return f'Tile: {self.id}'

def get_data(file_name):
    result = []
    try:
        grid, id = [], 0
        for line in open(file_name, 'r').readlines():
            s = line.strip()
            if len(s) == 0:
                continue
            if 'Tile' in s:
                id = int(re.findall('\d+', s)[0])
                grid = []
                continue
            grid.append(s)
            if len(grid) == SIZE:
                result.append(Tile(id, grid))
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def part1(tiles):
    # matches for each tile are unique:
    #   so once a match is put into a tile,
    #   there is no need to check for more

    #  corners match uniquely to exactly two other tiles
    #  border tiles match to three
    #  interior tiles match to four
    # TODO: find cool way to shorten this -- probably some loop thru sides

    # sort of a DFS
    queue = [tiles[0]]
    while len(queue) > 0:
        t1 = queue.pop(0)
        if t1.visited:
            continue
        t1.visited = True

        for t2 in [t for t in tiles if t.id != t1.id and not t.visited]:
            if t1.match_up == None:
                up = t1.up[0]
# check edge and the reverse
                if up in t2.up:
                    t1.match_up, t2.match_up = t2, t1
                    queue.append(t2)
                elif up in t2.right:
                    t1.match_up, t2.match_right = t2, t1
                    queue.append(t2)
                elif up in t2.down:
                    t1.match_up, t2.match_down = t2, t1
                    queue.append(t2)
                elif up in t2.left:
                    t1.match_up, t2.match_left = t2, t1
                    queue.append(t2)

            if t1.match_right == None:
                right = t1.right[0]
                if right in t2.up:
                    t1.match_right, t2.match_up = t2, t1
                    queue.append(t2)
                elif right in t2.right:
                    t1.match_right, t2.match_right = t2, t1
                    queue.append(t2)
                elif right in t2.down:
                    t1.match_right, t2.match_down = t2, t1
                    queue.append(t2)
                elif right in t2.left:
                    t1.match_right, t2.match_left = t2, t1
                    queue.append(t2)

            if t1.match_down == None:
                down = t1.down[0]
                if down in t2.up:
                    t1.match_down, t2.match_up = t2, t1
                    queue.append(t2)
                elif down in t2.right:
                    t1.match_down, t2.match_right = t2, t1
                    queue.append(t2)
                elif down in t2.down:
                    t1.match_down, t2.match_down = t2, t1
                    queue.append(t2)
                elif down in t2.left:
                    t1.match_down, t2.match_left = t2, t1
                    queue.append(t2)

            if t1.match_left == None:
                left = t1.left[0]
                if left in t2.up:
                    t1.match_left, t2.match_up = t2, t1
                    queue.append(t2)
                elif left in t2.right:
                    t1.match_left, t2.match_right = t2, t1
                    queue.append(t2)
                elif left in t2.down:
                    t1.match_left, t2.match_down = t2, t1
                    queue.append(t2)
                elif left in t2.left:
                    t1.match_left, t2.match_left = t2, t1
                    queue.append(t2)

    return math.prod(t.id for t in tiles if t.matches() == 2)
'''
sea monster
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''
def part2(tiles):
    # get grid of tiles arranged correctly
    # take of the borders of each tile
    # remove blanks
    # then look for sea monster
    # where sea monster is put in 0's
    # answer is how many #'s there are

    return None

def main():
# actual data is a 12 x 12
    tiles = get_data('aoc20final.txt')

    # Part 1
    print(f'PART 1--Product of corner tiles: {part1(tiles)}')

    # Part 2
#    print(f'PART 2--{part2(tiles)}')


if __name__ == '__main__':
    main()
# answer should be 32287787075651
# answer tiles: 1621 3547 3389 1657