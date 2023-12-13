from functools import lru_cache


def hot_springs(records):
    # Part 2. Duplicate *5 to produce the same results
    return solve(
        records=records,
        duplicate=1,
    ), solve(records=records, duplicate=5)


def solve(records, duplicate: int) -> int:
    total_arrangements = 0
    for record in records:
        springs, damaged_springs = record

        # Produce copies of springs
        springs = "?".join((springs,) * duplicate)
        damaged_springs = tuple(damaged_springs * duplicate)

        nb_arrangements = compute_arrangements(springs, damaged_springs)
        total_arrangements += nb_arrangements
    return total_arrangements


@lru_cache()
def compute_arrangements(springs: str, damaged_springs: tuple[int]) -> int:
    # extract first group
    damaged_spring, damaged_springs = damaged_springs[0], damaged_springs[1:]

    nb_arrangements = 0
    for idx_start in range(
        # Iterate through
        len(springs)
        - (sum(damaged_springs) + len(damaged_springs))
        - damaged_spring
        + 1
    ):
        if all_damaged_or_unknown(springs[idx_start : idx_start + damaged_spring]):
            if len(damaged_springs) == 0:
                if all_operational_or_unknown(springs[idx_start + damaged_spring :]):
                    nb_arrangements += 1
            elif springs[idx_start + damaged_spring] in ".?":
                nb_arrangements += compute_arrangements(
                    springs[idx_start + damaged_spring + 1 :], damaged_springs
                )

        if springs[idx_start] not in ".?":
            break

    return nb_arrangements


def all_damaged_or_unknown(springs: str) -> bool:
    return all(spring in "#?" for spring in springs)


def all_operational_or_unknown(springs: str) -> bool:
    return all(spring in ".?" for spring in springs)
