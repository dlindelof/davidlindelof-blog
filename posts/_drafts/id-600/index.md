---
title: "The non-halting Nelder-Mead algorithm (Floating-point woes, part 2)"
draft: true
---

You use the so-called Nelder-Mead algorithm when you have a reasonably well-behaved function of N (floating-point) variables that you want to minimize. It is my go-to algorithm, I have used it on my doctoral thesis and we use variants of it for certain simple optimization problems.

Naturally, being a huge fan of the Numerical Recipes series of books, I've always turned to their implementation of Nelder-Mead, which is probably as efficient as you can get:
