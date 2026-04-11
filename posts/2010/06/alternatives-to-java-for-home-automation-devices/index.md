---
title: "Alternatives to Java for home automation devices"
date: 2010-06-07
categories: 
  - "programming"
---

I think there's no escaping this simple fact: the Java Virtual Machine (JVM) is definitely here to stay, and all the evidence shows that it has tremendous potential for being used in home automation devices.

I still remember from a previous life when we hunted for a JVM implementation that would run with a minimal footprint in, if I remember correctly, a 16 MB flash drive with about the same amount of RAM. It was compliant with Java 1.3 at that time (around 2003), and I remember we were having issues with its total lack of logging libraries.

Things have changed a lot since then, but the JVM is still a superb platform for future home automation devices. It's just such an ubiquitous and comfortable environment to work with; the code you compile and unit-test on your laptop will be the same one being later executed on whatever water heating controller you're gonna use. And any platform that's more or less compliant with the official Java specs will come preloaded with plenty of libraries for your everyday needs.

Still, I'm not writing this to encourage you to learn or even perfect yourselves at Java. Java is actually a rather weak and inexpressive language. Instead, remember that JVM-the-platform is not quite the same thing as Java-the-programming-language. You compile Java code into [bytecode](http://en.wikipedia.org/wiki/Java_bytecode) that then gets executed by a JVM, but who said you needed to compile Java code? There are, indeed, [about 200 different languages](http://en.wikipedia.org/wiki/List_of_JVM_languages) that can be compiled to Java bytecode, many of which are arguably far better, more powerful, and more expressive languages than Java.

One such language is [Scala](http://www.scala-lang.org/), which I've been studying for a while now, and I'm impressed by the ease with which this language allows you to create Domain Specific Languages (DSLs), i.e. highly expressive pseudo-languages that apply to a very specialized field or domain. I would not be surprised to hear, five years from now, that about 10% of all bytecode being run in the world were in fact compiled from Scala.

If you're into writing embedded code for home automation devices, I strongly encourage you to learn at least one JVM language in addition to Java. I think you would be surprised how easier and faster it can be to write controller code in a programming language that lets you think at the right level of abstraction---which Java never let me do.
