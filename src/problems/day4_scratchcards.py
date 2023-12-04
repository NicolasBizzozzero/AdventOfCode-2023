from collections import defaultdict


def scratchcards(cards: list[list[str, str]]):
    number_of_winning_cards = defaultdict(int)
    score = 0
    for idx_card, card in enumerate(cards):
        numbers_winning, numbers_i_have = card
        correct_numbers = set(numbers_winning) & set(numbers_i_have)

        # Part 1. Computing simple score
        if len(correct_numbers) != 0:
            points = 2 ** (len(correct_numbers) - 1)
            score += points

        # Part2. List all number of winning cards
        number_of_winning_cards[idx_card + 1] = len(correct_numbers)

    # Part2. Count all those cards in total
    total_cards = 0
    for idx_card in number_of_winning_cards.keys():
        total_cards += compute_number_of_cards(
            idx_card=idx_card, number_of_winning_cards=number_of_winning_cards
        )

    return score, total_cards


def compute_number_of_cards(
    idx_card: int, number_of_winning_cards: dict[int, int]
) -> int:
    if number_of_winning_cards[idx_card] == 0:
        return 1

    accumulated_number_of_cards = 1
    for idx_other_card in range(
        idx_card + 1, idx_card + number_of_winning_cards[idx_card] + 1
    ):
        accumulated_number_of_cards += compute_number_of_cards(
            idx_card=idx_other_card, number_of_winning_cards=number_of_winning_cards
        )
    return accumulated_number_of_cards
