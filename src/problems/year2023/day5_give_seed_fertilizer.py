import math

import tqdm

from src.common.iterators import batched


def give_seed_fertilizer(almanac: dict):
    return (
        part1(
            seeds=almanac["seeds"],
            almanac=almanac["almanac"],
        ),
        part2(
            seeds=almanac["seeds"],
            almanac=almanac["almanac"],
        ),
    )


def part1(seeds: list[int], almanac: list[list[dict]]) -> int:
    lowest_location = math.inf
    for seed in seeds:
        if (location := seed_to_location(seed=seed, almanac=almanac)) < lowest_location:
            lowest_location = location
    return lowest_location


def part2(seeds: list[int], almanac: list[list[dict]]):
    """Bruteforce a compatible seed by checking every location from 0 to +infinity.
    For each location, retrieve the given seed number (possible because the almanac is a bijection), then check if this
    seed is in the given ranges.
    """
    with tqdm.tqdm() as pbar:
        part2_location = 0
        while not is_compatible_seed(
            seed=location_to_seed(location=part2_location, almanac=almanac),
            seed_ranges=seeds,
        ):
            part2_location += 1
            pbar.update()
    return part2_location


def seed_to_location(seed: int, almanac: list[list[dict]]):
    path = [seed]
    for maps in almanac:
        for correspondance in maps:
            if (
                correspondance["src_range_start"]
                <= path[-1]
                < correspondance["src_range_start"] + correspondance["range_length"]
            ):
                path.append(
                    correspondance["dest_range_start"]
                    + (path[-1] - correspondance["src_range_start"])
                )
                break
        else:
            path.append(path[-1])
    return path[-1]


def location_to_seed(location: int, almanac: list[list[dict]]) -> int:
    path = [location]
    for maps in reversed(almanac):
        for correspondance in maps:
            if (
                correspondance["dest_range_start"]
                <= path[-1]
                < correspondance["dest_range_start"] + correspondance["range_length"]
            ):
                path.append(
                    correspondance["src_range_start"]
                    + (path[-1] - correspondance["dest_range_start"])
                )
                break
        else:
            path.append(path[-1])
    return path[-1]


def is_compatible_seed(seed: int, seed_ranges: list[int]) -> bool:
    for range_start, range_length in batched(seed_ranges, 2):
        if range_start <= seed < range_start + range_length:
            return True
    return False
