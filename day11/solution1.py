"""Solution to day 11, part 1 puzzle on adventofcode.com"""

import numpy as np


def get_input(filepath: str) -> list[str]:
    """Get the input data"""
    with open(filepath) as file:
        data = file.readlines()
        output_data = []
        for line in data:
            output_data.append(list(line.strip()))
        return np.array(output_data)


def find_empty_rows_columns(input_data: list[str]) -> list:
    """Find the empty rows and columns"""
    rows_to_double = np.where((input_data == ".").all(axis=1))[0]
    columns_to_double = np.where((input_data == ".").all(axis=0))[0]
    return [rows_to_double, columns_to_double]


def double_rows_columns(input_data: list[str], row_indices: list, column_indices: list) -> list:
    """Double the rows and columns"""
    expanded_data = input_data.copy()
    row_addition = 0
    for row in sorted(row_indices):
        expanded_data = np.insert(expanded_data, row + row_addition, ".", axis=0)
        row_addition += 1
    column_addition = 0
    for column in sorted(column_indices):
        expanded_data = np.insert(expanded_data, column + column_addition, ".", axis=1)
        column_addition += 1
    return expanded_data


def calculate_path_length(start, end):
    """Calculate the path length between two points"""
    path = []
    x1, y1 = start
    x2, y2 = end

    path = abs(x2 - x1) + abs(y2 - y1)

    return path


def find_shortest_distances(matrix):
    indices = np.argwhere(matrix == "#")
    num_hashes = len(indices)

    distances = np.full((num_hashes, num_hashes), fill_value=-1, dtype=int)

    for i in range(num_hashes):
        for j in range(i + 1, num_hashes):
            start = tuple(indices[i])
            end = tuple(indices[j])
            path = calculate_path_length(start, end)

            distances[i, j] = distances[j, i] = path

    return distances


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total steps."""
    row_indices, columns_indices = find_empty_rows_columns(input_data)
    expanded_data = double_rows_columns(input_data, row_indices, columns_indices)
    shortest_distances = find_shortest_distances(expanded_data)
    answer = 0
    for i in range(shortest_distances.shape[0]):
        answer += sum(shortest_distances[i, :i].tolist())
    return answer


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day11/input.txt")

    # Iterate through each line
    answer = main_logic(input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 374


if __name__ == "__main__":
    solve_puzzle()
