"""Solution to day 13, part 2 puzzle on adventofcode.com"""

import numpy as np


def get_input(filepath: str) -> list[np.ndarray]:
    """Get the input data as NumPy arrays"""
    with open(filepath) as file:
        data = file.read().strip().split("\n\n")
        arrays = [np.array([list(row) for row in array.split("\n")]) for array in data]
        return arrays


def find_symmetry_line(matrix):
    """Finds the symmetry line in a matrix

    Returns the index of the symmetry line if found, otherwise returns False"""
    margin = 1
    i = 1

    while i < matrix.shape[1]:
        left_side = matrix[:, :i]
        right_side = matrix[:, i:]

        if left_side.shape[1] > right_side.shape[1]:
            left_side = left_side[:, left_side.shape[1] - right_side.shape[1] :]
        elif right_side.shape[1] > left_side.shape[1]:
            right_side = right_side[:, : left_side.shape[1]]
        right_side = np.flip(right_side, axis=1)

        if np.count_nonzero(left_side != right_side) == margin:
            return i
        i += 1
    return False


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total amount of configurations."""
    answer = 0
    for array in input_data:
        symmetry_line = find_symmetry_line(array)
        if not symmetry_line:
            symmetry_line = find_symmetry_line(array.T) * 100

        answer += symmetry_line
    return answer


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day13/input.txt")

    # Iterate through each line
    answer = main_logic(input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 400


if __name__ == "__main__":
    solve_puzzle()
