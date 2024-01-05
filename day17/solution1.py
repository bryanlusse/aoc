"""Solution to day 17, part 1 puzzle on adventofcode.com"""

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import List

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


@dataclass(frozen=True, order=True)
class Point:
    """Immutable class representing a 2D point with x and y coordinates."""

    x: int
    y: int

    def move(self, direction: int, distance: int) -> "Point":
        """Move the point in the specified direction by the given distance."""
        return Point(self.x + DIRS[direction][0] * distance, self.y + DIRS[direction][1] * distance)


@dataclass(frozen=True, order=True)
class State:
    """Immutable class representing the state in the search algorithm."""

    cost: int
    point: Point
    disallowed_direction: int

    def generate_next_state(self, direction: int, distance: int, cost_increase: int) -> "State":
        """Generate the next state after moving in the specified direction."""
        new_point = self.point.move(direction, distance)
        return State(self.cost + cost_increase, new_point, direction)


def get_input(filepath: str) -> List[List[int]]:
    """Get the input data"""
    with open(filepath) as file:
        data = [[int(y) for y in x] for x in file.read().strip().split("\n")]
        return data


def in_range(pos: Point, input_data: List[List[int]]) -> bool:
    """Check if the given point is within the boundaries of the 2D array."""
    return pos.x in range(len(input_data)) and pos.y in range(len(input_data[0]))


def calculate_shortest_path(input_data: List[List[int]], mindist: int = 1, maxdist: int = 3) -> int:
    """Run the search algorithm to find the shortest path with specific constraints."""
    start = Point(0, 0)
    goal = Point(len(input_data) - 1, len(input_data[0]) - 1)
    initial_state = State(cost=0, point=start, disallowed_direction=-1)

    q = [initial_state]
    seen = set()
    costs = {}

    while q:
        current_state = heappop(q)

        if current_state.point == goal:
            return current_state.cost

        if current_state in seen:
            continue

        seen.add(current_state)

        for direction in range(4):
            # loop over all 4-connected directions
            cost_increase = 0

            if (
                direction == current_state.disallowed_direction
                or (direction + 2) % 4 == current_state.disallowed_direction
            ):
                continue

            for distance in range(1, maxdist + 1):
                next_point = Point(
                    current_state.point.x + DIRS[direction][0] * distance,
                    current_state.point.y + DIRS[direction][1] * distance,
                )

                if in_range(next_point, input_data):
                    cost_increase += input_data[next_point.x][next_point.y]

                    if distance < mindist:
                        continue

                    next_state = current_state.generate_next_state(direction, distance, cost_increase)

                    if costs.get((next_point, direction), 1e100) <= next_state.cost:
                        continue

                    costs[(next_point, direction)] = next_state.cost
                    heappush(q, next_state)

    return -1


def main_logic(input_data: List[List[int]]) -> int:
    """Main logic for the puzzle. We need to find the total amount of steps."""
    return calculate_shortest_path(input_data)


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day17/input.txt")

    # Iterate through each line
    answer = main_logic(input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 102


if __name__ == "__main__":
    solve_puzzle()
