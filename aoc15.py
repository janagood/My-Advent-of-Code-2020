'''
Advent of Code 2020 Day 15
Jana Goodman


'''
import re
import collections

def part1(starts, end_turn):
    spokens = collections.defaultdict(lambda: [])
    for ptr, start in enumerate(starts, 1):
        spokens[start].append(ptr)
    turn = len(starts) + 1
    last = starts[-1]
    while True:
        if len(spokens[last]) == 1:
            last = 0
            spokens[0].append(turn)
        else:
                new_last = spokens[last][1] - spokens[last][0]
                spokens[last].pop(0)
                last = new_last
                spokens[last].append(turn)
#        print(turn, last)
        if turn % 1000000 == 0:
            print(turn)
        if turn == end_turn:
            return last
        turn += 1

def main():
    starts = [19,20,14,0,9,1]

    # Part 1
    print(f'PART 1--Answer: {part1(starts, 2020)}')

    # Part 2
    print(f'PART 2--Answer: {part1(starts, 30000000)}')

if __name__ == '__main__':
    main()
