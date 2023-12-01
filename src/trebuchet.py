def trebuchet(words: list[str]) -> tuple[int, int]:
    results1, results2 = [], []
    for word in words:
        results1.append(int(trebuchet_word(word)))
        results2.append(int(trebuchet_word2(word)))
    return sum(results1), sum(results2)


def trebuchet_word(word: str) -> str:
    """Simultaneously traverse the word from right and left until both digits have been found.
    Worst case is when the word contains only one digit, we thus need to traverse the whole word.
    Worst complexity: O(n).
    """
    number_left, number_right = None, None
    for idx_left in range(len(word)):
        idx_right = len(word) - 1 - idx_left

        if not number_left and word[idx_left].isdigit():
            number_left = word[idx_left]

        if not number_right and word[idx_right].isdigit():
            number_right = word[idx_right]

        if number_left and number_right:
            return number_left + number_right


def trebuchet_word2(word: str) -> str:
    """Same as before, but add another operation to check if there is a given prefix at the same index.
    Complexity: O(n)
    """
    number_left, number_right = None, None
    for idx_left in range(len(word)):
        idx_right = len(word) - 1 - idx_left

        if not number_left:
            if word[idx_left].isdigit():
                number_left = word[idx_left]
            elif number := get_digit_written_in_letters(word[idx_left:]):
                number_left = number

        if not number_right:
            if word[idx_right].isdigit():
                number_right = word[idx_right]
            elif number := get_digit_written_in_letters(word[idx_right:]):
                number_right = number

        if number_left and number_right:
            return number_left + number_right


def get_digit_written_in_letters(string: str) -> str:
    """Find if one of the digits is a prefix of `string`.
    At worst, we need to do 9 (number of digits) \times 5 (max length of a digit) opérations.
    Complexity: O(1)
    """
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for digit in digits.keys():
        if string.startswith(digit):
            return digits[digit]
