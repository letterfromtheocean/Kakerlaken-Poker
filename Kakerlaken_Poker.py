import random
from collections import Counter

ANIMALS = ['Cockroach', 'Bat', 'Fly', 'Toad', 'Rat', 'Scorpion', 'Spider', 'Stinkbug']
CARDS_PER_ANIMAL = 8

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.table = []

    def has_cards(self):
        return len(self.hand) > 0

    def add_to_table(self, card):
        self.table.append(card)

    def show_table(self):
        count = Counter(self.table)
        result = ''
        for a in ANIMALS:
            if count[a] > 0:
                if result:
                    result += ', '
                result += f'{a}:{count[a]}'
        return result

    def __str__(self):
        return f'{self.name} (Hand: {len(self.hand)} Table: {self.show_table()})'

def create_deck():
    deck = []
    for animal in ANIMALS:
        deck += [animal] * CARDS_PER_ANIMAL
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_players):
    hands = [[] for _ in range(num_players)]
    for i, card in enumerate(deck):
        hands[i % num_players].append(card)
    return hands

def print_players(players):
    for p in players:
        print(p)
    print()

def check_loser(players):
    for p in players:
        count = Counter(p.table)
        for animal in ANIMALS:
            if count[animal] >= 4:
                return p
    return None

def main():
    print('Welcome to Kakerlaken Poker!')
    num_players = 0
    while num_players < 2 or num_players > 6:
        try:
            num_players = int(input('Enter number of players (2-6): '))
        except ValueError:
            continue
    names = [input(f'Enter name for Player {i+1}: ') for i in range(num_players)]
    players = [Player(name) for name in names]
    deck = create_deck()
    hands = deal_cards(deck, num_players)
    for i, p in enumerate(players):
        p.hand = hands[i]

    current = 0
    while True:
        print_players(players)
        # Check if any player is out of cards
        if not players[current].has_cards():
            print(f'{players[current].name} has no cards, skipping.')
            # Check if all players are out of cards using a for loop and flag
            all_no_cards = True
            for p in players:
                if p.has_cards():
                    all_no_cards = False
                    break
            if all_no_cards:
                # Find player with the most of a single animal on table
                max_count = 0
                loser = None
                for p in players:
                    count = Counter(p.table)
                    if count:
                        most = max(count.values())
                        if most > max_count:
                            max_count = most
                            loser = p
                print_players(players)
                print(f'All players are out of cards. {loser.name} has the most of a single animal on the table ({max_count}). {loser.name} loses!')
                break
            current = (current + 1) % num_players
            continue

        print(f"{players[current].name}'s turn.")
        # Choose target
        while True:
            try:
                target = int(input(f'Choose a player to pass a card to (enter player number, your number is {current+1}, others are 1-{num_players}): ')) - 1
                if target == current or target < 0 or target >= num_players:
                    print('Cannot choose yourself or invalid number.')
                    continue
                if not players[target].has_cards():
                    print('Target player has no cards, choose another.')
                    continue
                break
            except ValueError:
                continue
        # Choose card from hand
        print(f'Your hand: {Counter(players[current].hand)}')
        while True:
            card_input = input(f"Choose an animal to play ({', '.join(ANIMALS)}): ")
            card = None
            for animal in ANIMALS:
                if card_input.strip().lower() == animal.lower() and animal in players[current].hand:
                    card = animal
                    break
            if not card:
                print("You don't have this card or invalid animal name.")
                continue
            break
        # Make a claim
        while True:
            claim_input = input(f'What animal do you claim this is? (You may lie): ')
            claim = None
            for animal in ANIMALS:
                if claim_input.strip().lower() == animal.lower():
                    claim = animal
                    break
            if not claim:
                print('Invalid animal name. Please enter a valid animal.')
                continue
            break
        print(f'You pass a card face down to {players[target].name} and say: This is a {claim}.')
        # Target chooses action
        action = ''
        while action not in ['1', '2', '3']:
            action = input(f'{players[target].name}, do you: 1. Believe 2. Doubt 3. Pass (can only pass once): ')
        if action == '3':
            # Pass
            while True:
                try:
                    next_target = int(input(f'Who do you want to pass to? (cannot be {players[current].name} or yourself, enter number): ')) - 1
                    if next_target in [current, target] or next_target < 0 or next_target >= num_players:
                        print('Cannot choose yourself or the previous player.')
                        continue
                    if not players[next_target].has_cards():
                        print('Target player has no cards, choose another.')
                        continue
                    break
                except ValueError:
                    continue
            new_claim = input(f'What animal do you claim this is? (You may lie): ')
            print(f'You pass the card to {players[next_target].name} and say: This is a {new_claim}.')
            final_action = ''
            while final_action not in ['1', '2']:
                final_action = input(f'{players[next_target].name}, do you: 1. Believe 2. Doubt: ')
            if final_action == '1':
                print(f'{players[next_target].name} chooses to believe.')
                real = (new_claim == card)
                if real:
                    print(f"It's true! {players[current].name} puts the {card} card on their table.")
                    players[current].add_to_table(card)
                else:
                    print(f"It's a lie! {players[next_target].name} puts the {card} card on their table.")
                    players[next_target].add_to_table(card)
                players[current].hand.remove(card)
                loser = check_loser(players)
                if loser:
                    print_players(players)
                    print(f'{loser.name} has 4 of the same animal on the table. Game over! {loser.name} loses!')
                    break
                current = next_target
            else:
                print(f'{players[next_target].name} chooses to doubt.')
                real = (new_claim == card)
                if not real:
                    print(f"It's a lie! {players[current].name} puts the {card} card on their table.")
                    players[current].add_to_table(card)
                else:
                    print(f"It's true! {players[next_target].name} puts the {card} card on their table.")
                    players[next_target].add_to_table(card)
                players[current].hand.remove(card)
                loser = check_loser(players)
                if loser:
                    print_players(players)
                    print(f'{loser.name} has 4 of the same animal on the table. Game over! {loser.name} loses!')
                    break
                current = next_target
        else:
            if action == '1':
                print(f'{players[target].name} chooses to believe.')
                real = (claim == card)
                if real:
                    print(f"It's true! {players[current].name} puts the {card} card on their table.")
                    players[current].add_to_table(card)
                else:
                    print(f"It's a lie! {players[target].name} puts the {card} card on their table.")
                    players[target].add_to_table(card)
                players[current].hand.remove(card)
                loser = check_loser(players)
                if loser:
                    print_players(players)
                    print(f'{loser.name} has 4 of the same animal on the table. Game over! {loser.name} loses!')
                    break
                current = target
            else:
                print(f'{players[target].name} chooses to doubt.')
                real = (claim == card)
                if not real:
                    print(f"It's a lie! {players[current].name} puts the {card} card on their table.")
                    players[current].add_to_table(card)
                else:
                    print(f"It's true! {players[target].name} puts the {card} card on their table.")
                    players[target].add_to_table(card)
                players[current].hand.remove(card)
                loser = check_loser(players)
                if loser:
                    print_players(players)
                    print(f'{loser.name} has 4 of the same animal on the table. Game over! {loser.name} loses!')
                    break
                current = target

if __name__ == "__main__":
    main()
