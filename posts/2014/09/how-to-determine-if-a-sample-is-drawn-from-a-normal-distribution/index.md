---
title: "How to determine if a sample is drawn from a normal distribution"
date: 2014-09-25
---

Suppose you've performed some experiment on a given population sample. Each experiment yields a single numeric result. You have also derived the usual statistics (say, the sample mean and the sample standard deviation). Now you want to draw inferences about the rest of the population. How do you do that?

I was surprised the other day to learn that there's an [ISO norm for that](http://www.iso.org/iso/catalogue_detail.htm?csnumber=38154). However, life gets much simpler if you can assume that the parent population is [normally distributed](http://en.wikipedia.org/wiki/Normal_distribution). There are several ways to check this assumption, and here we'll cover what I believe are two of the easiest yet most powerful ones: first an informal, graphical one; then a formal, statistical one.

The graphical method is called a (normal) [Q-Q plot](http://en.wikipedia.org/wiki/Q%E2%80%93Q_plot). If your sample is normally distributed then the points in a normal Q-Q plot will fall on a line.

Here is a vector of measurements that I've been working with recently. (Never mind what these represent. Consider them as abstract data.)

```
> x
[1] 20.539154 -1.314532 4.096133 28.578643 36.497943 12.637312 6.783382 18.195836 15.464364 20.155207

```

The command to produce a normal Q-Q plot is included in R by default:

```
> qqnorm(x)
> qqline(x, col=2)

```

Note that I also call `qqline()` in order to draw a line through the 25% and 75% quantiles. This makes it easier to spot significant departures from normality. Here is the result:

[![qqplot](images/qqplot-550x550.png)](http://computersandbuildings.com/wp-content/uploads/2014/04/qqplot.png)

No nomination for best linear fit ever, but nothing either to suggest non-normality.

Now for the statistical test. There are actually [a lot of statistical tests for non-normality](http://en.wikipedia.org/wiki/Normality_test) out there, but according to Wikipedia the [Shapiro-Wilk test](http://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test) has the highest [power](http://en.wikipedia.org/wiki/Statistical_power), i.e. the highest probability of detecting non-normality on non-normally-distributed data. (I hope I'm getting this right or my statistician friends will tan my hide.)

This test is built-in to R with the `shapiro.test()` function:

```
> shapiro.test(x)

    Shapiro-Wilk normality test
    
data: x 
W = 0.9817, p-value = 0.9736

```

You probably have a part of your brain trained to release endorphins when it sees a p-value lower than 0.05, and to trigger a small depression when the p-value is higher than 0.9. But remember what it is we are testing for here. What is the null hypothesis here?

Here, the null hypothesis is that the data is normally distributed. You might find this counter-intuitive; for years, you have been trained into thinking that the null hypothesis is the thing you usually _dont't_ want to be true. But here it is the other way around: we want to confirm that the data is normally distributed, so we apply tests that detect non-normality and therefore hope the resulting p-value will be high. Here, any p-value lower than, say, 0.05 will ruin your day.

So we have determined both graphically and numerically that there is no evidence for non-normality in our data. We can therefore state that to the best of our knowledge, there is no evidence that the data comes from anything else than a normal distribution.

(Ever noticed how much statisticians love double-negatives?)
