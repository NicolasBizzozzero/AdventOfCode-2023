from collections import defaultdict


def lens_library(initialization_sequence: list[str]):
    results_HASH = []
    boxes = defaultdict(list)
    for label in initialization_sequence:
        print(label)
        # Part 1. Apply HASH over the whole label
        results_HASH.append(HASH_algorithm(string=label))

        # Part 2. Parse label then act accordingly
        if "=" in label:
            label, _, number = parse_label(label)
            box_number = HASH_algorithm(string=label)
            if label_in_box(label=label, box=boxes[box_number]):
                idx_label = remove_label(label=label, box=boxes[box_number])
                insert_label(
                    label=f"{label} {number}",
                    idx_label=idx_label,
                    box=boxes[box_number],
                )
            else:
                boxes[box_number].append(f"{label} {number}")
        else:
            label, _ = parse_label(label)
            box_number = HASH_algorithm(string=label)
            remove_label(label=label, box=boxes[box_number])

    return sum(results_HASH), focusing_power(boxes=boxes)


def label_in_box(label: str, box: list[str]) -> bool:
    return any(l.startswith(label) for l in box)


def remove_label(label: str, box: list[str]) -> int:
    for idx_l, l in enumerate(box):
        if l.startswith(label):
            box.pop(idx_l)
            return idx_l


def insert_label(label: str, idx_label: int, box: list[str]) -> None:
    box.insert(idx_label, label)


def focusing_power(boxes: dict[int, list[str]]) -> int:
    power = 0
    for box_number, box in boxes.items():
        for slot_number, label in enumerate(box):
            label, focal_length = label.split(" ")
            power += (1 + box_number) * (slot_number + 1) * int(focal_length)
            print(power)
    return power


def parse_label(label: str) -> tuple:
    if label.endswith("-"):
        return label[:-1], "-"
    parts, number = label.split("=")
    return parts, "=", int(number)


def HASH_algorithm(string: str) -> int:
    current_value = 0
    for element in string:
        ascii_code = ascii_to_int(element[0])
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value


def ascii_to_int(character: str) -> int:
    return ord(character)
