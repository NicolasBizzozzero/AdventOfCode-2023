from src.common.distances import manhattan


def cosmic_expansion(universe: list[str]):
    empty_rows, empty_cols = find_empty_spaces(universe)
    galaxies = find_galaxies(universe)

    total_distance = 0
    total_distance_farther = 0
    for galaxy1 in galaxies.values():
        for galaxy2 in galaxies.values():
            total_distance += distance_between_galaxies(
                galaxy1=galaxy1,
                galaxy2=galaxy2,
                empty_rows=empty_rows,
                empty_cols=empty_cols,
                expansion_factor=2,
            )
            total_distance_farther += distance_between_galaxies(
                galaxy1=galaxy1,
                galaxy2=galaxy2,
                empty_rows=empty_rows,
                empty_cols=empty_cols,
                expansion_factor=1_000_000,
            )

    # Divide by two because added all pairwise distances twice
    return total_distance // 2, total_distance_farther // 2


def find_empty_spaces(data: list[str]) -> tuple[list[int], list[int]]:
    empty_rows = []
    empty_cols = []

    for idx_row, row in enumerate(data):
        if "#" not in row:
            empty_rows.append(idx_row)

    for idx_col, col in enumerate(range(len(data[0]))):
        col = ["".join(data[idx_row][idx_col]) for idx_row in range(len(data))]
        if "#" not in col:
            empty_cols.append(idx_col)

    return empty_rows, empty_cols


def find_galaxies(data: list[str]) -> dict[int, tuple[int, int]]:
    galaxies = dict()
    for idx_row, row in enumerate(data):
        for idx_col, col in enumerate(data[idx_row]):
            if col == "#":
                galaxies[len(galaxies) + 1] = (idx_row, idx_col)
    return galaxies


def distance_between_galaxies(
    galaxy1: tuple[int, int],
    galaxy2: tuple[int, int],
    empty_rows: list[int],
    empty_cols: list[int],
    expansion_factor: int,
) -> int:
    # Expand space
    # Just need to count how many rows / columns are between the two galaxies, and multiply this result by the expansion
    # factor.
    expansion = len(
        [
            row
            for row in empty_rows
            if min(galaxy1[0], galaxy2[0]) <= row <= max(galaxy1[0], galaxy2[0])
        ]
    ) * (expansion_factor - 1) + len(
        [
            col
            for col in empty_cols
            if min(galaxy1[1], galaxy2[1]) <= col <= max(galaxy1[1], galaxy2[1])
        ]
    ) * (
        expansion_factor - 1
    )

    return manhattan(galaxy1, galaxy2) + expansion
