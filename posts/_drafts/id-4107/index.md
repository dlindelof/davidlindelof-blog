---
title: "Patterns of Machine Learning Applications"
draft: true
---

I frequently provide a thin wrapper around the actual statistical model objects used in my machine learning code. These wrappers sometimes do little more than forward calls to `predict()`. Why go to this seemingly unnecessary trouble?

Machine learning applications frequently user statistial model provided by third-party libraries. These models can be slow, and have a less than straightforward interface. So how do you write unit tests for classes that directly depend on these models?

Wrapping actual 3rd party objects is a form of Gateway (466), and providing stubs to external services is a Service Stub (504).

Gateways should satisfy the need of the application. For example, if the application needs the probability of classification, have `predict()` return that probability and ignore the other gunk that the underlying `predict()` might return. See, for example, the return value of ranger's `predict()`.

A Record Set (508) is a list of maps, the rough equivalent of our data frame, except the latter are a map of lists.

The Dataset in the closeouts application is a collection of Table Modules (123).
