"""Solution to day 8, part 1 puzzle on adventofcode.com"""


def get_input(filepath: str) -> list[str]:
    """Get the input data"""
    with open(filepath) as file:
        data = file.read()
        steps, coordinates = data.split("\n\n")
        steps = steps.strip()
        coordinates = coordinates.strip()
        return steps, coordinates


def process_coordinates(coordinates: str) -> dict:
    """Process the coordinates and return a dictionary."""
    # Initialize an empty dictionary
    result_dict = {}

    # Process each line and populate the dictionary
    for line in coordinates.split("\n"):
        key, value = map(str.strip, line.split("="))
        value = tuple(map(str.strip, value[1:-1].split(",")))
        result_dict[key] = value
    return result_dict


def main_logic(steps: str, coordinates: str) -> int:
    """Main logic for the puzzle. We need to find the total steps."""
    # Process the coordinates
    coordinate_dict = process_coordinates(coordinates=coordinates)
    start_point = "AAA"
    current_loc = start_point
    final_dest = "ZZZ"
    steps_nr = 0
    mapped_steps = [0 if step == "L" else 1 for step in steps]
    steps_index = 0

    while current_loc != final_dest:
        current_loc = coordinate_dict[current_loc][mapped_steps[steps_index]]
        steps_nr += 1
        steps_index = (steps_index + 1) % len(steps)

    return steps_nr


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    steps, coordinates = get_input(filepath="/Users/bryan/aoc/day8/input.txt")

    # Iterate through each line
    answer = main_logic(steps=steps, coordinates=coordinates)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 6


if __name__ == "__main__":
    solve_puzzle()
