import os
import re

from src.common import batched


def get_path_input(path_dir_input: str, problem_number: int):
    return os.path.join(path_dir_input, f"{problem_number}.txt")


def parse_input(path_dir_input: str, problem_number: int):
    path_input = get_path_input(
        path_dir_input=path_dir_input, problem_number=problem_number
    )

    with open(path_input) as fp:
        if problem_number in (2,):
            lines = []
            for line in fp.readlines():
                # For both problems, no need to split between each cube draw
                # Furthermore, we can deduce game ID with line index, so we can safely remove it.
                line = re.sub("[;,:]", "", line).split()[2:]
                line = batched(line, 2)  # Split in chunks of 2
                lines.append(line)
            return lines
        elif problem_number in (4,):
            lines = []
            for line in fp.readlines():
                line = line.split(":")[1]  # Remove card number

                # Parse numbers
                numbers_winning, numbers_i_have = line.split(" | ")
                numbers_winning = numbers_winning.strip().split(" ")
                numbers_i_have = numbers_i_have.strip().split(" ")
                numbers_winning = [
                    int(number) for number in numbers_winning if number != ""
                ]
                numbers_i_have = [
                    int(number) for number in numbers_i_have if number != ""
                ]
                lines.append([numbers_winning, numbers_i_have])
            return lines
        elif problem_number in (5,):
            seeds, *maps = fp.read().split("\n\n")

            seeds = list(map(int, seeds.split(": ")[1].split(" ")))

            maps_cleaned = []
            for m in maps:
                m = m.split("map:")[1]  # Remove useless data
                m = m.strip().split("\n")  # Split each map
                m = [
                    {
                        "dest_range_start": int(line[0]),
                        "src_range_start": int(line[1]),
                        "range_length": int(line[2]),
                    }
                    for line in [data.split() for data in m]
                ]
                maps_cleaned.append(m)
            return {"seeds": seeds, "almanac": maps_cleaned}

        else:
            return [line.strip() for line in fp.readlines()]
