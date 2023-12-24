# Advent of Code 2023 - Day 16: The Floor Will Be Lava

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

In today's task we are asked to code the path for a light beam refracting through a certain path made of empty space (`.`), mirrors (`/` and `\`), and splitters (`|` and `-`). Afterwards we need to find the number of tiles we have touched in our path. Some parts seemed familiar to [Day 10](https://github.com/bryanlusse/aoc/tree/main/day10) as we also have some specific logic when running into specific characters. However, I decided not to reuse the same logic but was intrigued by `xavdid`'s [solve](https://advent-of-code.xavd.id/writeups/2023/day/16/). I followed this path to the answer (although I did not blindly want to copy, so I added some (unfortnately inefficient) logic of my own).

## Part 2

In the second part, we are required to find the **biggest** possible number of tiles. We can do this by performing our solution to part 1 multiple times and retaining the highest value. Again thanks to `xavdid` for the inspiration.

Happy coding!
