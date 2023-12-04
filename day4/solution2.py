"""Solution to day 4, part 1 puzzle on adventofcode.com"""

from collections import Counter


def get_input(filepath: str) -> str:
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.readlines()


def main_logic(input_data: list) -> int:
    """Main logic for the puzzle. We need to find the total number of won cards."""
    final_cards = {}
    for i, line in enumerate(input_data):
        line = line.split("\n")[0]
        line = line.split("|")
        winning = line[0].split(":")[1].strip().split(" ")
        winning = [value for value in winning if value != ""]
        cards = line[1].strip().split(" ")
        cards = [value for value in cards if value != ""]

        overlap = list(set(winning) & set(cards))
        matches = len(overlap)
        if matches != 0:
            matched_cards = list(range(i + 2, i + matches + 2))
            try:
                duplicate_cards = final_cards[i + 1] + 1
            except KeyError:
                duplicate_cards = 1
            matched_cards = matched_cards * duplicate_cards
            occurences = dict(Counter(matched_cards))
            for key, value in occurences.items():
                try:
                    final_cards[key] = final_cards[key] + value
                except KeyError:
                    final_cards[key] = value

    return sum(final_cards.values()) + (i + 1)


# 5667240


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
