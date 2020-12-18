'''
Advent of Code 2020 Day 18
Jana Goodman

'''


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

def precedence(op, rule=1):
    # rule 1: for this problem + and * have same precedence
    # rule 2: + evaluated before *
    #   no * or / for rules 1 and 2
    # rule 3: normal PEMDAS
    if op not in '+-/*':
        return 0
    if rule == 0:
        if op in '+-':
            return 1
        elif op in '*/':
            return 2
    elif rule == 1:
            return 1
    elif rule == 2:
        if op == '*':
            return 1
        elif op == '+':
            return 2


def do_math(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    if op == '/':
        return x // y


def evaluate(tokens, rule=1):
    values = []
    ops = []
    ptr = 0
    while ptr < len(tokens):
        if tokens[ptr] == ' ':
            ptr += 1
            continue
        if tokens[ptr] == '(':
            ops.append(tokens[ptr])
        elif tokens[ptr].isdigit():
            val = 0
            while ptr < len(tokens) and tokens[ptr].isdigit():
                val = (val * 10) + int(tokens[ptr])
                ptr += 1
            values.append(val)
            ptr -= 1
        elif tokens[ptr] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(do_math(val1, val2, op))
            ops.pop()
        else:
            while (len(ops) != 0 and
                   precedence(ops[-1], rule) >=
                   precedence(tokens[ptr], rule)):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(do_math(val1, val2, op))
            ops.append(tokens[ptr])
        ptr += 1

    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(do_math(val1, val2, op))
    return values[-1]


def part1(problems):
    return sum(evaluate(problem) for problem in problems)


def part2(problems):
    return sum(evaluate(problem, 2) for problem in problems)


def main():
    data = get_data('aoc18.txt')

    # Part 1
    print(f'PART 1--Total of all answers: {part1(data)}')

    # Part 2
    print(f'PART 2--Total of all answers: {part2(data)}')


if __name__ == '__main__':
    main()
