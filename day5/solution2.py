"""Solution to day 4, part 1 puzzle on adventofcode.com"""

import time


def get_input(filepath: str) -> list[str]:
    """Get the input data as a list of strings."""
    with open(filepath) as file:
        return file.read()


def main_logic(input_data: list[str]) -> int:
    """Main logic for the puzzle. We need to find the total number of points."""
    (
        seeds,
        seed_soil,
        soil_fertilizer,
        fertilizer_water,
        water_light,
        light_temperature,
        temperature_humidity,
        humidity_location,
    ) = input_data.split("\n\n")
    production_maps = [
        seed_soil,
        soil_fertilizer,
        fertilizer_water,
        water_light,
        light_temperature,
        temperature_humidity,
        humidity_location,
    ]
    processed_maps = []
    for _i, production_map in enumerate(production_maps):
        production_map = production_map.split(":")[1].strip().split("\n")
        processed_map = {}
        for j, line in enumerate(production_map):
            dst_range_start, src_range_start, range_length = line.split(" ")
            dst_range_start = int(dst_range_start)
            src_range_start = int(src_range_start)
            range_length = int(range_length)
            processed_map[j] = [dst_range_start, src_range_start, range_length]
        processed_maps.append(processed_map)
    seeds = seeds.split(":")[1].strip().split(" ")
    seed_pairs = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    final_seeds = []
    for seed_pair in seed_pairs:
        start, length = seed_pair
        final_seeds += list(range(int(start), int(start) + int(length)))

    start = 1
    length = 100

    for location in range(int(start), int(start) + int(length)):
        location = int(location)
        val = location
        for _i, processed_map in enumerate(processed_maps[::-1]):
            for _key, value in processed_map.items():
                if val in range(value[0], value[0] + value[2]):
                    val = (val - value[0]) + value[1]
                    break
        if val in final_seeds:
            break

    return location


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day5/input.txt")

    # Iterate through each line
    answer = main_logic(input_data=input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 46


if __name__ == "__main__":
    time_now = time.time()
    solve_puzzle()
    print(f"Time taken: {time.time() - time_now}")
