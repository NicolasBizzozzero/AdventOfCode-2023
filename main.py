import os

from src.trebuchet import trebuchet


def main():
    problems = {
        1: trebuchet,
    }

    for problem_number in range(1, len(problems) + 1):
        input_data = load_input(
            path_input=get_path_input(
                path_dir_input="inputs", problem_number=problem_number
            ),
            problem_number=problem_number,
        )
        problem_function = problems[problem_number]
        results = problem_function(input_data)
        print(
            format_problem_results(
                problem_number=problem_number,
                problem_function=problem_function,
                results=results,
            )
        )


def load_input(path_input: str, problem_number: int):
    with open(path_input) as fp:
        return [word.strip() for word in fp.readlines()]


def get_path_input(path_dir_input: str, problem_number: int):
    return os.path.join(path_dir_input, f"{problem_number}.txt")


def format_problem_results(
    problem_number: int, problem_function: callable, results: tuple[int, int]
) -> str:
    return f"{problem_number}. {problem_function.__name__} : {', '.join(str(result) for result in results)}"


if __name__ == "__main__":
    main()
