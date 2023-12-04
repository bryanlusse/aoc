# Advent of Code 2023 - Day 4: Scratchcards

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

We are given some input file with outcomes of scratchcards. On one side we have the winning numbers and on the other side we have the numbers on the card. It is our job to find the winning numbers on our card and then calculate a score. We then sum the scores of all the cards and that is our final answer.
This was a relatively easy problem, as long as you take into account to remove any empty string characters (I had a lot of winning numbers that were empty strings 🤦)

## Part 2

Now, we are asked to do something a bit more difficult. When we now play a game and get winning numbers, the amount of winning numbers determines how many additional scratch cards we get. If we get 3 winning numbers on scratch card 1, that means we get additional copies of scratch cards 2, 3 and 4. These additional copies can get additional copies of themselves!

In the initial implementation my code kept track of all additional copies in a list, however, as we have many additional copies, the size of this list grows very large. Looking up the amount of copies for a certain scratch card id therefore gets quite slow. In order to optimize my code I decided to keep track of the additional copies in a dictionary, where the keys are the scratch card id and the value is the amount of additional copies. This sped up my code by quite a bit!

Happy coding!
