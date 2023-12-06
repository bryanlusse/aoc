# Advent of Code 2023 - Day 4: Scratchcards

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

We are given some input file with times and distances of records for toy boat races. We need to calculate in how many ways we can beat these records. The toy boats have a button that charges them up to a speed related to the time the boat has been pressed. Initially I bruteforced my way through these, but in Part 2 I decided to optimize.
The brute force way here is to actually go through all scenario's. So I created a list of possible options regarding holding the button, calculated the distance that would be achieved in the record time and then compared these distances to the distance of the record.

## Part 2

Now, we are asked to do something a bit more difficult. Now we don't have multiple races, but one super big race. In this way the previous strategy gets computationally inefficient. Not as inefficient as day 5 but still.

The way to optimize our code is to put our code as an equation and solve for the unknown. We can then realize that the distances we get follow a quadratic distibrution and the way to solve that is the goold old 'abc' formula:

In order to get a win our distance needs to be bigger than the record distance, aka the following must hold

```
x * (time - x) > distance
```

Where x is the time spent holding the button

```
x * (x - time) > distance
x^2 - time*x > distance
x^2 - time*x - distance > 0
```

To solve this we do:

```python
a = 1
b = -int(time)
c = int(distance)
high_x = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
low_x = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
wins = math.floor(high_x - low_x)
```

Happy coding!
