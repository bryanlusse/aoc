# Advent of Code 2023 - Day 3: Gear Ratios

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

We are given some input file with numbers and symbols. We should extract the numbers that are adjacent (also diagonally) to any symbols. I decided to first extract all symbols and _then_ the adjacent numbers (which showed to be an inefficient solution, but more about that later). I did this by extracting the string input as a grid and then looping over every entry trying to find if it was a symbol or not. After I found a symbol, I would find the 8 connected neighbours (if not a position on an edge) to check if they were digits and if they had digits next to them (a number like `667` will take up 3 places on the grid. If only the 7 is adjacent to the symbol, the number will still count). For every neighbour I would extract the number and check if it was not already found (which is a tricky thing as the same numbers showed up multiple times in the text and even on the same line). Only if it was not already found I would add it to the sum.

This method was inefficient as we extracted certain numbers multiple times (if they had multiple connections to the same symbol). An easy improvement is to search for the numbers instead of the symbols. In this way we only find the numbers once, and can add them to symbols easily.

Github user jmerle gives a great [example](https://github.com/jmerle/advent-of-code-2023/blob/master/src/day03/part1.py) of this.

There were quite some edge cases included in the input but not in the test, making this a very challenging task!

## Part 2

Now, we are asked to find the gear ratio

```python
gear_ratio = adjacent_number_1 * adjacent_number_2
```

only for numbers adjacent to a `*` symbol (with logically only 2 adjacent numbers).

In order to this, I changed my code to only take the `*` symbol into account. Additionally I saved adjacent numbers as value in a dictionary with the symbol coordinates as key. After finding all adjacent numbers again, I only multiplied the values in this dictionary where the length was 2 (i.e. 2 adjacent numbers).

Happy coding!
