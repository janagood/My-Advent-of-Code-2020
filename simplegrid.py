'''

simple grid rows/columns of characters

'''

class SimpleGrid:
    def __init__(self, width, height, display=None, BLANK='.'):
        self.width = width
        if display != None:
# lengths of lines vary
            self.width = max(len(line) for line in display)
        self.height = height
        self.BLANK = BLANK
        self.grid = [[BLANK for x in range(0, self.width)]
                            for y in range(0, self.height)]
        if display != None:
            for y in range(0, self.height):
                for x in range(0, len(display[y])):
                    self.set_display(x, y, display[y][x])

    def set_display(self, x, y, ch):
        self.grid[y][x] = ch

    def get_display(self, x, y):
        return self.grid[y][x]

    def get_neighbors(self, x, y, chk, diag=False):
        if diag:
            neighbors = [(x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1),
                         (x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
        else:
            neighbors = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
        return [(x2, y2) for x2, y2 in neighbors
                if self.get_display(x2, y2) == chk]

    def is_clear(self, x, y):
        return self.get_display(x, y) == self.BLANK

    def count(self, ch):
        return sum(1 for x in range(0, self.width)
                       for y in range(0, self.height)
                     if self.get_display(x, y) == ch)

    def add_border(self, ch):
        for y in range(0, self.height):
            self.grid[y] = [ch] + self.grid[y] + [ch]
        self.width += 2
        border = [ch] * self.width
        self.grid = [border] + self.grid + [border]
        self.height += 2

    def __eq__(self, other):
        if (self.width != other.width
            or self.height != other.height):
            return False
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.get_display(x, y) != other.get_display(x, y):
                    return False
        return True


    def __repr__(self):
        result = ''
        for row in self.grid:
            result += ''.join(row) + '\n'
        return result
