---
title: "Statistically significant energy savings: how many buildings are enough?"
date: 2013-12-09
---

From [Neurobat's website](http://neurobat.net/home/) it is now possible to download a [brochure with the 2012-2013 test results](http://neurobat.net/neurobat/downloads/dokumentationen/). It summarises the findings we published at the [CISBAT 2013 conference](http://cisbat.epfl.ch/), describing the energy savings that we have achieved on four experimental test sites. Of these four, one is an administrative office. Another included the (domestic) hot water in its energy metering. Therefore, only two of them are single-family houses whose energy savings concern the space heating alone. The energy savings we measured on these two sites are 23% and 35%.

It is natural to ask oneself what the average energy savings on a typical house might be. It's possible to give an estimate, provided that we make several assumptions. We're going to assume that the energy savings that Neurobat can achieve on a single-family house in Switzerland is a random variable drawn from a normal distribution. Therefore, our best estimates for the mean and standard deviation of that parent distribution are:

$$\\mu = \\frac{23 + 35}{2} = 29$$

and

$$s = \\sqrt{\\frac{(23-29)^2 + (35-29)^2}{1}} = 8.49$$

The sample mean estimated from n samples of a normal parent distribution is distributed according to a [t-distribution](http://mathworld.wolfram.com/Studentst-Distribution.html) with $n-1$ degrees of freedom. The 95% confidence interval for the true (parent) mean can therefore be found by looking up the 0.975 and 0.025 quantiles of the t-distribution with $n-1$ degrees of freedom. In our case, $n = 2$ and the 95% confidence interval of the true mean is therefore:

$$\\left\[\\mu - t\_{n-1, 0.975} \\frac{s}{\\sqrt{n}}, \\mu + t\_{n-1, 0.975} \\frac{s}{\\sqrt{n}}\\right\] = \\left\[ -47, 105 \\right\],$$

where $\\mu = 29$, $s$ is the sample standard deviation calculated above and $n = 2$. Not the most helpful estimate ever.

We are currently repeating the experiment for this 2013-2014 heating season. A natural question that has come up is "How many buildings do we need to have a usable confidence interval for the average energy savings?"

As always, reformulating the question in precise terms is half of the battle. We want a narrow confidence interval around the mean energy savings. We can make it as narrow as we want by increasing n, or by relaxing our confidence requirement. Suppose then that we want a 95% confidence interval not wider than 10%; i.e., we want to state that Neurobat achieves $X\\pm5\\%$ energy savings with 95% confidence.

By a bit of arithmetic, what we are looking for is the number $n$ such that

$$n \\ge 4t^2\_{n-1, 0.975}\\frac{s^2}{w^2},$$

where $s$ is our sample standard deviation and $w$ is the desired width of our confidence interval. There is no closed-form solution for this equation (except for large $n$, where the t-distribution can be approximated with a normal distribution), so finding $n$ is an iterative process. In R, the right-hand side of this formula can be computed with:

\[code\] 4 \* qt(.975,n-1)^2 \* s^2 / w^2 \[/code\]

Evaluate this expression with increasing values of n until is becomes smaller than n.

Assuming that $s = 8.49$ as above, we obtain:

$$n = 14.$$

And that's it. Again, assuming that the energy savings are drawn from a normal distribution whose parent standard deviation is about 8.49, we will need experimental results on 14 buildings to give a 95% confidence interval not larger than 10% on the expected energy savings. For $n = 10$, the width of the confidence interval increases to 12% and for $n = 5$, it is 21%.

The next time you hear someone claim suspiciously precise energy savings with their miracle device, you have my permission to ask them what their confidence interval is, how they calculated it, and what underlying assumptions they are making.
