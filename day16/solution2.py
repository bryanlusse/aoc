"""Solution to day 16, part 2 puzzle on adventofcode.com"""

import numpy as np
from dataclasses import dataclass

direction_dict = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

@dataclass(frozen=True)
class State:
    location: tuple
    facing: str

    @property
    def next_loc(self) -> tuple:
        """Get the next location"""
        direction = direction_dict[self.facing]
        summed_loc = tuple(x + y for x, y in zip(self.location, direction))
        return summed_loc

    def step(self) -> "State":
        return State(self.next_loc, self.facing)

    def turned_step(self, direction) -> "State":
        if direction == 'left':
            turned_loc = tuple(x + y for x, y in zip(self.location, (0, -1)))
            return State(turned_loc, 'left')
        elif direction == 'right':
            turned_loc = tuple(x + y for x, y in zip(self.location, (0, 1)))
            return State(turned_loc, 'right')
        elif direction == 'up':
            turned_loc = tuple(x + y for x, y in zip(self.location, (-1, 0)))
            return State(turned_loc, 'up')
        elif direction == 'down':
            turned_loc = tuple(x + y for x, y in zip(self.location, (1, 0)))
            return State(turned_loc, 'down')


    def next_states(self, character: str):
        """Get the next states"""
        match character:
            case ".":
                return [self.step()]
            # ignore the pointy end of a splitter
            case "-" if self.facing in ('left', 'right'):
                return [self.step()]
            case "|" if self.facing in ('up', 'down'):
                return [self.step()]
            # split on splitters we didn't pass over
            case "-":
                return [
                    self.turned_step('right'),
                    self.turned_step('left'),
                ]
            case "|":
                return [
                    self.turned_step('up'),
                    self.turned_step('down'),
                ]
            # mirror
            case "/" if self.facing == 'up':
                return [self.turned_step('right')]
            case "/" if self.facing == 'right':
                return [self.turned_step('up')]
            case "/" if self.facing == 'down':
                return [self.turned_step('left')]
            case "/" if self.facing == 'left':
                return [self.turned_step('down')]
            case "\\" if self.facing == 'up':
                return [self.turned_step('left')]
            case "\\" if self.facing == 'right':
                return [self.turned_step('down')]
            case "\\" if self.facing == 'down':
                return [self.turned_step('right')]
            case "\\" if self.facing == 'left':
                return [self.turned_step('up')]
            case _:
                raise ValueError(
                    f"Unable to calculate next step from {self} and {char=}"
                )

def get_input(filepath: str) -> np.ndarray:
    """Get the input data"""
    with open(filepath) as file:
        data = file.readlines()
        array = np.array([list(row.strip()) for row in data])
        return array

def reflect_beam(input_data: np.ndarray, start: State) -> np.ndarray:
    """Reflect the beam"""

    seen: set[State] = set()
    queue: list[State] = [start]

    while queue:
        current = queue.pop()
        if current in seen:
            continue
        seen.add(current)

        for next_state in current.next_states(input_data[current.location]):
            if all(0 <= coord < dim for coord, dim in zip(next_state.location, input_data.shape)):
                queue.append(next_state)

    return len({state.location for state in seen})


def main_logic(input_data: np.ndarray) -> int:
    """Main logic for the puzzle. We need to find the total amount of steps."""
    grid_size = len(input_data)

    return max(
        # top, facing down
        *(
            reflect_beam(input_data, State((0, col), 'down'))
            for col in range(grid_size)
        ),
        # right, facing left
        *(
            reflect_beam(input_data, State((row, grid_size - 1), 'left'))
            for row in range(grid_size)
        ),
        # bottom, facing up
        *(
            reflect_beam(input_data, State((grid_size - 1, col), 'up'))
            for col in range(grid_size)
        ),
        # left, facing right
        *(
            reflect_beam(input_data, State((row, 0), 'right'))
            for row in range(grid_size)
        ),
    )


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day16/input.txt")

    # Iterate through each line
    answer = main_logic(input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 51


if __name__ == "__main__":
    solve_puzzle()
