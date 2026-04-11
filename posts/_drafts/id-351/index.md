---
title: "When is a window not a window?"
categories: 
  - "general"
draft: true
---

Buildings are messy. Very messy. I'm sitting here in an open-space office with about 20 tables, a high ceiling, and at the far end of the space there are two private spaces enclosed by light walls with windows in them, high enough to prevent anyone from seeing what happens inside.

I shudder at the thought of having to model such things in software.

That private space, at the far end of the open-space, has windows looking out to the outside and windows towards the inside. The windows towards the outside can be opened, those towards the inside cannot.

Now if you take any children and put them in that room, and ask them to open all the windows because it is too hot, it would never occur to them to even try to open the windows towards the inside. a) those windows can't be opened, b) even if they could, they can't be reached, being too high, and c) they would not help, being on the inside.

Now put an automatic controller in that room and tell it to do something about the excessive heat inside. Be sure to tell it about the windows first.

My guess is that you will have some routine in that controller trying to open all the available windows in order to get some fresh air. But how do you deal with windows that cannot/should not be opened? How do you model this sort of thing?

Or put it another way: assume your controller has a reference to all the windows in a room, stored in some collection of some sort. Let's say it wants to open all the windows that can be opened. How does it do?

One solution would be to define an OpenableWindow interface, which would extend both a Openable and a Window interface. Openable would be rather simple:

`public interface Openable { void open(); void close(); boolean isOpen(); }`

whereas Window could have some other methods proper to a window, especially its physics:

`public interface Window { double getUValue(); double getArea(); // ... }`

Now let's go back to our collection, say windows. Then to open all the windows in that collection, you would do something along the following lines:

`for (Window eachWindow : windows) { if (eachWindow instanceof Openable) ((Openable)eachWindow).open(); }`

While technically correct, this solution does not really map to the way we humble humans would tend to think about the problem. In particular, once a window has been recognized as not openable we should not try to open it again.

Think of how
