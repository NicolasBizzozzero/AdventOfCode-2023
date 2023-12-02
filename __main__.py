import copy
import os
import time
import re
from collections import defaultdict

from src.day1_trebuchet import trebuchet
from src.day2_cube_conundrum import cube_conundrum


def main():
    problems = {
        1: trebuchet,
        2: cube_conundrum,
    }

    for problem_number in range(1, len(problems) + 1):
        t1 = time.time()
        input_data = load_input(
            path_input=get_path_input(
                path_dir_input="inputs", problem_number=problem_number
            ),
            problem_number=problem_number,
        )
        problem_function = problems[problem_number]
        results = problem_function(input_data)
        t2 = time.time()
        print(
            format_problem_results(
                problem_number=problem_number,
                problem_function=problem_function,
                results=results,
                time_to_completion=t2 - t1,
            )
        )


def get_path_input(path_dir_input: str, problem_number: int):
    return os.path.join(path_dir_input, f"{problem_number}.txt")


def load_input(path_input: str, problem_number: int):
    with open(path_input) as fp:
        if problem_number in (1,):
            return [word.strip() for word in fp.readlines()]
        elif problem_number in (2,):
            lines = []
            for line in fp.readlines():
                # For both problems, no need to split between each cube draw
                # Furthermore, we can deduce game ID with line index, so we can safely remove it.
                line = re.sub("[;,:]", "", line).split()[2:]
                line = [
                    line[i : i + 2] for i in range(0, len(line), 2)
                ]  # Split in chunks of 2 TODO: chunk func in common
                lines.append(line)
            return lines


def format_problem_results(
    problem_number: int,
    problem_function: callable,
    results: tuple[int, int],
    time_to_completion: float,
) -> str:
    return f"{problem_number}. {problem_function.__name__} : {', '.join(str(result) for result in results)} ({round(time_to_completion, 4)}s)"


if __name__ == "__main__":
    main()
