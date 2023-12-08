import math

from src.common.iterators import cycle


def haunted_wasteland(documents):
    instructions, nodes = documents

    return part1(instructions=instructions, nodes=nodes), part2(
        instructions=instructions, nodes=nodes
    )


def part1(instructions: str, nodes: dict[str, dict]):
    step = 0
    current_node = "AAA"
    iter_instructions = cycle(instructions)
    while current_node != "ZZZ":
        instruction = next(iter_instructions)
        current_node = nodes[current_node]["left" if instruction == "L" else "right"]
        step += 1
    return step


def part2(instructions: str, nodes: dict[str, dict]):
    """Veeeery-long to bruteforce.
    Each starting node A reach its ending Z in a cycle, so if you count the number of steps for each cycle and compute
    their LCM, that should result in the number of total steps.
    """
    current_nodes = [node for node in nodes if node[-1] == "A"]
    all_steps = []

    step = 0
    iter_instructions = cycle(instructions)
    while len(current_nodes) != 0:
        instruction = next(iter_instructions)
        step += 1

        new_nodes = []
        for current_node in current_nodes:
            if instruction == "L":
                new_node = nodes[current_node]["left"]
            else:
                new_node = nodes[current_node]["right"]

            if new_node.endswith("Z"):
                all_steps.append(step)
                continue
            else:
                new_nodes.append(new_node)
        current_nodes = new_nodes

    return math.lcm(*all_steps)
