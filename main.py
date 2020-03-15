def check_combination(cards: list):
    sorted_cards = sorted(cards)
    uni_count = tuple(sorted([sorted_cards.count(x) for x in set(sorted_cards)]))
    straight = list(range(sorted_cards[0], sorted_cards[0] + 5))
    patterns = {
        (1, 1, 1, 1, 1): 'Straight' if sorted_cards == straight else 'Nothing',
        (5,): 'Impossible',
        (1, 1, 1, 2): 'One Pair',
        (1, 4): 'Four of a Kind',
        (2, 3): 'Full House',
        (1, 2, 2): 'Two Pairs',
        (1, 1, 3): 'Three of a Kind'
    }
    return patterns[uni_count]
