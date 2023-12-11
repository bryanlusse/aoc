# Advent of Code 2023 - Day 9: Mirage Maintenance

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

We are given some input file with ranges of numbers. It is our job to find the next number for every range. We have to do this by looking at the differences between numbers, and at the differences between those numbers. In other words, we have to find the pattern. This solution is quite straightforward. Keep finding differences untill the resulting differences are all zeroes and then working your way back again by adding all final values of the differences together.
Make sure to exactly match a list of 0 valued numbers (the input file has negative numbers, because of which the sum of all differences will be 0 without all values being 0).

## Part 2

Now, we are asked to do something a tiny bit harder, we need to calculate the _previous_ value. In order to do this, we only have to change our 'calculating back' logic. Instead of adding the final values together, we need to subtract the first value of the previous iteration, from the first value of the current iteration. This was a good day!

Happy coding!
