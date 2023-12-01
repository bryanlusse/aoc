"""Solution to day 1, part 1 puzzle on adventofcode.com"""

import re


def get_input(filepath):
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.readlines()


def get_numbers(line):
    """Get all numbers from a string."""
    regex = r"(\d)"
    return re.findall(regex, line)


def solve_puzzle():
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input("/Users/bryan/aoc/day1/input.txt")

    answer = 0

    # Iterate through each line
    for line in input_data:
        # Get all numbers from the current line
        numbers = get_numbers(line)

        # Check if there is a match
        if numbers:
            # Extract the first and last standalone single digits
            first_digit = numbers[0]
            last_digit = numbers[-1]
            row_total = int(first_digit + last_digit)
            answer = answer + row_total

    # Print the result
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    solve_puzzle()
