'''

Advent of Code 2020 Day 23
Jana Goodman

'''


class Circle:
    def __init__(self, cups, mx=9):
        self.__cups__ = list(map(int, cups))
        self.__curr_cup__ = self.__cups__[0]
        self.__mx__ = mx
        self.__next_cups__ = self.__load_nexts__()

    def move(self):
        cups3 = self.__next3__()
        next_cup = self.__next_cups__[cups3[-1]]
        dest_cup = self.__get_dest_cup__(cups3)
        self.__next_cups__[self.__curr_cup__] = next_cup
        self.__next_cups__[cups3[-1]] = self.__next_cups__[dest_cup]
        self.__next_cups__[dest_cup] = cups3[0]
        self.__curr_cup__ = next_cup

    def cups_after1(self):
        result = ''
        cup = 1
        while True:
            cup = self.__next_cups__[cup]
            if cup == 1:
                return result
            result += str(cup)

    def cw_cup1_prod(self):
        c1 = self.__next_cups__[1]
        c2 = self.__next_cups__[c1]
        return c1 * c2

    def __next3__(self):
        c1 = self.__next_cups__[self.__curr_cup__]
        c2 = self.__next_cups__[c1]
        c3 = self.__next_cups__[c2]
        return [c1, c2, c3]

    def __get_dest_cup__(self, arr):
        dest_cup = self.__curr_cup__ - 1
        while True:
            if dest_cup == 0:
                dest_cup = self.__mx__
            if dest_cup not in arr:
                return dest_cup
            dest_cup -= 1

    def __load_nexts__(self):
        def after(n):
            return (self.__cups__.index(n) + 1) % clen

        clen = len(self.__cups__)
        nexts = [0] + [self.__cups__[after(i)]
                       for i in range(1, clen + 1)]
        if self.__mx__ == 9:
            return nexts

        # for part 2:
        #   put 11..1000001 into the circle
        #   10 now follows the 'last cup' (one before current cup)
        #   current cup now follows 1000000 (in place of 1000001)
        nexts.extend(range(len(self.__cups__) + 2, self.__mx__ + 2))
        nexts[int(self.__cups__[-1])] = len(self.__cups__) + 1
        nexts[self.__mx__] = self.__curr_cup__
        return nexts


def part1(circle, moves):
    for _ in range(0, moves):
        circle.move()
    return circle.cups_after1()


def part2(circle, moves):
    for _ in range(0, 10 * moves):
        circle.move()
    return circle.cw_cup1_prod()


def main():
    # test input
    #    input = '389125467'
    # actual input
    incircle = '872495136'

    moves = 100
    circle = Circle(incircle)
    print(f'PART 1--Labels cw from cup1: {part1(circle, moves)}')

    moves = 1000000
    circle = Circle(incircle, moves)
    print(f'PART 2--Product of two cups cw from cup1: {part2(circle, moves)}')


if __name__ == '__main__':
    main()
