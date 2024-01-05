# Advent of Code 2023 - Day 17: Clumsy Crucible

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

In today's task we are asked to navigate lava through a city on gear island. We get a map of the city and the heat loss per city block. We need to find the shortest path from the starting point (top left point `[0,0]`) to the destination (bottom right point `[input.shape[0]-1, input.shape[1]-1]`) while keeping to the condition of only moving in a straight line for at most three blocks.

In order to solve this we turn to [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), which is a popular algorithm for finding short paths. Dijkstra's algorithm, works by exploring the map, as a graph, in a greedy manner. It loops over neighbouring points and keeps picking the neighbours that result in the lowest heat loss.

In our implementation, the `Point` dataclass encapsulates the x and y coordinates, facilitating easy movement in the 2D space. The `State` dataclass captures the current state during the exploration, keeping track of cost, point, and disallowed direction.
Just like in the previous day, we make use of dataclasses, this enhances code clarity and encapsulates the state and point information elegantly.

My solution was inspired by solutions from Reddit users [xavdid](https://advent-of-code.xavd.id/writeups/2023/day/16/) and [leijurv](https://topaz.github.io/paste/#XQAAAQBUBAAAAAAAAAAzHIoib6py7i/yVWhl9dSCjkM4GPHrtd8B89i1ferannGa/iSPEhSfwXSQjO97mxh41OLgLuTQT5wZp7bL+YFnrXGCd60/JWIJ5WDSmI0hG6+qMtQOj2QXDJktThQfZ6yIaRD6IZd0P7FmvoN12N2kW/FQ0qpK6T1z6dICqSYqO0/Ksi5YYpqJcNN8deanbLf8wUaZ+5epfmFAoDmvOVTVXvFnKco4Us7YFjds3fPaa954Jf59LhozJtJsgKGwzGe88BZZsMONFj7eorNEm64UlpMkbwm3AX/f5q4PRVDYidntpWQAOacIkW6P5qxfeTyoBlErtzaTP5jf8rGuQiZfpmE5Y+4Rnyq0tOA0sjBsg5VtPNZsYnWssqb1QXz/C9k+GpgJWC7wibMKcO6LzbFeP3L9zi6gzg1cbzGnh0VMsBaat3ydPU977qz/+phzmMAn4TORuFsJneXjbnokMULP7VkIyB3iY9wyPR3Fq8G09fvU/abyU9ZXNGFZvdfeH1RXmRxd638aQUjWEzugbC7VD4vM/iJEkhhJddEKWgl3642Z0Lgb/RrESf8sAicMP7ehT4u8TNRq4ZKPJJp7DvevdrsSJJ8vM+GuqPD+dqa5/Ee3qsJYdjyCm5j1CpYrJSL+KBjeUWho+l5mablrGuP6/R3+dfiEOfJY0p8nxp+l2C3T+nwpw5s3hgOKXYLdTb+HaMceyd+EAz4R32xkCurWxa5x18ym7USc/CFfmlk5M1WTmgYgShgeG39+cMf/gaRH1A==).

Things to keep in mind:

- Don't forget to check whether a given point is within the boundaries of the 2D array.

## Part 2

In the second part, the constraint on the amount of consecutive steps in the same direction that can be taken is changed. Instead of ranging from 1-3, it needs to range fron 4-10. In our code this is easily changeable by changing the default values for `min_dist` and `max_dist`.

Happy coding!
