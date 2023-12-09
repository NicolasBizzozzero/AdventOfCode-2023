import time

from src.parse_input import parse_input
from src.problems.year2023.day1_trebuchet import trebuchet
from src.problems.year2023.day2_cube_conundrum import cube_conundrum
from src.problems.year2023.day3_gear_ratios import gear_ratios
from src.problems.year2023.day4_scratchcards import scratchcards
from src.problems.year2023.day5_give_seed_fertilizer import give_seed_fertilizer
from src.problems.year2023.day6_wait_for_it import day6_wait_for_it
from src.problems.year2023.day7_camel_cards import camel_cards
from src.problems.year2023.day8_haunted_wasteland import haunted_wasteland
from src.problems.year2023.day9_mirage_maintenance import mirage_maintenance


def main():
    problems = {
        1: trebuchet,
        2: cube_conundrum,
        3: gear_ratios,
        # 4: scratchcards,
        # 5: give_seed_fertilizer,
        # 6: day6_wait_for_it,
        7: camel_cards,
        8: haunted_wasteland,
        9: mirage_maintenance,
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
