'''
Advent of Code 2020 Day 7
Jana Goodman

TODO: make logic clearer -- at least rename variables

'''

import networkx
import bellmanford

def get_data(file_name):
    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(line.strip())
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def shade_color(string):
    if string == 'no other bags.':
        return None
    t = string.split(' ')
    if len(t) == 3:
        return t[0] + ' ' + t[1]
    return t[1] + ' ' + t[2]

def get_digraph(arr):
    rules = [_.split(' contain ') for _ in arr]
    rules = [[_[0], _[1].split(', ')] for _ in rules]
    rules = [[shade_color(r[0]), [shade_color(_) for _ in r[1]]] for r in rules]
    dig = networkx.DiGraph()
    for bag, colors in rules:
        dig.add_node(bag)
        for color in colors:
            dig.add_edge(bag, color)
    return dig

def part1(dig):
    result = 0
    for node in dig.nodes():
        if node != 'shiny gold':
            path_nodes = bellmanford.bellman_ford(dig, node, 'shiny gold')[1]
            if len(path_nodes) > 0:
                result += 1
    return result

def number_shade_color(string):
    if string == 'no other bags.':
        return None
    t = string.split(' ')
    if len(t) == 3:
        return t[0] + ' ' + t[1]
    return (int(t[0]), t[1] + ' ' + t[2])

def get_dictionary(arr):
    rules = [_.split(' contain ') for _ in arr]
    rules = [[_[0], _[1].split(', ')] for _ in rules]
    rules = [[number_shade_color(r[0]), [number_shade_color(_) for _ in r[1]]]
             for r in rules]
    rules = [[color, contain] if contain != [None] else [color, []]
             for color, contain in rules]
    dictionary = dict()
    for color, contain in rules:
        dictionary[color] = contain
    return dictionary

def part2(dictionary):
    # 340 too low
    result = 0
    current_level = [(1, 'shiny gold')]
    next_level = []
    while len(current_level) > 0:
        print(current_level)
        for contain1, color1 in current_level:
            for contain2, color2 in dictionary[color1]:
                result += contain1 * contain2
                next_level.append((contain1 * contain2, color2))
        current_level = [_ for _ in next_level]
        next_level = []
    return result

def main():
    data = get_data('aoc07.txt')
#     data = [
# 'shiny gold bags contain 2 dark red bags.',
# 'dark red bags contain 2 dark orange bags.',
# 'dark orange bags contain 2 dark yellow bags.',
# 'dark yellow bags contain 2 dark green bags.',
# 'dark green bags contain 2 dark blue bags.',
# 'dark blue bags contain 2 dark violet bags.',
# 'dark violet bags contain no other bags.'
#     ]
    print(data)
    digraph = get_digraph(data)

    # Part 1
    print(f'PART 1--Answer: {part1(digraph)}')

    # Part 2
    dictionary = get_dictionary(data)
    print(dictionary)
    print(f'PART 2--Answer: {part2(dictionary)}')

if __name__ == '__main__':
    main()
