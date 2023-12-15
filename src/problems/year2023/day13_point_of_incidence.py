from typing import Union

from src.common.distances import hamming


def point_of_incidence(valley: list[list[str]]):
    return find_all_reflections(valley=valley, with_smudge=False), find_all_reflections(
        valley=valley, with_smudge=True
    )


def find_all_reflections(valley: list[list[str]], with_smudge: bool) -> int:
    total = 0
    for pattern in valley:
        # Check horizontal reflection
        if (count := reflect_horizontal(pattern, with_smudge)) is not None:
            total += count * 100
            continue

        # Check vertical reflection
        if (count := reflect_horizontal(rotate_grid(pattern), with_smudge)) is not None:
            total += count
            continue
    return total


def reflect_horizontal(pattern: list[str], with_smudge: bool) -> Union[int, None]:
    for idx_row in range(len(pattern) - 1):
        if is_horizontal_mirror(pattern, idx_row, error_tolerance=int(with_smudge)):
            return idx_row + 1


def is_horizontal_mirror(
    pattern: list[str], idx_row: int, error_tolerance: int
) -> bool:
    for idx_left, idx_right in zip(
        range(idx_row, -1, -1), range(idx_row + 1, len(pattern))
    ):
        row_left = pattern[idx_left]
        row_right = pattern[idx_right]
        if row_left != row_right:
            if hamming(row_left, row_right) == 1:
                error_tolerance -= 1
            else:
                return False
    return error_tolerance == 0


def rotate_grid(grid: list[str]) -> list[str]:
    return ["".join(row) for row in [*zip(*grid)]]


def print_pattern(pattern: list[str]) -> None:
    for line in pattern:
        print(line)
    print()
