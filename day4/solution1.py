"""Solution to day 4, part 1 puzzle on adventofcode.com"""


def get_input(filepath: str) -> list[str]:
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.readlines()


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total number of points."""
    answer = 0
    for line in input_data:
        print(f"line: {line}")
        line = line.split("\n")[0]
        line = line.split("|")
        winning = line[0].split(":")[1].strip().split(" ")
        winning = [value for value in winning if value != ""]
        cards = line[1].strip().split(" ")
        cards = [value for value in cards if value != ""]

        overlap = list(set(winning) & set(cards))
        print(f"overlap: {overlap}")
        if len(overlap) < 1:
            points = 0
        elif len(overlap) == 1:
            points = 1
        else:
            points = 1
            for _value in overlap[1:]:
                points *= 2
        answer += points
    return answer


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day4/input.txt")

    # Iterate through each line
    answer = main_logic(input_data=input_data)

    # Print the result
    print(f"The answer is: {answer}")


if __name__ == "__main__":
    solve_puzzle()
