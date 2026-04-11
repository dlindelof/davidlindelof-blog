---
title: "Probability's not fair"
date: 2020-08-10
categories: 
  - "maths"
---

I'm currently reviewing a book for a well-known tech publisher, in which the author discusses the assignment of probabilities to each face of a die, when the faces are not of equal size. In the absence of more information, he claims that this is impossible.

I beg to differ.

What follows will depend a lot on how you define a probability. As an aspiring Bayesian, I accept probabilities as reflecting our degree of belief in a particular outcome. Consequently, following [Jaynes's convention](https://www.cambridge.org/gb/academic/subjects/physics/theoretical-physics-and-mathematical-physics/probability-theory-logic-science), all probabilities should be understood as being conditional on the sum of all your prior knowledge. In other words, an event $A$ cannot have a "naked" probability $\\Pr(A)$; it can only have a conditional probability $\\Pr(A\\mid I)$, where $I$ stands for all your prior knowledge and beliefs.

So back to that die. Let's first consider a similar, but simpler problem:

> You're given a coin, and told that the coin is loaded, but you're not told which way. What is the probability of tossing heads?

Let's define the amount of loading $\\rho$ as the fraction of heads that will result as the number of tosses approaches infinity. We know that $0\\leq\\rho\\leq 1$ and that $\\rho \\neq 0.5$.

<figure>

![](images/2Q==)

<figcaption>

_What follows works even for this coin._

</figcaption>

</figure>

We may even have in mind a prior distribution for $\\rho$; perhaps we suspect that most loaded coins have $\\rho$ close to $0.5$ to avoid detection. But we won't need that information, provided we accept that the coin is equally likely to be loaded either way. That is to say, our prior probability distribution function for $\\rho$ satisfies $p(\\rho) = p(1-\\rho)$.

Then the probability of heads can be found from $\\Pr(\\text{Heads} \\mid \\rho, I) = \\rho$ and from exploiting the symmetry of the problem:

\\begin{align\*}  
\\Pr(\\text{Heads}\\mid I) &= \\int\_0^1 \\Pr(\\text{Heads} \\mid \\rho, I) p(\\rho) \\mathrm{d}\\rho \\\\  
&= \\int\_0^1 \\rho p(\\rho) \\mathrm{d}\\rho \\\\  
&= \\left.\\left\[\\int\_0^1 \\rho p(\\rho) \\mathrm{d}\\rho + \\int\_0^1 \\rho p(\\rho) \\mathrm{d}\\rho\\right\] \\middle/ 2 \\right. \\\\  
&= \\left.\\left\[\\int\_0^1 \\rho p(\\rho) \\mathrm{d}\\rho + \\int\_0^1 \\rho p(1 - \\rho) \\mathrm{d}\\rho\\right\] \\middle/ 2 \\right.\\\\  
&= \\left.\\left\[\\int\_0^1 \\rho p(\\rho) \\mathrm{d}\\rho + \\int\_0^1 (1 - \\rho) p(\\rho) \\mathrm{d}\\rho\\right\] \\middle/ 2 \\right. \\\\  
&= 1 / 2 \\\\  
\\end{align\*}

Of course, we could also have simply noted that by symmetry, $\\Pr(\\text{Heads} \\mid I) = \\Pr(\\text{Tails} \\mid I)$. And since $\\Pr(\\text{Heads} \\mid I) + \\Pr(\\text{Tails} \\mid I) = 1$, we get again that $\\Pr(\\text{Heads} \\mid I) = 1 / 2$.

This is the correct answer: the only probability one can assign to a toss of heads from a loaded coin, without more information, is $1/2$, even when we _know_ that in the long run, the number of heads will not be half the total number of tosses. It's perhaps counterintuitive but remember than in the Bayesian context a probability does not have the same interpretation as in a frequentist setting. So by a similar reasoning, the probability of any face of a die coming up when we don't know whether the die is fair is $1/6$.
