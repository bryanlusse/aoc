"""Solution to day 9, part 2 puzzle on adventofcode.com"""


def get_input(filepath: str) -> list[str]:
    """Get the input data"""
    with open(filepath) as file:
        data = file.readlines()
        return data


def extrapolate_value(line: str) -> int:
    """Process the line and return an extrapolated value."""
    values = line.split(" ")
    values = [int(value) for value in values]
    stages = {}
    counter = 0
    while values != ([0] * len(values)):
        stages[counter] = values
        values = [t - s for s, t in zip(values, values[1:])]
        counter += 1

    prev_value = 0
    for _key, value in dict(sorted(stages.items(), reverse=True)).items():
        prev_value = value[0] - prev_value
    return prev_value


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total steps."""
    answer = 0
    for line in input_data:
        answer += extrapolate_value(line.strip())
    return answer


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day9/input.txt")

    # Iterate through each line
    answer = main_logic(input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 2


if __name__ == "__main__":
    solve_puzzle()
