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
        else:
            return [line.strip() for line in fp.readlines()]
