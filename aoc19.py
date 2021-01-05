'''
Advent of Code 2020 Day 19
Jana Goodman

Part 1: the patterns in the rules are 'almost' re expressions

Part 2: recursion in rules

In the test rules and challenge rules rule 000 points 
directly to 8 and 11 in this order.

So every valid rule follows one of these patterns:

Rule 8 returns pattern like this: (42), (42, 42), (42, 42, 42), ...
Rule 11: (42, 31), (42, 42, 31, 31), (42, 42, 42, 31, 31, 31), ...

There is issue of how many repeats?
   However, the size of the messages is relatively small.
   So, using 9 repeats

'''
import re


def get_data(file_name):
    rules, messages = [], []
    try:
        collecting_rules = True
        for line in open(file_name, 'r').readlines():
            line = line.strip()
            if len(line) == 0:
                collecting_rules = False
                continue
            if collecting_rules:
                rules.append(line.strip())
            else:
                messages.append(line.strip())
        return rules, messages
    except FileNotFoundError:
        print(f'File {file_name} not found.')


def process_rules(rules):
    # take these patterns in the rule string
    #      and make 'almost' good for re.match
    # NOTE: treating rules as strings,
    #       so string.replace can be used
    #       to be sure rule numbers are unique: 000,001,002,...
    def parse_rule(s):
        if s in ['"a"', '"b"']:
            return s[1]
        nums = re.findall('\d+', s)
        nums = [n.rjust(3, '0') for n in nums]
        if '|' in s:
            if len(nums) == 2:
                return f'({nums[0]}|{nums[1]})'
            elif len(nums) == 4:
                return f'({nums[0]} {nums[1]}|{nums[2]} {nums[3]})'
        if len(nums) == 1:
            return f'{nums[0]}'
        elif len(nums) == 2:
            return f'{nums[0]} {nums[1]}'

    result = dict()
    for s in rules:
        id, rule = s.split(': ')
        result[id.rjust(3, '0')] = parse_rule(rule)
    return result


def get_re(rules, main='000', ignores=set()):
    # boil rules down to just one rule 000 by
    #  repeatedly replacing rule numbers with definitions
    #  until rule 000 has no numbers in it
    # ultimately rule 000 becomes a re.match expression
    rule_main = rules[main]
    rules.pop(main)
    while True:
        numbers = re.findall('\d+', rule_main)
        numbers = [n for n in numbers if n not in ignores]
        if len(numbers) == 0:
            break
        for rule1 in numbers:
            if rule1 not in rules.keys():
                break
            r = rules.pop(rule1)
            rule_main = rule_main.replace(rule1, r)
            for rule2 in rules:
                if rule1 in rules[rule2]:
                    rules[rule2] = rules[rule2].replace(rule1, r)
    result = rule_main.replace(' ', '')
    return '^' + result + '$'


def part1(rules, messages):
    rule0 = get_re(rules)
    return sum(1 for s in messages if re.match(rule0, s))


def copy_dict(d):
    result = dict()
    for id in d:
        result[id] = d[id]
    return result


def get_matches(pattern, messages):
    return set([s for s in messages if re.match(pattern, s)])


def part2(rules, messages):
    save = copy_dict(rules)
    rule000 = get_re(rules)

    # same as part 1
    matches = get_matches(rule000, messages)

    # expand 042 and 031
    rules = copy_dict(save)
    rules.pop('000')
    rule031 = get_re(rules, '031')[1:-1]

    rules = copy_dict(save)
    rules.pop('000')
    rule042 = get_re(rules, '042')[1:-1]

    # finally a big long re expression to check the messages
    rule2 = '(42)+'
    rule8 = '(' \
            '((42){1}(31){1})|' \
            '((42){2}(31){2})|' \
            '((42){3}(31){3})|' \
            '((42){4}(31){4})|' \
            '((42){5}(31){5})|' \
            '((42){6}(31){6})|' \
            '((42){7}(31){7})|' \
            '((42){8}(31){8})|' \
            '((42){9}(31){9}))'

    final_rule = '^(42)+('.replace('42', rule042)
    repeat_string = '((42){x}(31){x})|'.replace('42', rule042)
    repeat_string = repeat_string.replace('31', rule031)
    for x in range(1, 10):
        final_rule += repeat_string.replace('x', str(x))
    final_rule = final_rule[0:-1] + ')$'

    for message in messages:
        if re.match(final_rule, message):
            matches.add(message)
    return len(matches)


def main():
    rules, messages = get_data('aoc19.txt')
    rules = process_rules(rules)
    save = copy_dict(rules)

    # Part 1
    print(f'PART 1--Number of good messages: {part1(rules, messages)}')

    # Part 2
    print(f'PART 2--Number of good messages: {part2(copy_dict(save), messages)}')


if __name__ == '__main__':
    main()
