---
title: "Should control commands block?"
categories: 
  - "general"
draft: true
---

Suppose you wrote a script in your favorite programming language to control the lighting in your home according to some set of rules. You implement it in terms of simple abstractions, say Occupancy and Lighting objects, with simple interfaces. Through these interfaces, you send a command to the electric lighting with calls similar to:

```
lighting.setIntensity(50);
```

Depending on the reliability of the underlying building communication bus, this call might fail. How would you know? Should it block until you are sure the command was successfully sent? Is this something you would desire?

Naively, one would be tempted to say yes, for at least two reasons.

1. The underlying call can signal problems to the caller by throwing an exception.
2. Most I/O libraries that I know of block until the I/O is complete. For instance, the socket Python library has a send command that blocks until all data has been sent, explicitly set to be non-blocking. (But in this instance, 'non-blocking' does not mean the data is sent asynchronously. It only means an error is raised if the data cannot be sent immediately.)

But on the other hand, when you write a control program, chances are you do not want to deal with low-level I/O problems for at least two reasons:

1. What would you do with the problem? It's not your responsibility to deal with such low-level problems, nor would you be expected to.
2. I usually have other things to do and I want to return as quickly as possible to more interesting business, for instance computing the next set of commands to send.

Seems that there are really two questions that must be solved here:

- Should `lighting.setIntensity(50);` block?
- Should the caller of `lighting.setIntensity(50);` expect exceptions?

I think it's wrong to compare `lighting.setIntensity` to operations as low-level as socket operations. It should instead be compared to the writing to FileOutputStreams in Java. There's an underlying implementation that takes your data, signals any immediate problems, returns immediately and promises the data will eventually be... what? Written to file? No. Let's read what the Java API tells us about the flush() method:

> flushing the stream guarantees only that bytes previously written to the stream are passed to the operating system for writing; it does not guarantee that they are actually written to a physical device such as a disk drive.
