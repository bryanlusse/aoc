"""Solution to day 15, part 1 puzzle on adventofcode.com"""


def get_input(filepath: str) -> str:
    """Get the input data"""
    with open(filepath) as file:
        data = file.read().split(",")
        return data


def calculate_hash(string: str) -> int:
    """Calculates the hash value of a string"""
    value = 0
    for char in string:
        ascii_repr = ord(char)
        value += ascii_repr
        value *= 17
        value = value % 256
    return value


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total value of the hashes."""
    answer = 0
    for string in input_data:
        answer += calculate_hash(string)
    return answer


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day15/input.txt")
    # print(input_data)

    # Iterate through each line
    answer = main_logic(input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 1320


if __name__ == "__main__":
    solve_puzzle()
