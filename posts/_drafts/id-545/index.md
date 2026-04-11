---
title: "Reshaping a timeserie with lag in R"
draft: true
---

Suppose you have a time-series of measurements, i.e. a text file with one line per measurement. Suppose for simplicity that each line is measured at regular intervals, say one hour. For instance, it might look like this:

time indoor.temp outdoor.temp 2011-02-01T15:34:00 20.4 14.5 2011-02-01T16:34:00 20.6 14.6 ...

Suppose now that you need to have, on each row, not only the current measurements but also the past N measurements. In other words, you want your data to look like:

time indoor.temp.1 indoor.temp.2 ... indoor.temp.N outdoor.temp.1 outdoor.temp.2 ... outdoor.temp.N 2011-02-01T16:34:00 20.6 20.4 ... 14.6 14.5 ...

In R, you can accomplish this by abusing the reshape function. reshape is supposed to transform a 'long' data frame (i.e., with one row per time per variable) into a 'long' data frame (i.e. with one row per time, but with as many columns as there are variables).

Here is one possible way of doing it. I'm using a loop and could not think of a better way to do it.

We'll write a function reshape.timeserie() that will transform a data frame representing a timeserie such as the one above into a 'long' data frame. Let's first write a function to test it:

...

and here is the reshape.timeserie as it emerged after passing the tests:

...

This 'long' timeserie (for lack of a better word) is very useful when you're looking at the evolution of one variable responding to changes in one or more other variables, possibly with a time lag. For such systems, where for the sake of notation let y be the response and u be the stimulus, one can often model y as

y(t) = a y(t-1) + ...

Then you see that with the help of such a dataframe you can use R's lm() function to estimate the ... coefficients:

model ...

I'm not entirely satisfied with my implementation of reshape.timeseries though, to be honest. That loop in there bothers me very much, and it is very slow for even relative modest data sets, discouraging me from automatically running the test everytime I change it. If you have a better idea, or some other insight, feel free to comment below.
