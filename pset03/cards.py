from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]


def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])


def deal(number_of_hands, cards_per_hand):
    if not isinstance(number_of_hands, int) or not isinstance(cards_per_hand, int):
        raise TypeError("number_of_hands and cards_per_hand must be integers")
    if number_of_hands <= 0 or cards_per_hand <= 0:
        raise ValueError("number_of_hands and cards_per_hand must be positive")
    if number_of_hands * cards_per_hand > 52:
        raise ValueError("Not enough cards in the deck to deal the hands")
    deck = shuffled_deck()
    hands = []
    for i in range(number_of_hands):
        hand = deck[i * cards_per_hand:(i + 1) * cards_per_hand]
        hands.append(set(hand))
    return hands


def poker_classification(hand):
    hand = list(hand)
    if len(hand) != 5:
        raise ValueError("hand must contain exactly 5 cards")
    for card in hand:
        if not isinstance(card, Card):
            raise TypeError("hand must only contain Card objects")
    ranks = [14 if card.rank == 1 else card.rank for card in hand]
    ranks.sort()
    suits = [card.suit for card in hand]

    is_flush = len(set(suits)) == 1
    is_straight = len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4
    if set([14 if r == 1 else r for r in [card.rank for card in hand]]) == {14, 2, 3, 4, 5}:
        is_straight = True
    rank_counts = {}
    for r in ranks:
        if r in rank_counts:
            rank_counts[r] += 1
        else:
            rank_counts[r] = 1
    counts = list(rank_counts.values())

    if is_straight and is_flush:
        if min(ranks) == 10:
            return "Royal Flush"
        return "Straight Flush"
    if 4 in counts:
        return "Four of a Kind"
    if 3 in counts and 2 in counts:
        return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if 3 in counts:
        return "Three of a Kind"
    if counts.count(2) == 2:
        return "Two Pair"
    if 2 in counts:
        return "One Pair"
    return "High Card"
