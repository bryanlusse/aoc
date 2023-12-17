# Advent of Code 2023 - Day 11: Cosmic Expansion

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

Today wasn't a bad day. We are given some input file with characters that make up a universe. It consist of empty space (`.`) and galaxies (`#`). It is our job to calculate the distances between all unique pairs of galaxies. We then want to sum all of those distances in order to get to our answer. However, the universe expands, so empty space (columns or rows) gets twice as big. Initially I calculated this fully expanded universe, but as you see in part 2, this is not needed.
Things to keep in mind:

- Although the example calculates the shortest distance as some zig-zag pattern, it is the same distance as the Manhattan distance. Therefore you can just use that.
- Don't forget you only have to calculate each distance once. So using the test input you should only have to calculate 36 distances.

## Part 2

Now, our universe does not expand twice (x2), but it expands a million times (x1000000). To calculate our expanded universe again would cost substantially more memory. In order to not do that, we can use our original universe and keep track of which rows and columns will expand. For our distances, we calculate the distances in the unexpanded universe and then multiply with a factor that takes into account the expansion. For that we first need to check how many rows or columns on each path have expanded, but this is quite easy to do.

Happy coding!
