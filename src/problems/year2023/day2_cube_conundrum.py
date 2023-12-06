def cube_conundrum(games):
    max_values = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    possible_games = []
    powers = []
    for id_game, game in enumerate(games):
        possible = True
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        for record_value, record_color in game:
            record_value = int(record_value)

            # Check if record is possible
            if max_values[record_color] < record_value:
                possible = False

            # Update max cubes for one color
            max_cubes[record_color] = max(max_cubes[record_color], record_value)

        # Part one, game feasibility
        if possible:
            possible_games.append(id_game + 1)  # ID on data starts at one

        # Part two, power of max cubes
        powers.append(max_cubes["red"] * max_cubes["green"] * max_cubes["blue"])

    return sum(possible_games), sum(powers)
