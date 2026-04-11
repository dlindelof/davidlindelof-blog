---
title: "The law of total probability applied to a conditional probability"
date: 2023-03-08
---

Dear future self,

I've just lost (again) about half an hour of my life trying to find a vaguely remembered formula that generalizes the law of total probability to the case of conditional probabilities. Here it is. You're welcome.

<figure>

![](images/conditional_risk.png)

<figcaption>

_So what is the probability of dying from a lighting strike if you're an American who knows this statistic?_

</figcaption>

</figure>

The law of total probability says that if you can decompose the set of possible events into disjoint subsets (say $B$ and $\\overline{B}$), then (with obvious generalization to more than two subsets):

$$\\Pr(A) = \\Pr(A \\mid B) \\Pr(B) + \\Pr(A \\mid \\overline{B}) \\Pr(\\overline{B})$$

But what if you're dealing with $\\Pr(A \\mid C)$ instead of just $\\Pr(A)$? What's the formula for the law of total probability in that case? What you're searching for can be found by googling for "total law probability conditional":

$$\\Pr(A \\mid C) = \\Pr(A \\mid B, C) \\Pr(B \\mid C) + \\Pr(A \\mid \\overline{B}, C) \\Pr(\\overline{B} \\mid C) $$

There's a great derivation here: [https://math.stackexchange.com/questions/2377816/applying-law-of-total-probability-to-conditional-probability](https://math.stackexchange.com/questions/2377816/applying-law-of-total-probability-to-conditional-probability).
