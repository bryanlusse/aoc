"""Solution to day 6, part 1 puzzle on adventofcode.com"""

import math
import re

import numpy as np


def get_input(filepath: str) -> list[str]:
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.readlines()


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total number of ways to win and multiply them."""
    win_options = []
    times = re.split(r"\s+", input_data[0].split(":")[1].strip())
    distances = re.split(r"\s+", input_data[1].split(":")[1].strip())
    for time, distance in zip(times, distances):
        options = list(range(0, int(time) + 1))
        result_distance = np.multiply(options, list(map(lambda x: int(time) - x, options)))  # noqa: C417
        wins = sum(1 for element in result_distance if element > int(distance))
        win_options.append(wins)

    return math.prod(win_options)


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day6/input.txt")

    # Iterate through each line
    answer = main_logic(input_data=input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 288


if __name__ == "__main__":
    solve_puzzle()
