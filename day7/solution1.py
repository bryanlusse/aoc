"""Solution to day 7, part 1 puzzle on adventofcode.com"""

import numpy as np

char_order = "AKQJT98765432"


def get_input(filepath: str) -> list[str]:
    """Get the input data"""
    with open(filepath) as file:
        hands = []
        bids = []
        data = file.readlines()
        for line in data:
            hand, bid = line.split(" ")
            hands.append(hand.strip())
            bids.append(bid.strip())
        bids = [int(bid) for bid in bids]
        return hands, bids


def get_ranks(hands: str) -> int:
    """Get the rank of the hand."""
    ranked = {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}
    final_ranked = []
    for hand in hands:
        # Find duplicate numbers in string
        duplicates = {x: hand.count(x) for x in hand if hand.count(x) > 1}
        if len(duplicates) == 0:
            ranked["1"].append(hand)
        elif (len(duplicates) == 1) & (5 in duplicates.values()):
            ranked["7"].append(hand)
        elif (len(duplicates) == 1) & (4 in duplicates.values()):
            ranked["6"].append(hand)
        elif (len(duplicates) == 2) & (3 in duplicates.values()):
            ranked["5"].append(hand)
        elif (len(duplicates) == 1) & (3 in duplicates.values()):
            ranked["4"].append(hand)
        elif (len(duplicates) == 2) & (2 in duplicates.values()):
            ranked["3"].append(hand)
        elif (len(duplicates) == 1) & (2 in duplicates.values()):
            ranked["2"].append(hand)
        else:
            print("Something went wrong")
    for _key, value in dict(sorted(ranked.items())).items():
        # Do some extra ranking for the letters
        sorted_list = sorted(value, key=lambda x: [char_order.index(c) for c in x], reverse=True)
        final_ranked = final_ranked + sorted_list
    ranks = [final_ranked.index(value) + 1 for value in hands]
    return ranks


def main_logic(hands: list[str], bids: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total winnings."""
    ranks = get_ranks(hands=hands)
    winnings = np.dot(ranks, bids)
    return winnings


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    hands, bids = get_input(filepath="/Users/bryan/aoc/day7/input.txt")

    # Iterate through each line
    answer = main_logic(hands=hands, bids=bids)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 6440


if __name__ == "__main__":
    solve_puzzle()
