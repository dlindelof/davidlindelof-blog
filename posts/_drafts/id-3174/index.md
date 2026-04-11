---
title: "Is NR production-ready?"
draft: true
---

I hate to say so, but I have some serious misgivings about using the Numerical Recipes In X algorithms in production code.

Consider the implementation of the Nelder-Mead algorithm given in that book. Let's define a function in the two-dimensional plane:

f(x, y) = x^2 + y^2

Now let's try to find its minimum. The NM algorithm requires that you provide N+1 starting points, where N is the dimension of the function's domain. Let's try with:
