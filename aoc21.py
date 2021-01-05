'''
Advent of Code 2020 Day 19
Jana Goodman

NOTE:
    ingredients have none or one allergen
    allergens are in exactly one ingredient
    foods list all the ingredients,
        but not necessarily all the allergens
        in those ingredients
'''


class Ingredient:
    def __init__(self, name):
        self.__name__ = name
        self.__allergen__ = None
        self.__possible_allergens__ = set()
        self.__foods__ = set()

    def add_possible_allergen(self, allergen_id):
        self.__possible_allergens__.add(allergen_id)

    def get_foods(self):
        return self.__foods__

    def add_food(self, food_id):
        self.__foods__.add(food_id)


class Allergen:
    def __init__(self, name):
        self.__name__ = name
        self.__ingredient__ = None
        self.__foods__ = set()

    def add_food(self, food_id):
        self.__foods__.add(food_id)


class Food:
    def __init__(self, name):
        self.__name__ = name
        # name is FOODn w/ n = number of the line in the data
        self.__ingredients__ = set()
        self.__allergens__ = set()

    def get_ingredients(self):
        return self.__ingredients__

    def add_ingredient(self, ingredient):
        self.__ingredients__.add(ingredient)

    def get_allergens(self):
        return self.__allergens__

    def add_allergen(self, allergen):
        self.__allergens__.add(allergen)


def get_data(file_name):
    def parse_line(string, id):
        ingredients, allergens = string.split('(')
        ingredients = ingredients.strip().split(' ')
        allergens = allergens[9:-1].split(', ')
        return f'FOOD{id}', ingredients, allergens

    try:
        foods, ingredients, allergens = dict(), dict(), dict()
        food_id = 0
        for line in open(file_name, 'r').readlines():
            f_name, i_names, a_names = parse_line(line.strip(), food_id)
            foods[f_name] = Food(f_name)
            for i_name in i_names:
                if i_name not in ingredients.keys():
                    ingredients[i_name] = Ingredient(i_name)
                foods[f_name].add_ingredient(i_name)
            for a_name in a_names:
                if a_name not in allergens.keys():
                    allergens[a_name] = Allergen(a_name)
                foods[f_name].add_allergen(a_name)
            food_id += 1
        for f_name in foods.keys():
            for i in foods[f_name].get_ingredients():
                ingredients[i].add_food(f_name)
                for a in foods[f_name].get_allergens():
                    ingredients[i].add_possible_allergen(a)
            for a in foods[f_name].get_allergens():
                allergens[a].add_food(f_name)
        return foods, ingredients, allergens
    except FileNotFoundError:
        print(f'File {file_name} not found.')


def is_possible(foods, a, i):
    for food in foods.values():
        if a in food.get_allergens():
            if i not in food.get_ingredients():
                return False
    return True


def has_no_allergens(i, foods, allergens):
    for allergen in allergens:
        if is_possible(foods, allergen, i):
            return False
    return True


def part1(foods, ingredients, allergens):
    return sum(len(ingredients[i].get_foods()) for i in
               [i for i in ingredients
                if has_no_allergens(i, foods, allergens)])


def get_possibles(foods, allergens):
    allergen_names = [a for a in allergens]
    allergen_names.sort()
    possibles = []
    for allergen_name in allergen_names:
        foods_w_allergen = [f for f in foods
                            if allergen_name in
                            foods[f].get_allergens()]
        ingreds_of_foods_w_allergen = \
            set.union(*[foods[f].get_ingredients()
                        for f in foods_w_allergen])
        possible_allergen_ingreds = []
        for i in ingreds_of_foods_w_allergen:
            bad = False
            for f in foods_w_allergen:
                if i not in foods[f].get_ingredients():
                    bad = True
                    break
            if not bad:
                possible_allergen_ingreds.append(i)
        possibles.append([allergen_name, possible_allergen_ingreds])
    return possibles


def get_unique_ingredient(possibles):
    change = True
    while change:
        change = False
        ndx = 0
        for poss in possibles:
            allergen_name = poss[0]
            if 'DONE-' in allergen_name:
                ndx += 1
                continue
            poss_ingreds = poss[1]
            if len(poss_ingreds) == 1:
                ingred = list(poss_ingreds)[0]
                for ndx2 in range(0, len(possibles)):
                    if possibles[ndx2][0] != allergen_name:
                        if ingred in possibles[ndx2][1]:
                            possibles[ndx2][1].remove(ingred)
                            change = True
                possibles[ndx][0] = 'DONE-' + allergen_name
            ndx += 1
    return possibles


def part2(foods, allergens):
    # possibles:
    #   allergen and
    #   list of ingredient that might contain the allergen
    possibles = get_possibles(foods, allergens)
    # now possibles are 'DONE-allergen' and the unique ingredient
    possibles = get_unique_ingredient(possibles)
    return ''.join([f'{p[1][0]},' for p in possibles])[0:-1]


def main():
    foods, ingredients, allergens = get_data('aoc21.txt')

    # Part 1
    ans = part1(foods, ingredients, allergens)
    print(f'PART 1--Number of ingredients w/ no allergens: {ans}')

    # Part 2
    print(f'PART 2--Dangerous ingredients: {part2(foods, allergens)}')


if __name__ == '__main__':
    main()
