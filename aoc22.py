'''
Advent of Code 2020 Day 22
Jana Goodman

'''


class Game():
    def __init__(self, hand1, hand2):
        self.hand1, self.hand2 = [_ for _ in hand1], [_ for _ in hand2]
        self.winner = 0

    def draw_cards(self):
        return self.hand1.pop(0), self.hand2.pop(0)

    def is_empty(self, arr):
        return len(arr) == 0

    def round_winner(self, c1, c2):
        if c1 < c2:
            return 2
        return 1

    def update_winner(self, w, c1, c2):
        if w == 1:
            self.hand1 += [c1, c2]
        else:
            self.hand2 += [c2, c1]

    def score(self):
        if self.winner == 1:
            hand = self.hand1
        else:
            hand = self.hand2
        return sum([pos * card for pos, card in enumerate(list(reversed(hand)), 1)])

    def play_round(self):
        card1, card2 = self.draw_cards()
        self.update_winner(self.round_winner(card1, card2), card1, card2)
        if self.is_empty(self.hand2):
            self.winner = 1
        elif self.is_empty(self.hand1):
            self.winner = 2

    def play_game(self):
        while self.winner == 0:
            self.play_round()
        return self.score()


class RecurGame(Game):
    def __init__(self, hand1, hand2):
        Game.__init__(self, hand1, hand2)
        self.hand1, self.hand2 = [_ for _ in hand1], [_ for _ in hand2]
        self.prev = set()

    def repeats(self):
        curr = (tuple(self.hand1), tuple(self.hand2))
        if curr in self.prev:
            return True
        self.prev.add(curr)

    def need_subgame(self, c1, c2):
        return c1 <= len(self.hand1) and c2 <= len(self.hand2)

    def play_round(self):
        if self.repeats():
            self.winner = 1
            return
        card1, card2 = self.draw_cards()
        if self.need_subgame(card1, card2):
            self.subgame = RecurGame(list(self.hand1)[:card1], list(self.hand2)[:card2])
            self.subgame.play_game()
            wins_round = self.subgame.winner
        else:
            wins_round = self.round_winner(card1, card2)
        self.update_winner(wins_round, card1, card2)
        if self.is_empty(self.hand1) or self.is_empty(self.hand2):
            self.winner = wins_round

def get_data(file_name):
    hand = 0
    deck = [[], []]
    try:
        for line in open(file_name, 'r').readlines():
            s = line.strip()
            if s == '':
                hand += 1
            else:
                if s.isnumeric():
                    deck[hand].append(int(s))
        return deck[0], deck[1]
    except FileNotFoundError:
        print(f'File {file_name} not found.')


def part1(game):
    game.play_game()
    return game.score()


# no need for part2

def main():
    hand1, hand2 = get_data('aoc22.txt')
    print(f'PART 1--Winning score: {part1(Game(hand1, hand2))}')
    print(f'PART 2--Winning score: {part1(RecurGame(hand1, hand2))}')


if __name__ == '__main__':
    main()
