import re
import string
from math import prod
from typing import Union


def gear_ratios(schematic: list[str]):
    # Retrieve symbols position
    positions_symbols = []
    positions_gears = dict()
    for row in range(len(schematic)):
        for column in range(len(schematic[0])):
            if schematic[row][column] not in string.digits + ".":
                positions_symbols.append((row, column))

            # Part 2. Also record gears
            if schematic[row][column] == "*":
                positions_gears[(row, column)] = []

    # Find all numbers in schematic and filter them
    part_numbers = []
    for idx_row, row in enumerate(schematic):
        for match in re.finditer(r"\d+", row):  # Match all numbers + their position
            number = int(match.group())
            positions_number = [
                (idx_row, idx_column)
                for idx_column in range(match.span()[0], match.span()[1])
            ]

            # Part 1. Find if there is a symbol nearby
            if pos_symbol := has_symbol_in_vicinity(
                positions_number=positions_number, positions_symbols=positions_symbols
            ):
                part_numbers.append(number)

                # Part 2. Check if this symbol is a gear
                if pos_symbol in positions_gears.keys():
                    positions_gears[pos_symbol].append(number)

    return (
        sum(part_numbers),
        sum(
            [prod(numbers) for numbers in positions_gears.values() if len(numbers) == 2]
        ),
    )


def has_symbol_in_vicinity(
    positions_number: list[tuple], positions_symbols: list[tuple]
) -> Union[bool, tuple]:
    for pos_number in positions_number:
        for window_row in (-1, 0, 1):
            for window_column in (-1, 0, 1):
                pos = (pos_number[0] + window_row, pos_number[1] + window_column)
                if pos in positions_symbols:
                    return pos
    return False


def print_schematic(schematic: list[str]):
    for line in schematic:
        print(line)
