"""Solution to day 1, part 1 puzzle on adventofcode.com"""

import re

import numpy as np


def get_input(filepath):
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.readlines()


def get_red_cubes(line):
    """Get all red cubes from a string."""
    regex = r"(\d+) red"
    return re.findall(regex, line)


def get_green_cubes(line):
    """Get all green cubes from a string."""
    regex = r"(\d+) green"
    return re.findall(regex, line)


def get_blue_cubes(line):
    """Get all blue cubes from a string."""
    regex = r"(\d+) blue"
    return re.findall(regex, line)


def main_logic(line):
    """Main logic for the puzzle. We need to find the max amount of cubes per color and multiply them together."""
    game = line.split(":")
    sets = game[1]

    # Get all cubes from the current line
    red_cubes = get_red_cubes(sets)
    green_cubes = get_green_cubes(sets)
    blue_cubes = get_blue_cubes(sets)

    # Get the max amount per color in the game
    red_max = max(np.array(red_cubes).astype(int))
    green_max = max(np.array(green_cubes).astype(int))
    blue_max = max(np.array(blue_cubes).astype(int))

    # Calculate the power
    power = red_max * green_max * blue_max

    return power


def solve_puzzle():
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input("/Users/bryan/aoc/day2/input.txt")

    answer = 0
    # Iterate through each line
    for line in input_data:
        answer = answer + main_logic(line=line)

    # Print the result
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    solve_puzzle()
