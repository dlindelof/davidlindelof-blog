---
title: "Where all floating-point values are above average"
date: 2016-04-25
---

When you just fix a programming bug quickly, you lose. You waste a previous opportunity to think and reflect on what led to this error, and to improve as a craftsman.

Some time ago, I discovered a bug. The firmware was crashing, seemingly at random. It was eventually resolved, the fix reviewed and tested, and temptation was high to just leave it at that and get on with what was next on the backlog.

This is probably how most programmers work. But it's probably wrong. Here's Douglas Crockford on the topic, [interviewed by Scott Hanselman](http://www.hanselminutes.com/396/bugs-considered-harmful-with-douglas-crockford):

> There’s a lot of Groundhog’s Day in the way that we work. One thing you can do is, every time you make a mistake, write it down. Keep a bug journal.

I wanted to give it a try. So what follows is my best recollection of how I solved the bug.

First, the observations. You cannot be a successful debugger if you are not a successful observer. My firmware wasn't _quite_ crashing at random. It would crash and reboot 18 times in very quick succession (less than a few minutes) following a firmware update. Once this tantrum was over it would behave normally again.

It was a new firmware version. The same firmware had been deployed on other devices, but without the same problem. So why should it happen on some devices but not all of them?

There are some useful heuristics to keep in mind when debugging. I've said it before, but if you don't observe carefully and keep notes, you're just not a good debugger. I've found the following heuristics useful when debugging:

1. What changed between this release and the previous one?
2. What is different between this environment and another where the failure doesn't occur?
3. Carefully go through whatever logfiles you may have. Document anything you notice.
4. How often does the failure happen? Any discernible pattern?

In this case, the software changes introduced by this release were relatively minor and I judged it unlikely that those changes were the cause of the problem. If they were, I would expect to see the same problem on all devices.

Now when I say that something is "unlikely", I mean of course that there must be something else that is more likely to be the real explanation. Nothing is ever unlikely by itself, and if you can remove feelings from your day-to-day work you'll be a better engineer. But more on this in another post.

I next examined the logfiles, and noticed that the _first_ recorded crash was not a crash. It was the normal system reboot when a new firmware was installed. The _second_ crash was not a crash either. It was a factory reset of the system, performed by the person who updated the system to the new firmware. It's an operation that can only be done manually, and the only crashing device was the one that had been factory-reset right after the firmware update.

So someone had logged into that device and factory-reset the system. Going through the `/var/log/auth` logfiles I could determine who had done it. When confronted, he confirmed that he had reset the system in order to try an improved version of our heating schedule detection algorithm.

Now there's nothing wrong with that; but it's well-known that bugs are more likely in the largest, most recently changed modules. The module doing heating schedule detection was relatively large, complex, and recently changed.

Now experience had shown that only two events could cause the firmware to crash and reboot:

- a watchdog reset;
- a failed assertion.

(A watchdog is a countdown timer that will reboot the system after a given timeout, typically of the order of the second. You're supposed to manually reset the timer at regular intervals throughout your application. It's meant to prevent the system from being stuck in infinite loops.)

At this point I went through the implementation of that algorithm very carefully, keeping an eye on anything that could be an infinite loop or a failed assertion. When I was done, I was fairly confident (i.e. could almost prove) that it would always terminate. But I also came across a section of code whose gist was the following:

```
float child[24]; // assume child[] is filled here with some floating-point values
float sum = 0;
float avg;
for (int i = 0; i < 24; i++) 
  sum += child[i];
avg = sum / 24; // compute the average of the elements of child[]

int n_above_avg = 0; // count how many elements are greater than the average
int n_below_avg = 0; // count how many elements are less than or equal to the average
for (int i = 0; i < 24; i++)
  if (child[i] <= avg)
    n_below_avg++;
  else 
    n_above_avg++;
assert(n_below_avg > 0); // at least one element must be less than or equal to the average
```

That was the only place where an assertion was called. Could this assertion ever fail? This code calculates the average of a set of floating-point values, and counts how many elements are less than or equal to the average (`n_below_avg`), and how many are greater (`n_above_avg`). Elementary mathematics tells you that at least one element must be less than or equal to the average.

But we're dealing with floating-point variables here, where common-sense mathematics doesn't always hold. Could it be that all the values were greater than their average? I asked that [question on Stackoverflow.](http://stackoverflow.com/questions/20102906/can-a-set-of-floating-point-numbers-be-all-above-average) Several answers came quickly back: it is indeed perfectly possible for a set of floating-point numbers to all be above their average.

[![Above-Average-Children](images/Above-Average-Children.png)](https://davidlindelof.com//wp-content/uploads/2016/04/Above-Average-Children.png)

In fact, it's easy to find such a set of numbers if they are all the same. One respondent gave a list of floating-point values that, when averaged, turned out to all be greater than their average. For example:

```
#include <iostream>
#include <cassert>

using namespace std;

int main() {
  int sz = 24;
  int i;
  double values[sz];
  for (i = 0; i < sz; i++) values[i] = 0.108809;
  double avg;
  for (avg = 0, i = 0; i < sz; i++) avg += values[i];
  avg /= sz;
  assert (values[0] > avg);
  return 0;
}
```

Once the root cause of the problem was identified, it was relatively easy to write a failing unit-test and implement a solution.

Well, that's the news from the world of programming where all the floating-point values _can_ be above average. Who said [Lake Wobegon](https://en.wikipedia.org/wiki/Lake_Wobegon#Standard_monologue_items) was pure fiction?
