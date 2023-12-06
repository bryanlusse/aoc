"""Solution to day 6, part 2 puzzle on adventofcode.com"""

import math
import re


def get_input(filepath: str) -> list[str]:
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.readlines()


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total number of ways to win"""
    time = "".join(re.split(r"\s+", input_data[0].split(":")[1].strip()))
    distance = "".join(re.split(r"\s+", input_data[1].split(":")[1].strip()))

    # Solve quadratic equation
    a = 1
    b = -int(time)
    c = int(distance)
    high_x = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    low_x = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    wins = math.floor(high_x - low_x)

    return wins


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day6/input.txt")

    # Iterate through each line
    answer = main_logic(input_data=input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 71503


if __name__ == "__main__":
    solve_puzzle()
