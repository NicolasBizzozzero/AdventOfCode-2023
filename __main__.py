import time

from src.parse_input import parse_input
from src.problems.year2023.day10_pipe_maze import pipe_maze
from src.problems.year2023.day01_trebuchet import trebuchet
from src.problems.year2023.day02_cube_conundrum import cube_conundrum
from src.problems.year2023.day03_gear_ratios import gear_ratios
from src.problems.year2023.day04_scratchcards import scratchcards
from src.problems.year2023.day05_give_seed_fertilizer import give_seed_fertilizer
from src.problems.year2023.day06_wait_for_it import day6_wait_for_it
from src.problems.year2023.day07_camel_cards import camel_cards
from src.problems.year2023.day08_haunted_wasteland import haunted_wasteland
from src.problems.year2023.day09_mirage_maintenance import mirage_maintenance
from src.problems.year2023.day11_cosmic_expansion import cosmic_expansion
from src.problems.year2023.day12_hot_springs import hot_springs
from src.problems.year2023.day13_point_of_incidence import point_of_incidence


def main():
    problems = {
        # 1: trebuchet,
        # 2: cube_conundrum,
        # 3: gear_ratios,
        # 4: scratchcards,
        # 5: give_seed_fertilizer,
        # 6: day6_wait_for_it,
        # 7: camel_cards,
        # 8: haunted_wasteland,
        # 9: mirage_maintenance,
        # 10: pipe_maze,
        # 11: cosmic_expansion,
        # 12: hot_springs,
        13: point_of_incidence
    }

    for problem_number, problem_function in problems.items():
        t1 = time.time()
        input_data = parse_input(
            path_dir_input="inputs",
            problem_number=problem_number,
        )
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
