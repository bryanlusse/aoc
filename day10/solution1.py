"""Solution to day 10, part 1 puzzle on adventofcode.com"""

import sys

import numpy as np

sys.setrecursionlimit(100000)  # Set the recursion limit to a higher value


def get_input(filepath: str) -> list[str]:
    """Get the input data"""
    with open(filepath) as file:
        data = file.readlines()
        output_data = []
        for line in data:
            output_data.append(list(line.strip()))
        return np.array(output_data)


def walk_pipes(input_data: np.array, y: int, x: int, direction: str, steps: int = 0) -> int:  # noqa: C901
    """Walk the pipes and return the number of steps."""

    steps += 1

    if input_data[y, x] == "S":
        return steps

    if direction == "up":
        if input_data[y, x] == "|":
            return walk_pipes(input_data, y - 1, x, "up", steps)
        elif input_data[y, x] == "F":
            return walk_pipes(input_data, y, x + 1, "right", steps)
        elif input_data[y, x] == "7":
            return walk_pipes(input_data, y, x - 1, "left", steps)
        else:
            return 0
    elif direction == "down":
        if input_data[y, x] == "|":
            return walk_pipes(input_data, y + 1, x, "down", steps)
        elif input_data[y, x] == "L":
            return walk_pipes(input_data, y, x + 1, "right", steps)
        elif input_data[y, x] == "J":
            return walk_pipes(input_data, y, x - 1, "left", steps)
        else:
            return 0
    elif direction == "left":
        if input_data[y, x] == "-":
            return walk_pipes(input_data, y, x - 1, "left", steps)
        elif input_data[y, x] == "L":
            return walk_pipes(input_data, y - 1, x, "up", steps)
        elif input_data[y, x] == "F":
            return walk_pipes(input_data, y + 1, x, "down", steps)
        else:
            return 0
    elif direction == "right":
        if input_data[y, x] == "-":
            return walk_pipes(input_data, y, x + 1, "right", steps)
        elif input_data[y, x] == "7":
            return walk_pipes(input_data, y + 1, x, "down", steps)
        elif input_data[y, x] == "J":
            return walk_pipes(input_data, y - 1, x, "up", steps)
        else:
            return 0


def find_longest_distance(input_data: np.array) -> int:
    """Process the line and return an extrapolated value."""
    y, x = np.where(input_data == "S")
    locations = ["up", "down", "left", "right"]
    fin_values = []
    for loc in locations:
        if loc == "up":
            fin_values.append(walk_pipes(input_data, y - 1, x, loc))
        if loc == "down":
            fin_values.append(walk_pipes(input_data, y + 1, x, loc))
        if loc == "left":
            fin_values.append(walk_pipes(input_data, y, x - 1, loc))
        if loc == "right":
            fin_values.append(walk_pipes(input_data, y, x + 1, loc))
    return max(fin_values)


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total steps."""
    answer = round(find_longest_distance(input_data) / 2)
    return answer


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day10/input.txt")

    # Iterate through each line
    answer = main_logic(input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 8


if __name__ == "__main__":
    solve_puzzle()
