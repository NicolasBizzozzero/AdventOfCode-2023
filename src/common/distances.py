def manhattan(position1: tuple[int, int], position2: tuple[int, int]) -> int:
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])


def hamming(string1: str, string2: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(string1, string2))
