import copy
from typing import Iterable

from tqdm import tqdm

from src.common.strings import replace_at_index


def pipe_maze(sketch: list[str]):
    # Part 1
    previous_position = find_starting_position(sketch=sketch)
    current_position, position_ending = get_possible_positions(
        sketch=sketch, current_position=previous_position
    )
    path_loop = {0: previous_position, 1: current_position}  # Part 2. Keeping loop path
    step = 2  # +1 starting position, and +1 for reaching end
    while current_position != position_ending:
        current_position, previous_position = (
            get_next_position(
                sketch=sketch,
                current_position=current_position,
                previous_position=previous_position,
            ),
            current_position,
        )
        path_loop[step] = current_position
        step += 1

    # Part 2
    # There is no other loop, thus replace every unvisited tile by empty to clear things up
    for x in range(len(sketch)):
        new_line = []
        for y in range(len(sketch[0])):
            if (x, y) in path_loop.values():
                new_line.append(get_symbol(sketch=sketch, position=(x, y)))
            else:
                new_line.append(".")
        sketch[x] = "".join(new_line)

    # Don't forget the S !
    starting_position = find_starting_position(sketch=sketch)
    sketch[starting_position[0]] = replace_at_index(
        old_string=sketch[starting_position[0]],
        substring="|",
        index=starting_position[1],
    )

    enclosed_tiles = []
    for x in range(1, len(sketch) - 1):
        for y in range(1, len(sketch[0]) - 1):
            if (x, y) in path_loop.values():
                continue

            if is_enclosed(tile=(x, y), path_loop=path_loop, sketch=sketch):
                enclosed_tiles.append((x, y))

    return step // 2, len(enclosed_tiles)


def is_enclosed(tile: tuple[int, int], path_loop: dict, sketch: list[str]):
    """Follows the Even-Odd rule. Draw any line starting from the tile and going outside the loop and count the number
    of walls it crosses. If it crosses an odd number of walls, then the tile is enclosed inside the loop.
    """
    winding_number = 0

    for y in range(tile[1] - 1, -1, -1):
        position = (tile[0], y)
        if position in path_loop.values():
            pipe = get_symbol(sketch=sketch, position=position)
            if pipe in "|JL":
                winding_number += 1

    return winding_number % 2 == 1


def find_starting_position(sketch: list[str]) -> tuple[int, int]:
    for idx_line, line in enumerate(sketch):
        try:
            return idx_line, line.index("S")
        except ValueError:
            pass


def get_next_position(
    sketch: list[str],
    current_position: tuple[int, int],
    previous_position: tuple[int, int],
) -> tuple[int, int]:
    possible_positions = get_possible_positions(
        sketch=sketch, current_position=current_position
    )
    for possible_position in possible_positions:
        if possible_position != previous_position:
            return possible_position


def get_possible_positions(
    sketch: list[str], current_position: tuple[int, int]
) -> list[tuple[int, int]]:
    return [
        position
        for position in iter_around_position(position=current_position)
        if are_connected(sketch=sketch, position1=current_position, position2=position)
    ]


def are_connected(
    sketch: list[str], position1: tuple[int, int], position2: tuple[int, int]
) -> bool:
    if not is_in_bound(sketch=sketch, position=position2):
        return False

    # position2 MUST be in the vicinity of position1
    symbol1 = get_symbol(sketch=sketch, position=position1)
    symbol2 = get_symbol(sketch=sketch, position=position2)

    # Case right
    if position2 == (position1[0], position1[1] + 1):
        return symbol1 in "-LFS" and symbol2 in "-J7S"

    # Case down
    if position2 == (position1[0] + 1, position1[1]):
        return symbol1 in "|7FS" and symbol2 in "|JLS"

    # Case left
    if position2 == (position1[0], position1[1] - 1):
        return symbol1 in "-J7S" and symbol2 in "-LFS"

    # Case up
    if position2 == (position1[0] - 1, position1[1]):
        return symbol1 in "|JLS" and symbol2 in "|7FS"


def iter_around_position(position: tuple[int, int]) -> Iterable[tuple[int, int]]:
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == 0 and y == 0:
                continue
            yield position[0] + x, position[1] + y


def get_symbol(sketch: list[str], position: tuple[int, int]) -> str:
    return sketch[position[0]][position[1]]


def is_in_bound(position: tuple[int, int], sketch: list[str]) -> bool:
    return 0 <= position[0] < len(sketch) and 0 <= position[1] < len(sketch[0])


def print_maze(sketch: list[str], enclosed: list[tuple[int, int]] = None) -> None:
    sketch = copy.deepcopy(sketch)
    if enclosed:
        for position in enclosed:
            sketch[position[0]] = replace_at_index(
                old_string=sketch[position[0]], substring="X", index=position[1]
            )
    for line in sketch:
        line = line.replace("|", "║")
        line = line.replace("-", "═")
        line = line.replace("F", "╔")
        line = line.replace("L", "╚")
        line = line.replace("7", "╗")
        line = line.replace("J", "╝")
        print(line)
