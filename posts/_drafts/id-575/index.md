---
title: "Quicksort didn't come out of TDD"
draft: true
---

Test-driven development is great for driving the development of what I like to call business-facing code, i.e. code whose behavior is largely defined by the business. But there is an important class of programming problems that TDD cannot effectively address: the design of algorithms.

Suppose you are assigned the programming of a sorting routine. You are given the following prototype to implement:

void qsort(void \*base, size\_t nmemb, size\_t size, int(\*compar)(const void \*, const void \*));

Let me see you now implement an efficient sorting algorithm using TDD. Soon you should realize that the only kind of tests you can expect to write are variations of:

\- generate a random array of things - call qsort() - verify the array is sorted.

If you follow the TDD tenets religiously (i.e. build the simplest thing that could possibly work), then congratulations on your new Bogosort implementation.

I claim that TDD will not help you design algorithms. The quicksort algorithm was the fruit of careful thought and deep knowledge of efficiency issues. And I'm pretty sure that the inventor of Quicksort wrote the tests for his implementation AFTER writing it, not before.

At Neurobat we are faced with the design of novel machine-learning algorithms for the efficient control of heating space of buildings. We routinely address questions on how to best forecast local climate conditions. However, how on Earth do you test such algorithms? How indeed does one test ANY machine-learning algorithm? How do you unit test Google's search results?

The short answer is that you don't. First because unit-testing machine-learning algorithms often takes far too long to be considered a unit-test in the strict sense of the term (i.e., a test that takes less than 100ms to run). Second, because you cannot ask a machine to assess the quality of the learning, unless you can explicitly and carefully define what it means for a result to be good enough. You might for instance train the algorithm with one half of the data and try and forecast the other half, and define a metric for the quality of the forecast. But again, this computation is likely to take far too long to be considered a valid unit test.
