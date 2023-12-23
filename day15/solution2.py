"""Solution to day 15, part 2 puzzle on adventofcode.com"""

import re
from typing import Dict

pattern = re.compile(r"[-=]")


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


def do_box_logic(boxes: Dict, box: int, orig_string: str, split_string: str) -> None:
    """Do the box logic"""
    if "-" in orig_string:
        if box not in boxes.keys():
            pass
        else:
            existing_list = boxes[box]
            filtered_list = [string for string in existing_list if string.split("=")[0] != split_string[0]]
            boxes[box] = filtered_list
    else:
        if box not in boxes.keys():
            boxes[box] = []
        existing_list = boxes[box]
        contains_substring = any(split_string[0] == string.split("=")[0] for string in existing_list)

        if contains_substring:
            updated_list = [
                orig_string if split_string[0] == string.split("=")[0] else string for string in existing_list
            ]
            boxes[box] = updated_list
        else:
            existing_list.append(orig_string)
            boxes[box] = existing_list
    return boxes


def calculate_boxes(boxes: Dict) -> int:
    """Calculate the boxes"""
    answer = 0
    for box in boxes:
        for i, string in enumerate(boxes[box]):
            answer += (int(box) + 1) * (i + 1) * int(string[-1])
    return answer


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total value of the boxes."""
    boxes = {}
    for string in input_data:
        split_string = pattern.split(string)
        box = calculate_hash(split_string[0])
        boxes = do_box_logic(boxes, box, string, split_string)
    answer = calculate_boxes(boxes)
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
    # assert answer == 145


if __name__ == "__main__":
    solve_puzzle()
