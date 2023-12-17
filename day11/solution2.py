"""Solution to day 11, part 2 puzzle on adventofcode.com"""

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


def calculate_path_length(start, end, row_indices, column_indices):
    """Calculate the path length between two points"""
    x1, y1 = start
    x2, y2 = end
    factor = 1000000 - 1

    path = abs(x2 - x1) + abs(y2 - y1)
    expanded_rows = [row for row in row_indices if (x1 < row < x2) | (x2 < row < x1)]
    expanded_columns = [column for column in column_indices if (y1 < column < y2) | (y2 < column < y1)]
    path += (len(expanded_rows) + len(expanded_columns)) * factor

    return path


def find_shortest_distances(matrix, row_indices, column_indices):
    """Find the shortest distances between all pairs of hashes"""
    indices = np.argwhere(matrix == "#")
    num_hashes = len(indices)

    distances = np.full((num_hashes, num_hashes), fill_value=-1, dtype=int)

    for i in range(num_hashes):
        for j in range(i + 1, num_hashes):
            start = tuple(indices[i])
            end = tuple(indices[j])
            path = calculate_path_length(start, end, row_indices, column_indices)

            distances[i, j] = distances[j, i] = path

    return distances


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total steps."""
    row_indices, columns_indices = find_empty_rows_columns(input_data)
    # expanded_data = double_rows_columns(input_data, row_indices, columns_indices)
    shortest_distances = find_shortest_distances(input_data, row_indices, columns_indices)
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
    # assert answer == 8410


if __name__ == "__main__":
    solve_puzzle()
