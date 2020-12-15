'''
Advent of Code 2020 Day 4
Jana Goodman

'''
class Passport:

    def __init__(self, string):
        self.MANDATORIES = {'byr': self.get_birth_year,
                            'iyr': self.get_issue_year,
                            'eyr': self.get_expiration_year,
                            'hgt': self.get_height,
                            'hcl': self.get_hair_color,
                            'ecl': self.get_eye_color,
                            'pid': self.get_passport_id}
        self.string = string
        self.data = dict()
        for field in string.split(' '):
            [id, value] = field.split(':')
            if id not in self.MANDATORIES.keys():
                self.data[id] = value
            else:
                self.data[id] = self.MANDATORIES[id](value)

        self.field_missing = not all([id in self.data.keys()
                                    for id in self.MANDATORIES.keys()])

    def is_valid(self, part):
        if self.field_missing:
            return False
        if part == 1:
            return True
        return not any([self.data[id] == None for id in self.data.keys()
                    if id != 'cid'])

    def valid_year(self, string, low, high):
        if len(string) != 4 or not string.isnumeric():
            return None
        year = int(string)
        if low <= year <= high:
            return year
        return None

    def get_birth_year(self, string):
        return self.valid_year(string, 1920, 2002)

    def get_issue_year(self, string):
        return self.valid_year(string, 2010, 2020)

    def get_expiration_year(self, string):
        return self.valid_year(string, 2020, 2030)

    def get_height(self, string):
        if len(string) <= 2:
            return None
        in_or_cm = string[-2:]
        if in_or_cm not in ['cm', 'in']:
            return None
        ht = string[0:-2]
        if not ht.isnumeric():
            return None
        ht = int(ht)
        if in_or_cm == 'cm':
            if 150 <= ht <= 193:
                return ht
            return None
        if 59 <= ht <= 76:
            return ht
        return None

    def get_hair_color(self, string):
        if len(string) != 7:
            return None
        if string[0] != '#':
            return None
        for dig in string[1:]:
            if dig not in 'abcdef0123456789':
                return None
        return string

    def get_eye_color(self, string):
        if string in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return string
        return None

    def get_passport_id(self, string):
        if len(string) != 9:
            return None
        return all([dig in '0123456789' for dig in string[1:]])

def get_data(file_name):
    result = []
    try:
        for line in open(file_name, 'r').readlines():
            result.append(line.strip())
        return result
    except FileNotFoundError:
        print(f'File {file_name} not found.')

def is_blank(string):
    return len(string) == 0

def get_passports(arr):
    passports = []
    passport_string = ''
    for line in arr:
        if is_blank(line):
            passports.append(Passport(passport_string))
            passport_string = ''
        else:
            if passport_string == '':
                passport_string = line
            else:
                passport_string += ' ' + line
    passports.append(Passport(passport_string))
    return passports

def part1(passports):
    return [passport.is_valid(1) for passport in passports].count(True)


def part2(passports):
    return [passport.is_valid(2) for passport in passports].count(True)

def main():
    data = get_data('aoc04.txt')
    passports = get_passports(data)
    # Part 1

    print(f'PART 1--Answer: {part1(passports)}')

    print(f'PART 2--Answer: {part2(passports)}')

if __name__ == '__main__':
    main()
