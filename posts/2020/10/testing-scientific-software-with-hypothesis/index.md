---
title: "Testing Scientific Software with Hypothesis"
date: 2020-10-28
categories: 
  - "python"
---

Writing unit tests for scientific software is challenging because frequently you don't even know what the output should be. Unlike business software, which automates well-understood processes, here you cannot simply work your way through use case after use case, unit test after unit test. Your program is either correct or it isn't, and you have no way of knowing.

[![](images/image.png)](https://dilbert.com/strip/2018-10-21)

If you cannot know if your program is correct, does it mean you cannot test it? No, but you'll be using other techniques than the ones traditionally used for unit tests. In this piece we'll look at two techniques you can use to test your software. These are:

- comparing the output with a reference (an oracle)
- verifying that the output satisfies certain properties.

And we'll illustrate these two techniques through three examples:

- the square root function
- the trigonometric functions
- a simple Pandas operation

<!--more-->

This piece was originally a Jupyter notebook, so you should be able to copy/paste and run each cell as we go along. First we import the usual packages.

```python
import math
import sys

import numpy as np
import pandas as pd
```

### The square root

The square root of $x$, noted $\\sqrt{x}$, is the non-negative number $y$ such that $y^2 = x$. It is the root of $y^2 - x = 0$. A method to compute that root is the Newton-Raphson algorithm:

1. $y \\leftarrow 1$
2. Repeat $y \\leftarrow \\left.\\left(y + \\frac{x}{y}\\right)\\middle/2\\right.$ until convergence

For the first version of this function we just apply the algorithm as-is:

```python
def sqrt(x):
    y_new = 1
    y_old = 0
    while (y_new != y_old):
        y_new, y_old = (y_new + x / y_new) / 2, y_new
    return y_new

assert sqrt(1) == 1
assert sqrt(4) == 2
assert sqrt(9) == 3
```

Looks pretty reasonable; notice that right after defining my function I run a few unit tests (yes, you _don't need_ a unit testing framework to write unit tests). But how do I know this function will work for all inputs? (Hint: as it stands it has at least two bugs.)

Here's where property testing comes in handy. We know that the square root $y$ of a number $x$ must satisfy $y^2 = x$. One could imaging drawing some numbers at random, and checking that our function satisfies that property:

```python
from numpy.random import uniform

for _ in range(100):
    x = uniform(0., 100.)
    y = sqrt(x)
    assert np.isclose(y**2, x)
```

Great. It works for 100 numbers randomly drawn between 0 and 100, surely the function is correct? Wait a second. What about edge cases?

```python
assert sqrt(0) == 0
```

```
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-4-0b4976dfa332> in <module>
----> 1 assert sqrt(0) == 0

<ipython-input-2-cc00edd81170> in sqrt(x)
      3     y_old = 0
      4     while (y_new != y_old):
----> 5         y_new, y_old = (y_new + x / y_new) / 2, y_new
      6     return y_new
      7 

ZeroDivisionError: float division by zero
```

Oops. How could we forget that one? Clearly randomly drawing test samples is not good enough. But there's a better way, a way to draw random test samples in a smart way which will not overlook edge cases. I'm going to introduce a library that will automate this for us. It's the [Hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html) library.

_Note: what follows is not necessarily deterministic. If you run this on your own, you may get different results. I'm using the `seed` decorator provided by Hypothesis to ensure my output is reproducible on my machine, but real code should **not** do that._

Hypothesis lets you generate test cases automatically, provided you can express properties that the results of your function should satisfy. It's an example of what's known as property-based testing, which seems to have originated with the [QuickCheck](https://hackage.haskell.org/package/QuickCheck) Haskell library.

To use Hypothesis, we install the library and declare some common imports:

```python
from hypothesis import given, seed
from hypothesis import strategies as some
```

Now we need to write a function which accepts an input `x`, and verifies that the tested function satisfies the required properties for `x`:

```python
def test_sqrt_property(x):
    y = sqrt(x)
    assert y >= 0
    assert np.isclose(y**2, x)
    
test_sqrt_property(1)
test_sqrt_property(2)
test_sqrt_property(3)
```

And as expected, the assertion fails for `0` with the same error:

```python
test_sqrt_property(0)
```

```
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-7-1a87a96eae15> in <module>
----> 1 test_sqrt_property(0)

<ipython-input-6-b7c1d0a3deac> in test_sqrt_property(x)
      1 def test_sqrt_property(x):
----> 2     y = sqrt(x)
      3     assert y >= 0
      4     assert np.isclose(y**2, x)
      5 

<ipython-input-2-cc00edd81170> in sqrt(x)
      3     y_old = 0
      4     while (y_new != y_old):
----> 5         y_new, y_old = (y_new + x / y_new) / 2, y_new
      6     return y_new
      7 

ZeroDivisionError: float division by zero
```

To tell Hypothesis about this test function, we decorate it with the `given` decorator (and the `seed` decorator too, but you shouldn't do that as noted above):

```python
@given(some.floats())
@seed(42)
def test_sqrt_property(x):
    y = sqrt(x)
    assert y >= 0
    assert np.isclose(y**2, x)
```

Let's see now what happens when we run `test_sqrt_property`, but _without arguments_ (Hypothesis will generate the test cases for us):

```python
test_sqrt_property()
```

```
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-9-d13ac4e550a3> in <module>
----> 1 test_sqrt_property()

<ipython-input-8-8fe3da5479e4> in test_sqrt_property()
      1 @given(some.floats())
----> 2 @seed(42)
      3 def test_sqrt_property(x):
      4     y = sqrt(x)
      5     assert y >= 0

    [... skipping hidden 1 frame]

<ipython-input-8-8fe3da5479e4> in test_sqrt_property(x)
      2 @seed(42)
      3 def test_sqrt_property(x):
----> 4     y = sqrt(x)
      5     assert y >= 0
      6     assert np.isclose(y ** 2, x)

<ipython-input-2-cc00edd81170> in sqrt(x)
      3     y_old = 0
      4     while (y_new != y_old):
----> 5         y_new, y_old = (y_new + x / y_new) / 2, y_new
      6     return y_new
      7 

KeyboardInterrupt: 
```

Uh-ho… the call never finished and I had to interrupt it myself. Let's crack the debugger open:

```python
%debug
```

```
> <ipython-input-2-cc00edd81170>(5)sqrt()
      3     y_old = 0
      4     while (y_new != y_old):
----> 5         y_new, y_old = (y_new + x / y_new) / 2, y_new
      6     return y_new
      7 

ipdb> print(x)
-inf
ipdb> quit
```

Oh right… it chokes on negative numbers. I'm pretty sure that the algorithm won't work on negative numbers (especially negative infinity), so now I'm confronted with a choice on what to do with negative inputs. Easiest would be to throw an exception:

```python
def sqrt(x):
    if x < 0:
        raise ValueError(f'x should be non-negative but was {x}')
    y_new = 1
    y_old = 0
    while (y_new != y_old):
        y_new, y_old = (y_new + x / y_new) / 2, y_new
    return y_new
```

But we also need to tell Hypothesis to restrict its numbers to non-negative floats:

```python
@given(some.floats(min_value=0))
@seed(42)
def test_sqrt_property(x):
    y = sqrt(x)
    assert y >= 0
    assert np.isclose(y**2, x)
```

```python
test_sqrt_property()
```

```
Falsifying example: test_sqrt_property(
    x=0.0,
)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-13-d13ac4e550a3> in <module>
----> 1 test_sqrt_property()

<ipython-input-12-d15cee5d7b67> in test_sqrt_property()
      1 @given(some.floats(min_value=0))
----> 2 @seed(42)
      3 def test_sqrt_property(x):
      4     y = sqrt(x)
      5     assert y >= 0

    [... skipping hidden 1 frame]

<ipython-input-12-d15cee5d7b67> in test_sqrt_property(x)
      2 @seed(42)
      3 def test_sqrt_property(x):
----> 4     y = sqrt(x)
      5     assert y >= 0
      6     assert np.isclose(y**2, x)

<ipython-input-11-3f4b35a4ce01> in sqrt(x)
      5     y_old = 0
      6     while (y_new != y_old):
----> 7         y_new, y_old = (y_new + x / y_new) / 2, y_new
      8     return y_new

ZeroDivisionError: float division by zero
```

This looks good; Hypothesis found the same bug we did. The square root of 0 is 0, which will eventually be assigned to `y_new`, causing a division by zero error on line 7 (actually a `0 / 0` error). Let's handle that case separately:

```python
def sqrt(x):
    if x == 0:
        return 0
    if x < 0:
        raise ValueError(f'x should be non-negative but was {x}')
    y_new = 1
    y_old = 0
    while (y_new != y_old):
        y_new, y_old = (y_new + x / y_new) / 2, y_new
    return y_new
```

```python
test_sqrt_property()
```

```
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-15-d13ac4e550a3> in <module>
----> 1 test_sqrt_property()

<ipython-input-12-d15cee5d7b67> in test_sqrt_property()
      1 @given(some.floats(min_value=0))
----> 2 @seed(42)
      3 def test_sqrt_property(x):
      4     y = sqrt(x)
      5     assert y >= 0

    [... skipping hidden 1 frame]

<ipython-input-12-d15cee5d7b67> in test_sqrt_property(x)
      2 @seed(42)
      3 def test_sqrt_property(x):
----> 4     y = sqrt(x)
      5     assert y >= 0
      6     assert np.isclose(y**2, x)

<ipython-input-14-0a2e2f1934db> in sqrt(x)
      7     y_old = 0
      8     while (y_new != y_old):
----> 9         y_new, y_old = (y_new + x / y_new) / 2, y_new
     10     return y_new

KeyboardInterrupt: 
```

It still hangs. What was the offending input this time?

```python
%debug
```

```
> <ipython-input-14-0a2e2f1934db>(9)sqrt()
      6     y_new = 1
      7     y_old = 0
      8     while (y_new != y_old):
----> 9         y_new, y_old = (y_new + x / y_new) / 2, y_new
     10     return y_new

ipdb> print(x)
inf
ipdb> quit
```

Ok fine. Let's throw an exception whenever the input is non-finite then:

```python
def sqrt(x):
    if x == 0:
        return 0
    if x < 0:
        raise ValueError(f'x should be non-negative but was {x}')
    if not math.isfinite(x):
        raise ValueError(f'x should be finite but was {x}')
    y_new = 1
    y_old = 0
    while (y_new != y_old):
        y_new, y_old = (y_new + x / y_new) / 2, y_new
    return y_new
```

We also need to tell Hypothesis to exclude infinities:

```python
@given(some.floats(min_value=0, allow_infinity=False))
@seed(42)
def test_sqrt_property(x):
    y = sqrt(x)
    assert y >= 0
    assert np.isclose(y**2, x)
```

```python
test_sqrt_property()
```

```
Falsifying example: test_sqrt_property(
    x=1.7976931348623157e+308,
)
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)
<ipython-input-19-d13ac4e550a3> in <module>
----> 1 test_sqrt_property()

<ipython-input-18-b58fc7c3fdf1> in test_sqrt_property()
      1 @given(some.floats(min_value=0, allow_infinity=False))
----> 2 @seed(42)
      3 def test_sqrt_property(x):
      4     y = sqrt(x)
      5     assert y >= 0

    [... skipping hidden 1 frame]

<ipython-input-18-b58fc7c3fdf1> in test_sqrt_property(x)
      4     y = sqrt(x)
      5     assert y >= 0
----> 6     assert np.isclose(y**2, x)

OverflowError: (34, 'Result too large')
```

What's this now? Hypothesis was trying the largest representable float; its square root, when squared, overflowed. I'm not sure what's the right solution here. It looks like the algorithm works, but we cannot verify it. This is highly embarrassing; I confess I have no better solution than to exclude the largest representable float from the test.

```python
@given(some.floats(min_value=0, max_value=sys.float_info.max, exclude_max=True, allow_infinity=False))
@seed(42)
def test_sqrt_property(x):
    y = sqrt(x)
    assert y >= 0
    assert np.isclose(y**2, x)
```

I'm a little bit nervous about this because the Hypothesis documentation implies that passing a lower bound will exclude `nan` from being passed to the function. I'll cross that bridge when I come to it. For now let's run the tests:

```python
test_sqrt_property()
```

No output? Well after all this noise it's almost an anti-climax to be able to run this test without complaints. Looks like our function passes the property-based testing now.

What about the other kind of test, which I called the oracle test? Can we compare the output of the function with a reference implementation? In this case we can simply compare it with NumPy's `sqrt()` routine, but keep in mind that things won't always be that easy. Let's write another test function, decorated to work with Hypothesis (note that here we don't exclude `inf`):

```python
@given(some.floats(min_value=0, max_value=sys.float_info.max, exclude_max=True))
@seed(23)
def test_sqrt_oracle(x):    
    assert np.isclose(sqrt(x), np.sqrt(x))
```

```python
test_sqrt_oracle()
```

The tests pass, but now I sense your discomfort. How do we even know how much testing is being done here? Hypothesis has a rich set of settings, including `verbosity` which controls how much output is printed. Let's turn it on:

```python
from hypothesis import settings, Verbosity

@given(some.floats(min_value=0, max_value=sys.float_info.max, allow_infinity=False, exclude_max=True))
@settings(verbosity=Verbosity.verbose)
@seed(42)
def test_sqrt_property(x):
    y = sqrt(x)
    assert y >= 0
    assert np.isclose(y**2, x)
```

```python
test_sqrt_property()
```

```
Trying example: test_sqrt_property(
    x=0.0,
)
Trying example: test_sqrt_property(
    x=2.0014004551302755e+307,
)
<... 98 other examples ...>
```

As we can see, Hypothesis has tried 100 examples including `0.0` and extremely large numbers, close to the maximum representable float (in fact it was flirting dangerously close to the maximum with `1.7023370361275787e+308`). I have known many awesome testers in my life, but none who would be that patient or sadistic. I think that's as much testing as we can do and we can probably call it a day.

> Ah, the elusive square root,
> 
> It should be a cinch to compute.
> 
> But the best we can do
> 
> Is use powers of two
> 
> And iterate the method of Newt!

### The sine and cosine functions

Let's do another example, this time with the sine and cosine trigonometric functions. This time we'll begin by comparing the output with NumPy's reference implementation.

It's probably not the best algorithm, but the sine and cosine functions for small arguments can be easily computed from their series expansions:

\\begin{aligned}  
\\sin(x) &= x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - … \\\\  
&= \\sum\_{n=0}^{\\infty}\\frac{(-1)^n x^{2n+1}}{(2n+1)!} \\\\  
\\cos(x) &= 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - … \\\\  
&= \\sum\_{n=0}^{\\infty}\\frac{(-1)^n x^{2n}}{(2n)!}  
\\end{aligned}

```python
def sine(x):
    def sine_terms(x):
        term = x
        n = 1
        while True:
            yield term
            n += 2
            term = -term * x ** 2 / (n * (n - 1))
    y_new = 0
    y_old = -1
    for term in sine_terms(x):
        y_new, y_old = y_new + term, y_new
        if y_new == y_old:
            return y_new

assert np.isclose(sine(0), 0)
assert np.isclose(sine(math.pi), 0)
```

This passes a few manual unit tests. Let's throw Hypothesis at it as well, restricting the arguments to remain less than $\\pi$ in absolute value (as those series expansions are extremely ill-behaved for large numbers):

```python
@given(some.floats(min_value=-math.pi, max_value=math.pi))
def test_sine_oracle(x):
    assert np.isclose(sine(x), np.sin(x))
```

```python
test_sine_oracle()
```

That was almost too easy. Let's do the same thing for cosine:

```python
def cosine(x):
    def cosine_terms(x):
        term = 1
        n = 0
        while True:
            yield term
            n += 2
            term = -term * x ** 2 / (n * (n - 1))
    y_new = 0
    y_old = -1
    for term in cosine_terms(x):
        y_new, y_old = y_new + term, y_new
        if y_new == y_old:
            return y_new
        
assert np.isclose(cosine(0), 1)
assert np.isclose(cosine(math.pi), -1)
```

```python
@given(some.floats(min_value=-math.pi, max_value=math.pi))
def test_cosine_oracle(x):
    assert np.isclose(cosine(x), np.cos(x))
```

```
test_cosine_oracle()
```

Good. Now we'd like to come up with properties against which we can test our implementation. The most obvious one is that these functions must satisfy $\\cos^2(x) + \\sin^2(x) = 1$:

```python
@given(some.floats(min_value=-math.pi, max_value=math.pi))
def test_sum_squares(x):
    assert np.isclose(sine(x) * sine(x) + cosine(x) * cosine(x), 1)
```

```python
test_sum_squares()
```

That's… actually the only property I can think of that's easy to express in code. There's another one I'd like to mention, which I _think_ I've seen implemented in `glibc`'s math library but cannot find anymore. It is based on the observation that two functions $f(x)$ and $g(x)$ that satisfy the differential equations

\\begin{aligned}  
f'(x) &= g(x) \\\\  
g'(x) &= -f(x) \\\\  
\\end{aligned}

must, up to a multiplicative constant, be the sine and cosine functions. To compute the derivative of $f(x)$ I'm going to take it easy and approximate it with $\[f(x + \\Delta x) - f(x - \\Delta x)\]/2\\Delta x$ with a small-ish $\\Delta x$. So that would give us something like:

```python
@given(some.floats(min_value=-math.pi, max_value=math.pi))
def test_trigonometry_differential(x):
    def fprime(f, x):
        return (f(x + 1e-6) - f(x - 1e-6)) / 2e-6
    assert np.isclose(fprime(sine, x), cosine(x))
    assert np.isclose(fprime(cosine, x), -sine(x))
```

```python
test_trigonometry_differential()
```

To be honest, I didn't think this would work.

### Testing functions on Pandas DataFrames

In this final section I want to show how you can test functions that operate on Pandas `DataFrame`s. Hypothesis has a neat extension designed for testing the Pandas + NumPy stack; basically, we're going to generate random `DataFrame`s that satisfy certain conditions, and test the output of our function when applied to those `DataFrame`s. We begin by importing the right modules:

```python
from hypothesis.extra.pandas import data_frames, column
from pandas import Series
```

Let's see if we can write a function that, given two Pandas `Series` of equal length, computes their element-wise average. A simple implementation looks like this:

```python
def avg(x: Series, y: Series) -> Series:
    return (x + y) / 2
```

Congratulations, you just wrote a bug. To see why, let's write a test function powered up to work with Hypothesis. We need to generate two `Series` of the same length. I'm pretty sure it's possible to do so in Hypothesis, but I find it easier to just generate a two-column `DataFrame`:

```python
@given(df=data_frames([
    column('a', dtype=np.float64),
    column('b', dtype=np.float64)
]))
@seed(42)
def test_avg(df):
    assert np.all(np.isclose(np.mean(df, axis=1), avg(df['a'], df['b'])))
```

```python
test_avg()
```

```
Falsifying example: test_avg(
    df=     a   b
    0  0.0 NaN,
)
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-39-0f483bdaa75d> in <module>
----> 1 test_avg()

<ipython-input-38-d7addbe29af3> in test_avg()
      1 @given(df=data_frames([
----> 2     column('a', dtype=np.float64),
      3     column('b', dtype=np.float64)
      4 ]))
      5 @seed(42)

    [... skipping hidden 1 frame]

<ipython-input-38-d7addbe29af3> in test_avg(df)
      5 @seed(42)
      6 def test_avg(df):
----> 7     assert np.all(np.isclose(np.mean(df, axis=1), avg(df['a'], df['b'])))

AssertionError: 
```

Ok, again I get bitten by forgetting that floats can be `nan`. Let's cop out of this one and assume the input must be finite. It means we cannot use the `dtype` argument but the less elegant `elements`:

```python
@given(df=data_frames([
    column('a', elements=some.floats(allow_nan=False, allow_infinity=False)),
    column('b', elements=some.floats(allow_nan=False, allow_infinity=False))
]))
@seed(42)
def test_avg(df):
    assert np.all(np.isclose(np.mean(df, axis=1), avg(df['a'], df['b'])))
```

```python
test_avg()
```

```
/opt/anaconda3/envs/testing/lib/python3.7/site-packages/numpy/core/_methods.py:38: RuntimeWarning: overflow encountered in reduce
  return umr_sum(a, axis, dtype, out, keepdims, initial, where)
```

I _hate_ this. The test function returned… but there was a warning? Let's force Python to treat warnings as errors, and re-run the test:

```python
import warnings

warnings.resetwarnings()
warnings.simplefilter('error')
test_avg()
```

```
Falsifying example: test_avg(
    df=               a              b
    0  6.286897e+293  1.797693e+308,
)
---------------------------------------------------------------------------
RuntimeWarning                            Traceback (most recent call last)
<ipython-input-42-6ade4ec3315d> in <module>
      3 warnings.resetwarnings()
      4 warnings.simplefilter('error')
----> 5 test_avg()

<... skipping several frames ...>

/opt/anaconda3/envs/testing/lib/python3.7/site-packages/numpy/core/_methods.py in _sum(a, axis, dtype, out, keepdims, initial, where)
     36 def _sum(a, axis=None, dtype=None, out=None, keepdims=False,
     37          initial=_NoValue, where=True):
---> 38     return umr_sum(a, axis, dtype, out, keepdims, initial, where)
     39 
     40 def _prod(a, axis=None, dtype=None, out=None, keepdims=False,

RuntimeWarning: overflow encountered in reduce
```

```python
%debug
```

```
> /opt/anaconda3/envs/testing/lib/python3.7/site-packages/numpy/core/_methods.py(38)_sum()
     36 def _sum(a, axis=None, dtype=None, out=None, keepdims=False,
     37          initial=_NoValue, where=True):
---> 38     return umr_sum(a, axis, dtype, out, keepdims, initial, where)
     39 
     40 def _prod(a, axis=None, dtype=None, out=None, keepdims=False,

ipdb> print(a)
[[6.28689698e+293 1.79769313e+308]]
ipdb> quit
```

The error was… in NumPy? Let's see. What happens when we ask NumPy to compute the mean of two large numbers, close to but still less than the largest representable float?

```python
np.mean(np.array([1e308, 1e308]))
```

```
---------------------------------------------------------------------------
RuntimeWarning                            Traceback (most recent call last)
<ipython-input-44-a457465f6e81> in <module>
----> 1 np.mean(np.array([1e308, 1e308]))

<__array_function__ internals> in mean(*args, **kwargs)

/opt/anaconda3/envs/testing/lib/python3.7/site-packages/numpy/core/fromnumeric.py in mean(a, axis, dtype, out, keepdims)
   3333 
   3334     return _methods._mean(a, axis=axis, dtype=dtype,
-> 3335                           out=out, **kwargs)
   3336 
   3337 

/opt/anaconda3/envs/testing/lib/python3.7/site-packages/numpy/core/_methods.py in _mean(a, axis, dtype, out, keepdims)
    149             is_float16_result = True
    150 
--> 151     ret = umr_sum(arr, axis, dtype, out, keepdims)
    152     if isinstance(ret, mu.ndarray):
    153         ret = um.true_divide(

RuntimeWarning: overflow encountered in reduce

```

Ooops. NumPy's `mean()` will apparently take the sum of the elements before dividing by their number---which can overflow. So now we understand where that `RuntimeWarning` came from---but why did the test pass then? Turns out that our own function _also_ overflows.

Well, we have coded ourselves into a corner here. NumPy's `mean()` cannot be used as an oracle, because it can overflow. You _can_ tell NumPy to keep intermediate results in `np.longdouble`, which maps to your compiler's `long double`, but there's no guarantee that this will be larger that `double`.

Obviously we cannot use oracle-based testing for this one; instead we'd have to come up with some property to test against. For example, we could test that the average is equidistant from `a` and `b`. But I've spent many nights, trying to make this work, without success. Hypothesis was _always_ able to find a test case that fails. Programming with floating-point numbers sucks.

I'm going to stop this example here; the point was to demonstrate how to test functions that operate on Pandas `Series` and `DataFrame`s, not to find a correct function to calculate the average of two floating-point numbers, which is [devilishly difficult to do anyway](https://hal.inria.fr/hal-01174892/document). I'll just admit I suck at this.

## Final word

In this piece we've used the Hypothesis library to test scientific functions, either by comparing the output to a reference implementation (an oracle) or by testing that the output satisfies known properties.

Along the way, we've learned that:

- the domain of any function (the range of valid input) must always be given careful thought
- floating-point numbers include infinities and `nan`
- even simple operations (like taking the mean of two numbers) can be uncannily hard to specify correctly

We've also seen how difficult it can be to write (and test) a function that works with any valid input. Your application may guarantee that the inputs won't ever exceed certain boundaries and it's perfectly fine to limit testing to those values, as we did with the trigonometric functions---as long as you remain aware of the limitations of your test.
