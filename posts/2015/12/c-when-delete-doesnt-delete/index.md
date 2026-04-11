---
title: "C++: when delete doesn't delete"
date: 2015-12-21
---

We once spent almost a week chasing after a mysterious memory leak in our application, built on top of the highly regarded [eCos real-time operating system](http://ecos.sourceware.org/). The leak appeared after we had rewritten some of our code in C++ after recognising that C's object-oriented capabilities were no longer adequate for our needs.

After about half a day we could reproduce the memory leak on the target system with code that essentially looked like this:

```
Controller* controller = new Controller();
delete controller;
```

What baffled us most was that running this code in unit tests on the development machines exposed no such memory leak. We routinely run all our unit tests under Valgrind to identify memory usage errors, but in this case there was none. It was very unlikely that the leak was caused by defective code.

What's more, the leak was almost-but-not-quite consistent. We leaked about 952 bytes on average, but that figure could be as low as 920 or as high as 968. It was always a multiple of 8 bytes. After about 8.5 hours, the system would reboot, presumably because it ran out of memory. We used the `mallinfo()` function to display the amount of available memory.

After almost a week we found the answer. According to the [documentation](http://www.ecoscentric.com/ecospro/doc/html/ref/memalloc-standard-api.html), the default implementation of the `delete` operator in eCos is a no-op! I suppose the rationale is that most developers of embedded systems tend to shy away from dynamic memory allocation, and that it is better to reduce the size of the firmware by not providing a (rarely-needed) `delete` operator.

Except when we need one, of course.

To enable a proper `delete` operator you simply disable the `CYGFUN_INFRA_EMPTY_DELETE_FUNCTIONS` option in your eCos configuration file.
