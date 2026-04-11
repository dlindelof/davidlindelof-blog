---
title: "The power of power"
draft: true
---

A frequently overlooked aspect of statistical data analysis is the one of statistical power.

The following comes from a real-world example. A building's _total heat loss coefficient K_ is the amount of energy required to maintain constant indoor temperature for each extra degree of cold. Suppose that from historic utility invoices we have estimated a building's total heat loss coefficient before retrofit to be $K\_{pre} = 6.1 \\pm 0.57$.

Now let's suppose we retrofit this building, and that the effect of the retrofit is to lower $K$ by about 20%: $K\_\\mathrm{post} \\sim 4.8$. The question is now _what is the best accuracy with which the ratio $K\_\\mathrm{post} / K\_\\mathrm{pre}$ can be estimated?_

Since we cannot do anything about the estimates from historic utility invoices, let's suppose instead that we measure the post-installation total heat loss coefficient with perfect accuracy. Assuming that the pre-installation total heat loss coefficients are drawn from a normal distribution, how is that ratio distributed? I'm too tired to calculate the closed form (if any exists), so let's simulate.
