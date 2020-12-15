'''
Advent of Code 2020 Day 14
Jana Goodman


'''
import re
import collections
import itertools

def get_data(file_name):
    def parse_line(string):
        t = string.split(' = ')
        if t[0] == 'mask':
            return t[1]
        addr = int(re.sub('\D', '', t[0]))
        val = int(t[1])
        return addr, val

    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(parse_line(line.strip()))
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def is_mask(x):
    return not type(x) is tuple

def mask_value(m, v):
    bin_v = bin(v)[2:].rjust(36, '0')
    new_v = ''
    for vch, mch in zip(bin_v, m):
        if mch == 'X':
            new_v += vch
        else:
            new_v += mch
    return int(new_v, 2)

def part1(program):
    memory = collections.defaultdict(lambda: 0)
    for line in program:
        if is_mask(line):
            mask = line
        else:
            addr, val = line
            memory[addr] = mask_value(mask, val)
    return sum(memory.values())

def mask_address(mask, a):
    bin_a = bin(a)[2:].rjust(36, '0')
    new_mask = ''
    for ach, mch in zip(bin_a, mask):
        if mch == '0':
            new_mask += ach
        else:
            new_mask += mch
    return new_mask

def addresses(mask):
    result = []
    k = mask.count('X')
    repl_xs = [bin(_)[2:].rjust(k, '0') for _ in range(0, 2**k)]
    for b in repl_xs:
        addr = []
        b_ptr = 0
        for mch in mask:
            if mch == 'X':
                addr += b[b_ptr]
                b_ptr += 1
            else:
                addr += mch
        result.append(int(''.join(addr), 2))
    return result

def part2(program):
    memory = collections.defaultdict(lambda: 0)
    for line in program:
        if is_mask(line):
            mask = line
        else:
            addr, val = line
            for a in addresses(mask_address(mask, addr)):
                memory[a] = val
    return sum(memory.values())

def main():
    program = get_data('aoc14.txt')
    print(program)

    # Part 1
#    print(f'PART 1--Answer: {part1(program)}')

    # Part 2
    print(f'PART 2--Answer: {part2(program)}')

if __name__ == '__main__':
    main()
