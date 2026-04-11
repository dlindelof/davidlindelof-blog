---
title: "The RuntimeException dilemma"
categories: 
  - "general"
draft: true
---

According to Joel Spolsky (in episode 8 of the StackOverflow podcast), it's failry ok to use exceptions, as a programming construct, when writing applications. When writing system applications, though, he cautions against them:

> When you're writing systems programming, an exception is just a way to get a bug in your code you can't see. When you're writing application programming, it's a marvelously convenient and useful thing to have. But I came from a kind of a world where you're trying to write like a little bit of C code, like a page of code, that a processor can run, that will absolutely 100% work. And you really need to be constantly trying to think about every code path, and an exception is just one more thing that you may forget to think about.

Now let's assume that writing building automation software counts as system programming. I'm not sure what the right definition is anyway. Let's call system programming any programming that's dangerous enough.

Now if I may be so bold as to make an industry prediction, chances are that we will see more and more building control systems written in Java and less and less written in C. OSGi makes the programming experience simply much easier and enjoyable. And we will, I think, see a distinct split between those who program microcontrollers (mostly in C) and those who program higher-level supervisory devices, such as set-top boxes. The latter are much more likely to run Java.

Which means that future control systems written in Java will inevitably have to face exceptions. There's just no way around, once you start using Java. You can't write control systems without doing I/O operations, so you just have to be ready to handle IOExceptions.

Java exceptions (or, even more generally speaking, Java Throwables) come in several different flavors and developers who write control systems must know how to handle each of them. There are several texts out there on the topic. What follows is my personal take on it.

I throw checked exceptions when the caller can reasonably expect trouble and blame himself if the error (or exception) is badly handled. At the very least, he should be given a chance to recover. Examples are the classic checked exceptions, such as the ones thrown when I/O fails.

Unchecked exceptions, or RuntimeExceptions, should never happen. In other words, I consider a RuntimeException as a programming error, an error from which the caller can not be reasonably be expected to recover.

To take a concrete example from the field of building automation, suppose you provide an interface for switching lights on or off:

```
public interface Light {
  public void switchOn();
  public void switchOff();
}

```

Now what can possibly go wrong when I call light.switchOn()?

1. I/O errors: I might be unable to use the serial port, for unknown reasons;
2. Problems on the building automation system itself;
3. Problems with the lamp hardware itself.

Let's examine each one of them.

I/O errors: unless there's a real physical problem, the serial line should always work. When it does not, there's absolutely nothing the programmer can do. What's worse, how is the programmer expected to notice a problem? Retrying the message is unlikely to work if there's a hardware problem anyway. In such a situation I want my program to \`fail fast, fail early', to which I would also add \`fail spectacularly', i.e. throw a RuntimeException and either terminate the program or (if possible) log the error, page the operator, call the police or whatever.

Problem with the building automation system: If the building bus does not support some form of message acknowledgments, then this sort of error will never be (directly) detected and it is the caller's responsibility to ensure the command has had its desired effect (verify increased lighting levels, etc). If there are acknowledgments, then errors on the building bus can be detected but what should the caller do with them, and whom should be notified? The problem, you see, is that the caller should not have to wait for an acknowledgment to return. You don't want to put the caller's thread on hold just to wait for an acknowledgment. Commands should be sent asynchronously, therefore another thread should handle errors such as the lack of an acknowledgment. But what can this thread do besides throw an exception or log an error?

Problem with the lamp hardware: this sort of error is almost impossible to detect programatically, unless the caller checks lighting levels after sending the command.

Thus, the only kind of errors that the caller can be expected to detect (bus errors) are errors that cannot be handled asynchronously anyway.
