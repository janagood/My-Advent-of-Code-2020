'''
Advent of Code 2020 Day 8
Jana Goodman


'''
class Command:
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg
        self.executed = False

    def is_executed(self):
        return self.executed == True

    def set_executed(self, tf):
        self.executed = tf

    def toggle_jmp_nop(self):
        if self.op == 'jmp':
            self.op = 'nop'
        else:
            self.op = 'jmp'

class Program:
    def __init__(self, commands):
        self.ptr = 0
        self.accumulator = 0
        self.commands = [Command(op, arg) for op, arg in commands]
        self.halted = False
        self.completed = False

    def run(self):
        if self.ptr >= len(self.commands):
            self.halted = True
            self.completed = True
            return
        command = self.commands[self.ptr]
        if command.is_executed():
            self.halted = True
            return
        command.set_executed(True)
        if command.op == 'nop':
            self.ptr += 1
        elif command.op == 'jmp':
            self.ptr += command.arg
        elif command.op == 'acc':
            self.ptr += 1
            self.accumulator += command.arg

    def is_running(self):
        return not self.halted

    def get_accumulator(self):
        return self.accumulator

    def fix_command(self, x):
        self.commands[x].toggle_jmp_nop()

    def is_completed(self):
        return self.completed

def get_data(file_name):
    def parse_line(string):
        op, arg = string.split(' ')
        if arg[0] == '+':
            arg = int(arg[1:])
        else:
            arg = -int(arg[1:])
        return (op, arg)

    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(parse_line(line.strip()))
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def part1(program):
    while program.is_running():
        program.run()
    return program.get_accumulator()

def part2(data):
    prev_jmp_nop = -1
    while True:
        program = Program(data)
        for ndx in range(0, len(data)):
            op, arg = data[ndx]
            if op in ['jmp', 'nop'] and prev_jmp_nop < ndx:
                prev_jmp_nop = ndx
                program.fix_command(ndx)
                break
        while program.is_running():
            program.run()
        if program.is_completed():
            break    
    return program.get_accumulator()

def main():
    data = get_data('aoc08.txt')
    program = Program(data)

    # Part 1
    print(f'PART 1--Answer: {part1(program)}')

    # Part 2
    print(f'PART 2--Answer: {part2(data)}')

if __name__ == '__main__':
    main()
