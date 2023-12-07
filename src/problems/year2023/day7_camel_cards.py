import copy
import operator
from collections import Counter


def camel_cards(hands: dict):
    return get_total_winnings(
        copy.deepcopy(hands), with_jokers=False
    ), get_total_winnings(copy.deepcopy(hands), with_jokers=True)


def get_total_winnings(hands: dict, with_jokers: bool) -> int:
    for hand in hands:
        score = get_hand_score(hand["hand"], with_jokers=with_jokers)
        hand["score"] = score

    total_winnings = 0
    for ranking, hand in enumerate(sorted(hands, key=operator.itemgetter("score"))):
        total_winnings += (ranking + 1) * hand["bid"]

    return total_winnings


def get_hand_score(hand: str, with_jokers: bool) -> int:
    score = get_hand_type(hand, with_jokers=with_jokers) * 10_000_000_000
    for idx_card, card in enumerate(reversed(hand)):
        score += get_card_strength(card, with_jokers=with_jokers) * (100**idx_card)
    return score


def get_hand_type(hand: str, with_jokers: bool) -> int:
    counter = Counter(hand)
    most_common = counter.most_common(5)

    if with_jokers and "J" in hand:
        if hand == "JJJJJ":  # f. this edge case
            return 6
        most_common_value = (
            most_common[0][0] if most_common[0][0] != "J" else most_common[1][0]
        )
        return get_hand_type(
            hand.replace("J", most_common_value), with_jokers=with_jokers
        )

    if most_common[0][1] == 5:
        return 6  # Five of a kind
    if most_common[0][1] == 4:
        return 5  # Four of a kind
    if most_common[0][1] == 3:
        if most_common[1][1] == 2:
            return 4  # Full house
        return 3  # Three of a kind
    if most_common[0][1] == 2:
        if most_common[1][1] == 2:
            return 2  # Two pairs
        return 1  # One pair
    return 0  # High card


def get_card_strength(card: str, with_jokers: bool) -> int:
    return "J23456789TQKA".index(card) if with_jokers else "23456789TJQKA".index(card)
