# Advent of Code 2023 - Day 12: Hot Springs

🌟 **Happy Advent of Code!** 🎄✨

## Part 1

The exercise for this day has some caveats. We get some sample input that represents `condition records` for hot springs and their operational status / condition. These records contain unknowns, but do have a correct `total` amount of damaged hot springs. It is our job to find out how many possible configurations could satisfy every row of the condition records.

After being inspired by [Domyy95](https://github.com/Domyy95/Challenges/blob/master/2023-12-Advent-of-code/12.py) I realised we can use a recurrent function to keep checking how many possible arrangements there are.

## Part 2

For part 2, not a lot changes. Our input now needs to be timesed by 5 (`x5`), both the unknown operational statusses and the totals of damaged hot springs. This can be achieved in a few lines, however, it quickly blows up the amount of computations we have to do (in the example, one row went from having `10` possible arrangements to having `506250` possible arrangements 😱). In order to deal with this we can use a nice Python feature: The `cache` [decorator](https://docs.python.org/3/library/functools.html).

```python
from functools import cache

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

>>> factorial(10)      # no previously cached result, makes 11 recursive calls
3628800
>>> factorial(5)       # just looks up cached value result
120
>>> factorial(12)      # makes two new recursive calls, the other 10 are cached
479001600
```

As we can see, the `@cache` decorator caches function returns. Aka, if we call `factorial(10)` all computations will be done, but if we afterwards calculate `factorial(5)`, the result has already been cached and can be given to us in lightning speed.
The same applies to our function for part 2. Calls that have already been made do not have to be calculated from scratch again. As we fivefold all our calculations this comes in very handy.

Fun fact, this decorator has been in Python since `Python3.9`.

Happy coding!
