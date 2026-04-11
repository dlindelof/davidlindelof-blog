---
title: "How to test an oracle"
draft: true
---

Self-taught programming scientists face a double problem: they are usually unaware of modern techniques such as test-driven development; and the program they write are often impossible to unit-test.

The typical case is the machine-learning class of programs: a module that is given a set of training data, and is then asked to infer useful information about future data. This kind of system is often impossible to unit-test because:

- Training the module takes far too long and requires reading data from files or a database, and
- Nobody know what the right answer should be.

Here at Neurobat we have developed a class of model-predictive controllers, that includes a self-learning thermal model of the building under control. Given regularly sampled sensor data, this model makes predictions about the indoor temperatures for the next 24 hours. How on earth do you develop this system with traditional TDD?

In general, you can't, nor should you. There are simply cases where TDD doesn't apply, get over it. In particular, the development of new algorithms has never followed TDD. If TDD was the only way to develop software, we would never have gotten past insertion sort.

In our case, we had two big advantages.

### Use a reference implementation

It so happened that we had at our disposal a reference implementation of some elements of our algorithm, written in another language. Furthermore we had every reason to believe that this reference implementation was correct.

We generated a large amount of sample training data, fed it to the reference implementation, and captured its output in text files. When we later implemented the same algorithm in C, we could replay this sample training data and compare thee

* * *

The R Programming Language includes `all.equal` methods, meant to test two objects for "near" equality. The `all.equal.numeric` method, for example, test whether two numeric vectors differ by the following method (from the documentation):

> Numerical comparisons for scale = NULL (the default) are typically on relative difference scale unless the target values are close to zero: First, the mean absolute difference of the two numerical vectors is computed. If this is smaller than tolerance or not finite, absolute differences are used, otherwise relative differences scaled by the mean absolute target value. (Note that these comparisons are computed only for those vector elements where target is not NA and differs from current.)

You might think this method was added to the language as a convenience to the programmer. Not so. Here is what John M. Chambers says about it:

> We created the `all.equal` methods originally to test software for statistical models, when it was installed in a new computing environment or after changes to the software itself. The tests compared current results to those obtained earlier, not "exact" but asserted to be correct implementations, run in an environment where the needed numerical libraries also worked correctly for these computations.

In other words, the original creators of the R/S system faced the same problem that we face today: how to test numerical software. Their best answer was to "assert" that a certain reference implementation, on a reference platform, provided the correct answers. He goes on:

> Testing numerical results is an important and difficult part of using statistical software. Providing numerical tests is an equally important and difficult part of creating software. Most of the difficulty is intrinsic: It is often harder to test whether a substantial numerical computation has succeeded (or even to define clearly what "succeeded" means) than it is to carry out the computation itself.

I love the _even to define clearly what "succeeded" means_ part.
