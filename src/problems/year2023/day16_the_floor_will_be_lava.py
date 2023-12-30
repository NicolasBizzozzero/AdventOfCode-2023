CONTRAPTION: list[str] | None = None


def the_floor_will_be_lava(contraption: tuple[str]):
    global CONTRAPTION
    CONTRAPTION = contraption

    all_energized_possibilites = []
    for idx_row in range(len(contraption)):
        for idx_column in range(len(contraption[0])):
            if idx_row == 0:
                all_energized_possibilites.append(
                    propagate_beam(idx_start=(idx_row, idx_column), direction_from="v")
                )
            if idx_row == len(contraption) - 1:
                all_energized_possibilites.append(
                    propagate_beam(idx_start=(idx_row, idx_column), direction_from="^")
                )
            if idx_column == 0:
                all_energized_possibilites.append(
                    propagate_beam(idx_start=(idx_row, idx_column), direction_from=">")
                )
            if idx_column == len(contraption[0]) - 1:
                all_energized_possibilites.append(
                    propagate_beam(idx_start=(idx_row, idx_column), direction_from="<")
                )

    energized_part1 = propagate_beam(idx_start=(0, 0), direction_from=">")
    all_energized_possibilites = map(compute_energy, all_energized_possibilites)

    return compute_energy(energized_part1), max(all_energized_possibilites)


def compute_energy(energized: list[tuple[int, int]]) -> int:
    return len(set(energized))


def propagate_beam(
    idx_start: tuple[int, int], direction_from: str, cache: list = None
) -> list[tuple[int, int]]:
    global CONTRAPTION

    if cache is None:
        cache = []
    call = (idx_start[0], idx_start[1], direction_from)
    if call in cache:
        return []
    cache.append(call)

    if (not 0 <= idx_start[0] < len(CONTRAPTION)) or (
        not 0 <= idx_start[1] < len(CONTRAPTION[0])
    ):
        return []  # OOB

    symbol = CONTRAPTION[idx_start[0]][idx_start[1]]
    if direction_from == ">":
        match symbol:
            case "." | "-":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0], idx_start[1] + 1),
                    direction_from=">",
                    cache=cache,
                )
            case "|":
                return (
                    [idx_start]
                    + propagate_beam(
                        idx_start=(idx_start[0] - 1, idx_start[1]),
                        direction_from="^",
                        cache=cache,
                    )
                    + propagate_beam(
                        idx_start=(idx_start[0] + 1, idx_start[1]),
                        direction_from="v",
                        cache=cache,
                    )
                )
            case "/":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0] - 1, idx_start[1]),
                    direction_from="^",
                    cache=cache,
                )
            case "\\":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0] + 1, idx_start[1]),
                    direction_from="v",
                    cache=cache,
                )
    elif direction_from == "^":
        match symbol:
            case "." | "|":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0] - 1, idx_start[1]),
                    direction_from="^",
                    cache=cache,
                )
            case "-":
                return (
                    [idx_start]
                    + propagate_beam(
                        idx_start=(idx_start[0], idx_start[1] - 1),
                        direction_from="<",
                        cache=cache,
                    )
                    + propagate_beam(
                        idx_start=(idx_start[0], idx_start[1] + 1),
                        direction_from=">",
                        cache=cache,
                    )
                )
            case "/":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0], idx_start[1] + 1),
                    direction_from=">",
                    cache=cache,
                )
            case "\\":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0], idx_start[1] - 1),
                    direction_from="<",
                    cache=cache,
                )
    elif direction_from == "v":
        match symbol:
            case "." | "|":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0] + 1, idx_start[1]),
                    direction_from="v",
                    cache=cache,
                )
            case "-":
                return (
                    [idx_start]
                    + propagate_beam(
                        idx_start=(idx_start[0], idx_start[1] - 1),
                        direction_from="<",
                        cache=cache,
                    )
                    + propagate_beam(
                        idx_start=(idx_start[0], idx_start[1] + 1),
                        direction_from=">",
                        cache=cache,
                    )
                )
            case "/":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0], idx_start[1] - 1),
                    direction_from="<",
                    cache=cache,
                )
            case "\\":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0], idx_start[1] + 1),
                    direction_from=">",
                    cache=cache,
                )
    elif direction_from == "<":
        match symbol:
            case "." | "-":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0], idx_start[1] - 1),
                    direction_from="<",
                    cache=cache,
                )
            case "|":
                return (
                    [idx_start]
                    + propagate_beam(
                        idx_start=(idx_start[0] - 1, idx_start[1]),
                        direction_from="^",
                        cache=cache,
                    )
                    + propagate_beam(
                        idx_start=(idx_start[0] + 1, idx_start[1]),
                        direction_from="v",
                        cache=cache,
                    )
                )
            case "/":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0] + 1, idx_start[1]),
                    direction_from="v",
                    cache=cache,
                )
            case "\\":
                return [idx_start] + propagate_beam(
                    idx_start=(idx_start[0] - 1, idx_start[1]),
                    direction_from="^",
                    cache=cache,
                )
    return []


def print_energized(contraption: list[str], energized: list[tuple[int, int]]) -> None:
    result = ""
    for idx_row in range(len(contraption)):
        for idx_column in range(len(contraption[0])):
            result += "#" if (idx_row, idx_column) in energized else "."
        result += "\n"
    print(result)
