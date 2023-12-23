"""Solution to day 14, part 1 puzzle on adventofcode.com"""

import numpy as np


def get_input(filepath: str) -> np.ndarray:
    """Get the input data as NumPy arrays"""
    with open(filepath) as file:
        data = file.readlines()
        array = np.array([list(row.strip()) for row in data])
        return array


def move_north(matrix: np.ndarray) -> np.ndarray:
    """Moves all the rocks north"""
    moved_array = matrix.copy()
    round_rocks = np.where(matrix == "O")
    for rock in zip(*round_rocks):
        # find closest not moving rock north
        i = 1
        found = False
        while not found:
            # if no rock, break
            if rock[0] - i < 0:
                i += 1
                break
            found = matrix[rock[0] - i, rock[1]] == "#"
            i += 1

        moved_array[rock[0], rock[1]] = "."
        # Extra logic to deal with the case where the most northern position is already taken
        offset = 1
        occupied_space = True
        while occupied_space:
            offset += 1
            occupied_space = moved_array[rock[0] - i + offset, rock[1]] == "O"
        moved_array[rock[0] - i + offset, rock[1]] = "O"
    return moved_array


def calculate_load(matrix: np.ndarray) -> int:
    """Calculates the load of the matrix"""
    load = 0
    for i, row in enumerate(matrix):
        load += np.count_nonzero(row == "O") * (matrix.shape[0] - i)
    return load


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total amount of configurations."""
    answer = 0
    moved_data = move_north(input_data)
    answer = calculate_load(moved_data)
    return answer


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day14/input.txt")
    # print(input_data)

    # Iterate through each line
    answer = main_logic(input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 136


if __name__ == "__main__":
    solve_puzzle()
