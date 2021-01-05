'''
Advent of Code 2020 Day 25
Jana Goodman

'''


def get_loop_size(sub, pub, md):
    result = 0
    transform = 1
    while True:
        transform = (transform * sub) % md
        result += 1
        if transform == pub:
            return result


def part1(pub, loop_size, md):
    return pow(pub, loop_size, md)


def main():
    card_public_key, door_public_key = 8184785, 5293040
    subject_number = 7
    md = 20201227

    loop_size1 = get_loop_size(subject_number, card_public_key, md)
    print(f'Loop size for card public key {card_public_key} is {loop_size1}')
    loop_size2 = get_loop_size(subject_number, door_public_key, md)
    print(f'Loop size for door public key {door_public_key} is {loop_size2}')

    # Part 1
    #   also could do card key with door loop size
    print(f'PART 1--Encryption key: {part1(door_public_key, loop_size1, md)}')


# No part 2 -- just need rest of the stars -- looking at you Day 20, 22, 23


if __name__ == '__main__':
    main()
