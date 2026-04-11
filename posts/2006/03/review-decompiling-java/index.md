---
title: "Review: Decompiling Java"
date: 2006-03-13
categories: 
  - "book-reviews"
---

I just finished reading through [Decompiling Java](http://www.amazon.com/gp/product/1590592654?ie=UTF8&tag=compandsmarbu-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=1590592654) by Godfrey Nolan. You might ask, why would I mention a book on reverse-engineering bytecode in a weblog dedicated to smart buildings? What is the relationship between the intellectual property of companies writing Java code and home automation? The answer, essentially, is [OSGi](http://www.osgi.org/ "OSGi alliance").

An OSGi framework, in a nutshell, is a Java program for managing and running other Java programs. When you start it you get a shell prompt that allows you to download, install, start, stop, upgrade and remove other Java programs delivered as _bundles_, i.e. compressed sets of files.

Since recent years it has become economically possible to have embedded controllers that run on stripped-down versions of Linux with specially designed Java Virtual Machines (JVM). In other words, it has become possible to run Java on these constrained targets. And Java is a good language for writing home automation systems. Indeed, according to Peter Kriens, the author of OSGi's official weblog, OSGi was initially [designed in 1998 for the home automation market](http://www.osgi.org/blog/2006/01/cool-osgi-panel.html "Cool OSGi Panel").

I work together with Adhoco AG, whose flagship product is a home control system running an OSGi framework on an embedded controller. The author of the JVM we use has pointed out to us the relative ease with which compiled code can be decompiled, which is why I picked up this book after seeing it being reviewed in the ACM Computing Reviews.

Most of the book is about the process of decompilation itself, i.e. extracting the maximum amount of information from a compiled bytecode. While technically interesting, the meat of the book was in chapter 4, "Protecting Your Source: Strategies for Defeating Decompilers".

That chapter will, I think, be the most interesting one for businesses and it is neatly summarized in a table at the end of the chapter. Protection strategies range from naive obfuscation (cheap to do, but provides weak protection) to the use of native methods for sensitive parts of the code (best protection in my opinion, but breaks portability).

I would not recommend the purchase of this book if all your business wanted to do was to protect yourself against decompilation. After all, about 90% of the book is concerned with the writing of a Java decompiler. You might be best served by borrowing this book from a library and reading chapter 4 instead. But if you want to know the internal workings of a Java classfile, then I am not sure where I would find a book with as much information as this one.
