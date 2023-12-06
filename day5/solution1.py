"""Solution to day 4, part 1 puzzle on adventofcode.com"""


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
    locations = []
    seeds = seeds.split(":")[1].strip().split(" ")
    for seed in seeds:
        seed = int(seed)
        val = seed
        for _i, processed_map in enumerate(processed_maps):
            for _key, value in processed_map.items():
                if val in range(value[1], value[1] + value[2]):
                    val = (val - value[1]) + value[0]
                    break
        locations.append(val)

    return min(locations)


def solve_puzzle() -> None:
    """Solve today's puzzle."""
    # Get the input data
    input_data = get_input(filepath="/Users/bryan/aoc/day5/input.txt")

    # Iterate through each line
    answer = main_logic(input_data=input_data)

    # Print the result
    print(f"The answer is: {answer}")
    # assert answer == 35


if __name__ == "__main__":
    solve_puzzle()
