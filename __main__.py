import time

from src.parse_input import parse_input
from src.problems.day1_trebuchet import trebuchet
from src.problems.day2_cube_conundrum import cube_conundrum
from src.problems.day3_gear_ratios import gear_ratios


def main():
    problems = {1: trebuchet, 2: cube_conundrum, 3: gear_ratios}

    for problem_number in range(1, len(problems) + 1):
        t1 = time.time()
        input_data = parse_input(
            path_dir_input="inputs",
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


def format_problem_results(
    problem_number: int,
    problem_function: callable,
    results: tuple[int, int],
    time_to_completion: float,
) -> str:
    return f"{problem_number}. {problem_function.__name__} : {', '.join(str(result) for result in results)} ({round(time_to_completion, 4)}s)"


if __name__ == "__main__":
    main()
