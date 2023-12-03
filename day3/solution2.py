"""Solution to day 3, part 2 puzzle on adventofcode.com"""

import numpy as np

digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
symbol = "*"


def get_input(filepath: str) -> str:
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.read()


def make_array(input_data: str) -> np.array:
    """Make an array from the input data."""
    init_list = input_data.strip().split("\n")
    two_d_array = [list(line) for line in init_list]
    return np.array(two_d_array)


def find_connected_vals(array: np.array, coord: tuple, width: int) -> str:
    """Find all connected numerical values."""
    connected_vals = []

    # Find all connected values to the left
    if coord[1] > 0:
        offset = 1
        while coord[1] - offset >= 0:
            possible_val = array[coord[0], coord[1] - offset]
            if possible_val in digits:
                connected_vals.append(possible_val)
                offset += 1
            else:
                break
        connected_vals = connected_vals[::-1]
    connected_vals.append(array[coord[0], coord[1]])

    # Find all connected values to the right
    if coord[1] < (width - 1):
        offset = 1
        while coord[1] + offset <= (width - 1):
            possible_val = array[coord[0], coord[1] + offset]
            if possible_val in digits:
                connected_vals.append(possible_val)
                offset += 1
            else:
                break

    return connected_vals


def main_logic(input_data: str) -> int:  # noqa: C901
    """Main logic for the puzzle. We need to find if the amount of cubes does not exceed the limit."""
    text_as_array = make_array(input_data)

    height = text_as_array.shape[0]
    width = text_as_array.shape[1]

    answer = 0
    used_numbers = {}
    for i, line in enumerate(text_as_array):
        for j, char in enumerate(line):
            if char == symbol:
                neighbour_coords = [
                    (y, x)
                    for x in range(j - 1, j + 2)
                    for y in range(i - 1, i + 2)
                    if ((y, x) != (i, j)) & (x >= 0) & (y >= 0) & (x <= (width - 1)) & (y <= (height - 1))
                ]
                for neighbour_coord in neighbour_coords:
                    val = text_as_array[neighbour_coord[0], neighbour_coord[1]]
                    if val in digits:
                        connected_vals = find_connected_vals(array=text_as_array, coord=neighbour_coord, width=width)
                        connected_val = "".join(connected_vals)
                        try:
                            used_list = used_numbers[f"{j}+{i}"]
                        except KeyError:
                            used_list = []
                        if connected_val not in used_list:
                            used_list.append(connected_val)
                            used_numbers[f"{j}+{i}"] = used_list

    # Find gear ratios
    for _key, value in used_numbers.items():
        if len(value) == 2:
            gear_ratio = int(value[0]) * int(value[1])
            answer = answer + gear_ratio
    return answer


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input("/Users/bryan/aoc/day3/input.txt")

    # Iterate through each line
    answer = main_logic(input_data=input_data)

    # Print the result
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    solve_puzzle()
