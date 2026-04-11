---
title: "If your team isn't doing code katas, they should"
draft: true
---

At Neurobat we have a weekly so-called \`tech-lunch': pizza is being brought in at company's expense and we spend our lunch time learning something together. 9 times out of 10 it's going to be a video, but every once in a while we do something different. Last time I organised a coding kata session, in the randori style, using the rating poker hands kata.

In this kata, your program is given a string of characters representing two poker hands and your program must decide which is the winning hand. If your program is written in Python, called `poker.py`, then the following is an example use:

```
$ ./poker.py 5D 2C ...
Player 1 wins
```

In a randori, we take turns at the keyboard. There are always two coders. Each session lasts 5 minutes. We rotate who sits at the keyboard, and everyone spends two sessions at the keyboard. We started the session with the following piece of code:

```
def test():
    assert False

if __name__ == "__main__":
    test()
```

and built on from there.

I had done this before, so in order to not influence the initial design I made sure I would come last to the keyboard. By then the team had written some elaborate input validity checking code, but hadn't really gotten to implementing any of the real logic. I suspect there's some subtle procrastination at work here: when you are unsure how to deal with a complex problem, fall back to something you are more familiar with and call it work.

We eventually got down to doing the actual problem and decided it would make sense to break down the problem. First we wanted to rank an individual hand and wrote a failing unit test for what I thought would be the easiest hand to rank, three of a kind.

Once this was written, the team decided it was time to refactor and spent the rest of the kata extracting \`proper' classes representing the concepts from the domain. Here is the resulting code:

This is not necessarily a bad design, but I was perplexed by the team's reflexive urge to refactor towards the `Hand` and `Card` classes. If you have taken Peter Norvig's class on \`Design of Computer Programs' on Udacity (and if you haven't, you owe it to yourself to do it), then you will remember that the first lecture is about the same kind of problem but Dr Norvig gives the entire class without once using Python's class system. All the data structures he defines in his class use Python primitives: strings, lists, tuples and (sometimes) dicts. His programs consists in amazingly short functions that operate on these data structures.

A common misunderstanding among programmers is to believe that data encapsulation can only be achieved with classes, and that the main benefit of using a class system is to achieve encapsulation. This is not true. Encapsulation is achieved by the proper programming discipline. A Python module that does all its work using a (private) data structure expressed with Python primitives has achieved encapsulation; a C module doing all its work using an opaque pointer to a privately defined `struct` has achieved encapsulation. Once you understand this, you will be able to write far better programs and you'll probably see too that classes should be written only when the code tells you so, not when books do.
