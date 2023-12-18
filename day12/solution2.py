"""Solution to day 12, part 2 puzzle on adventofcode.com"""

from functools import cache


def get_input(filepath: str) -> list[str]:
    """Get the input data"""
    with open(filepath) as file:
        data = file.readlines()
        return data


@cache
def count_arrangements(unknowns, damaged_groups):
    """Count the number of possible arrangements of damaged springs"""
    if not damaged_groups:
        # If there is no damaged spring, there is only 1 possible arrangement
        return int("#" not in unknowns)

    if not unknowns:
        # There are no unknown springs, so there is only 1 possible arrangement if we have no damaged groups
        return int(not damaged_groups)

    result = 0

    # Case 1: If the next spring is operational or unknown
    if unknowns[0] in ".?":
        # Recursively call the function with remaining unknowns and the same damaged groups
        # Only damaged springs give us information we can use the damaged groups for
        result += count_arrangements(unknowns[1:], damaged_groups)

    # Case 2: If the first unknown spring is damaged or unknown
    if unknowns[0] in "#?":
        # We get the next consecutive amount of damaged springs
        first_group_size = damaged_groups[0]

        # Check conditions for placing a damaged group at the beginning of the row
        if (
            first_group_size <= len(unknowns)
            and "." not in unknowns[:first_group_size]
            and (first_group_size == len(unknowns) or unknowns[first_group_size] != "#")
        ):
            # Recursively call the function with remaining unknowns after the damaged group and remaining damaged groups
            result += count_arrangements(unknowns[first_group_size + 1 :], damaged_groups[1:])

    return result


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total amount of configurations."""
    answer = 0
    for line in input_data:
        unknowns, damaged_groups = line.split()
        unknowns = "?".join([unknowns] * 5)
        damaged_groups = eval(damaged_groups)  # noqa: PGH001
        damaged_groups = damaged_groups * 5
        answer += count_arrangements(unknowns, damaged_groups)
    return answer


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day12/input.txt")

    # Iterate through each line
    answer = main_logic(input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 374


if __name__ == "__main__":
    solve_puzzle()
