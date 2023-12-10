from math import prod


def day6_wait_for_it(sheet: str):
    races_time = [int(t) for t in sheet[0].split(":")[1].split(" ") if t != ""]
    races_best_distance = [int(t) for t in sheet[1].split(":")[1].split(" ") if t != ""]
    real_big_race_time = int(
        "".join([t for t in sheet[0].split(":")[1].split(" ") if t != ""])
    )
    real_big_race_best_distance = int(
        "".join([t for t in sheet[1].split(":")[1].split(" ") if t != ""])
    )

    total_records_beat = []
    for time, best_distance in zip(races_time, races_best_distance):
        total_records_beat.append(
            get_total_records_beaten(time=time, best_distance=best_distance)
        )

    return prod(total_records_beat), get_total_records_beaten(
        time=real_big_race_time, best_distance=real_big_race_best_distance
    )


def get_total_records_beaten(time: int, best_distance: int) -> int:
    records_beat = 0
    for time_pressed in range(1, time):
        time_remaining = time - time_pressed
        speed = time_pressed
        distance_moved = time_remaining * speed
        if distance_moved > best_distance:
            records_beat += 1
    return records_beat
