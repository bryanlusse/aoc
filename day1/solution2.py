"""Solution to day 1, part 2 puzzle on adventofcode.com"""
import re
from contextlib import suppress

digit_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ne": "1",
    "wo": "2",
    "hree": "3",
    "ine": "9",
    "ight": "8",
}


def get_input(filepath):
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.readlines()


def get_numbers(line):
    """Get all numbers from a string."""
    regex = r"(o?ne|t?wo|t?hree|four|five|six|seven|e?ight|n?ine|zero|\d)"
    return re.findall(regex, line)


def map_number(number):
    """Map numbers to their digit equivalent."""
    with suppress(KeyError):
        number = digit_mapping[number]
    return number


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
            first_digit = map_number(numbers[0])
            last_digit = map_number(numbers[-1])
            row_total = int(first_digit + last_digit)
            answer = answer + row_total

    # Print the result
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    solve_puzzle()
