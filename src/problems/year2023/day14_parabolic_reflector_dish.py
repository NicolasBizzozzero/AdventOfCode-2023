def parabolic_reflector_dish(platform: list[str]):
    return part1(platform=platform), part2(platform=platform)


def part1(platform: list[str]) -> int:
    platform = move_rocks(platform)
    return count_rocks(platform)


def part2(platform: list[str]) -> int:
    count = {}
    history = {}
    max_cycle = 1_000_000_000
    for idx_cycle in range(1, max_cycle):
        # print(cycle)
        for _ in range(4):
            platform = move_rocks(platform)
            platform = rotate(platform)

        if (representation := "".join(platform)) in history.keys():
            # Cycle detected
            idx_start_cycle = history[representation]
            idx_target = idx_start_cycle + (max_cycle - idx_start_cycle) % (
                idx_cycle - history[representation]
            )

            # Reverse lookup to find the repr matching the target index
            for representation, idx in history.items():
                if idx == idx_target:
                    return count[representation]
        else:
            history[representation] = idx_cycle
            count[representation] = count_rocks(platform)


def move_rocks(platform: list[str]) -> list[str]:
    columns = []
    for idx_col in range(len(platform[0])):
        column = move_rocks_column(platform, idx_col)
        columns.append(column)

    # Reconvert columns to data
    new_data = []
    for i in range(len(columns[0])):
        new_data.append("".join([columns[j][i] for j in range(len(columns))]))
    return new_data


def move_rocks_column(data: list[str], idx_col: int) -> str:
    # Retrieve all column
    column = [data[i][idx_col] for i in range(len(data))]
    for i in range(len(column)):
        if column[i] == "O":
            column = move_rock(column, idx_rock=i)

    return "".join(column)


def move_rock(column: list[str], idx_rock: int) -> list[str]:
    while idx_rock > 0:
        idx_rock -= 1
        if column[idx_rock] == ".":
            column = column[:idx_rock] + ["O", "."] + column[idx_rock + 2 :]
        elif column[idx_rock] in "#O":
            return column
    return column


def count_rocks(platform: list[str]) -> int:
    return sum(
        [
            len(platform) - idx_row
            for idx_row, row in enumerate(platform)
            for elem in row
            if elem == "O"
        ]
    )


def rotate(platform: list[str]) -> list[str]:
    height, width = len(platform), len(platform[0])
    new_grid = [["." for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for j in range(width):
            new_grid[j][height - i - 1] = platform[i][j]
    return ["".join(col) for col in new_grid]
