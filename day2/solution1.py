"""Solution to day 1, part 1 puzzle on adventofcode.com"""

import re

red_limit = 12
green_limit = 13
blue_limit = 14


def get_input(filepath):
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.readlines()


def get_red_cubes(line):
    """Get all red cubes from a string."""
    regex = r"(\d+) red"
    return re.findall(regex, line)


def get_green_cubes(line):
    """Get all red cubes from a string."""
    regex = r"(\d+) green"
    return re.findall(regex, line)


def get_blue_cubes(line):
    """Get all red cubes from a string."""
    regex = r"(\d+) blue"
    return re.findall(regex, line)


def main_logic(game_id, line):
    """Main logic for the puzzle. We need to find if the amount of cubes does not exceed the limit."""
    sets = line.split(":")[1]
    # Get all cubes from the current line
    red_cubes = get_red_cubes(sets)
    green_cubes = get_green_cubes(sets)
    blue_cubes = get_blue_cubes(sets)
    # Check if they do not exceed the limit
    if red_cubes:
        red_possible = [int(num) <= red_limit for num in red_cubes]
        if not all(red_possible):
            return 0
    if green_cubes:
        green_possible = [int(num) <= green_limit for num in green_cubes]
        if not all(green_possible):
            return 0
    if blue_cubes:
        blue_possible = [int(num) <= blue_limit for num in blue_cubes]
        if not all(blue_possible):
            return 0

    return game_id + 1


def solve_puzzle():
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input("/Users/bryan/aoc/day2/input.txt")

    answer = 0
    # Iterate through each line
    for i, line in enumerate(input_data):
        answer = answer + main_logic(game_id=i, line=line)

    # Print the result
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    solve_puzzle()
