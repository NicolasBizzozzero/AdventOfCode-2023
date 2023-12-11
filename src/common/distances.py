def manhattan(position1: tuple[int, int], position2: tuple[int, int]) -> int:
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])
