# Advent of Code 2023 - Day 2: Cube Conundrum

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

We are given some input file with records of games where the Elf retrieves a random amount of cubes from his bag. We need to check what games would have been possible if there was a maximum amount of cubes per color. In order to this, we need to parse all game results and asses if the amount of cubes in a single grab are smaller than the maximum amount. If the amount is bigger than the maximum amount, this game is not possible. Then we sum over all game id's of the possible games to get the answer.

I used regular expressions again in order to parse the number of cubes from the pieces of text. I used different regexes for the different colour cubes in order to split these results easily. So for red cubes I would use `(/d) red`, since in the end we are only concerned with the digit. This puzzle was quite straightforward if you remember to add up the game id's correctly (if you choose to use indices from the loop like me, remember that Python starts counting at 0 😬).

## Part 2

Now, we are asked to find the minimum amount of cubes that is necessary for each game to be possible, and to calculate the power of those numbers:

```python
power = min_red_cubes * min_green_cubes * min_blue_cubes
```

In order to this, we need to find the largest numbers of each color cube per game, and multiply these. Make sure to convert your strings to integers before calculating the maximum!
Besides that this challenge was quite straightforward.

Happy coding!
