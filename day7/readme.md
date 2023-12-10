# Advent of Code 2023 - Day 7: Camel Cards

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

We are given some input file with card hands and bids. It is our job to rank all the hands (using poker-like rules) and calculate the total winnings. I set up some function to sort the different hands into the different types (five of a kind, full house etc.) As this already gives some order. Afterwards I sort the hands by a custom sorting mechanism to make sure the ranking is correct.

## Part 2

Now, we are asked to do something similar, however also `Jokers` are part of the game now. I decided to not make my mapping life difficult and just remove the jokers from the hands. However, we do need them afterwards again to calculate the correct ranking of the hands, so I only remove them temporarily. Don't forget to update your custom sorting mechanism correctly, as the `J` was already a previously possible value (just adding the `J` at the end will not work).

Happy coding!
