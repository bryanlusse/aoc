# Advent of Code 2023 - Day 13: Point of Incidence

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

Today, our task is to find the line of reflection in maps that consist of ash (`.`) and rocks (`#`). This exercise took me a little while. The logic to calculate the lines of reflections was a little bit more sophisticated then I thought. In order to find this line, my final approach was to loop over all indices and in each iteration split the array in two parts (up untill the specified index and from the index onwards). In order to compare the two halves we need to make them the same length by trimming some excess columns. After we do this we can check if the remaining columns are the mirror image of eachother. If so, we return the index we are currently on, if not, then we keep going.

It is good to note that this operation should be done both on the columns and on the rows, as the lines of reflections can occur in both dimensions. An easy way to do this is to transpose our matrix, so we can treat rows as columns.

## Part 2

For part 2, instead of a perfect mirror image, we actually want a mirror image that is perfect on all but one spot. As we use the `np.count_nonzero()` function on our equal assignment of both halves, we actually count how many places are different in both parts. In the case that this number is `1` (instead of `0` in part 1), we know that we have found our smudged line of reflection.

Happy coding!
