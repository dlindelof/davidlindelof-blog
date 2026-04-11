---
title: "5 Java logging frameworks for building automation software"
date: 2009-07-23
categories: 
  - "programming"
tags: 
  - "java"
  - "java-virtual-machine"
  - "programming"
---

Back in 2005, when I was writing Java software for an embedded [home automation](http://en.wikipedia.org/wiki/Home_automation "Home automation") controller, we ran into a little unforeseen problem. The embedded virtual machine we were using implemented only the Java 1.3 API, and so did not offer any logging facilities (which only Java 1.4 started having).

We ended up using the logging implementation from the [GNU Classpath](http://www.gnu.org/software/classpath/) project, but choosing a good logging framework in future projects will make a crucial difference for embedded applications that will run for months, if not years, unattended.

Here I recap the most popular [Java logging frameworks](http://en.wikipedia.org/wiki/Java_logging_framework "Java logging framework") of the day, and their relevance to the field of building automation.

[Java Logging API](http://java.sun.com/javase/6/docs/technotes/guides/logging/)

The default logging framework, a default implementation of which comes with the JRE. Expect this to be available on any platform that implements at least Java 1.4. A good, default choice for many applications, but very limited in its functionalities. Probably the best choice when memory and/or disk space is a critical issue.

[Log4j](http://logging.apache.org/log4j "Log4j")

Arguably the most popular logging framework for Java, with equivalent implementations for many other languages. Extremely flexible and easy to configure. If your application runs on a "real" machine then you would be wise to choose this framework, or the more recent Logback (see below). If you run on an embedded platform, the choice will be more difficult and require careful thought. You can also use [Chainsaw](http://logging.apache.org/chainsaw/index.html), a graphical tool for parsing Log4j logfiles if they are formatted in XML, which should probably never be done on an embedded system. The development of Log4j seems, however, to be stuck on version 1.2.

[Logback](http://logback.qos.ch/)

Intended as the successor of Log4j, and written by the same author. I don't have much experience with it but it's probably a smart move to get to know it.

[Jakarta Commons Logging](http://commons.apache.org/logging/)

Not a logging framework per se, but a logging framework wrapper. Certain kinds of applications, such as libraries, should avoid any tight coupling with any particular logging framework and instead use a framework wrapper such as JCL. There will, however, be a (small) memory penalty, which should be evaluated if the application runs on an embedded platform.

[SLF4J](http://slf4j.org/)

The author of Logback and Log4j wrote also the Simple Logging Facade for Java, another logging framework wrapper that solves [several issues and problems with JCL](http://www.qos.ch/logging/classloader.jsp). I cannot see how a building automation application could be concerned with these kinds of classloading problems, but I like the idea of statically binding the wrapper with the logging framework, something which JCL did not do. Also, it sort of lazily evaluates the log strings, so you avoid the little performance hit when debugging is turned off (an important factor for embedded systems). You should probably prefer this wrapper over JCL, especially if Logback takes off and eventually replaces Log4j.
