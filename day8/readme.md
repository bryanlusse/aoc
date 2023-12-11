# Advent of Code 2023 - Day 8: Haunted Wasteland

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

We are given some input file with steps to take and coordinates with their direct neighbours. It is our job to find the amount of steps it takes us to go from the start coordinate `AAA` to the end coordinateb `ZZZ`. I processed the coordinates in order to make a mapping dictionary that maps every location to its direct neigbours. Then we can easily move from the start location all the way to the end.

## Part 2

Now, we are asked to do something a little harder, we need to find the amount of steps it takes us to get from all coordinates ending in an A `XXA` to all coordinates ending in a `XXZ`. We only count this when we reach all `XXZ` coordinates at the same time. Initially, I tried to do it in a similar way, just looping over all possible start and end points. However, once you realize that the paths you can take to end up at a similar coordinate will loop (there are a finite amount of coordinates after all) this becomes a different problem. We can calculate how long it takes to get to any end coordinate from a starting coordinate, do that for every starting coordinate, and find the lowest common multiplier (LCM) of all those values. In the end that gets us the right solution. For a more in depth explanation, see the following [link](https://www.reddit.com/r/adventofcode/comments/18e6vdf/2023_day_8_part_2_an_explanation_for_why_the/)

Happy coding!
