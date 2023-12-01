# Advent of Code 2023 - Day 1: Trebuchet?!

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

We are given some input file with coordinates that are hidden within the text. For every line we need to extract the first and last digit and put them together to make a 2 digit number. Then we need to sum all the 2 digit numbers to come to our answer.
I used regular expressions in order to parse digits from the pieces of text. When using `(/d)` one can extract single digits even if they are a part of bigger digit numbers. After extraction I selected the first and last matches and combined them, after which I summed all values.

## Part 2

Now, we learn that also the spelled out digits need to be taken into account. I updated my regular expression to also taking spelled out digits into account:

```
(one|two|three|four|five|six|seven|eight|nine|zero|\d)
```

Additionally, in order to map these string representations to actual numerical strings, I made a mapping dictionary that maps the spelled out version `one` to a digit version `1`.

But here comes the tricky part. Some parts of the text contain letters that are combined like this:

```
fcbdjhdndjchqlvdv2sixoneseven4fhfhxrrrxeightwotpt
```

Where we see that the first digit is a `2` and the last digit is a `two`. However, the `t` is shared between the `eight` and `two`. In my original regular expression this is not taken into account, resulting in an answer of `28` for this line. In order to fix this, I decided to make the possible overlapping digits optional in the regular expression. This made me end up on an expression like this:

```
(o?ne|t?wo|t?hree|four|five|six|seven|e?ight|n?ine|zero|\d)
```

This regular expression enabled me to get to the correct answer.

Happy coding!
