---
title: "Don't set your seed"
draft: true
---

Testing scientific software is usually harder than testing conventional software, for several reasons. Frequently you don't even know what the output should be. I've written about possible solutions for that problem elsewhere. Here I want to mention another frequent issue, which is when the program depends on some random number generator.

By nature, the output of such a program will never be twice the same, and so the best strategy will always be to apply some statistical test to multiple (many) runs of your program.

You might be tempted instead to manually set the seed of your random number generator before running the program, and verify that the output remains identical to some "golden" reference run. There are several problems with this approach.

1. Not all systems garantee that the same sequence of random numbers will always be generated from the same seed. For example, the following program:

## \[source\]

# set seed

for i in 1 to 10

## printf(" … " , rand());

will produce the following on OSX

but this on Linux

and this on Windows

So your tests are not garanteed to produce the same results on different platforms, unless you build your own rng, or use a library that makes such a garantee. Boost.Random is such a library, which incidentally will probably have a much stronger RNG than the one provided by your standard library.

2. There is usually no promise either from system implementers that the random number generators will remain the same forever. For example, R version X infamously changed their RNG which caused problems for, for example, instructors who had to update all their material.
