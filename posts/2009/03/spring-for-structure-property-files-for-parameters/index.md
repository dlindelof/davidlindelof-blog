---
title: "Spring for structure, property files for parameters"
date: 2009-03-13
categories: 
  - "programming"
tags: 
  - "java"
  - "programming"
  - "xml"
---

[Spring](http://www.springsource.com/) is a great framework for externalizing the [object graph](http://en.wikipedia.org/wiki/Object_graph "Object graph") of your application. Typically you write an XML config file that defines a number of Java objects (or "[beans](http://en.wikipedia.org/wiki/Bean "Bean")") and how they are supposed to relate to each others.

For example, suppose you have a class ThermalNode whose instances need to hold a reference to, say, an instance of a TimeProvider class. The way you usually do this in vanilla Java is you define this relationship somewhere close to the program's start:

\[code='java'\] ThermalNode node = new ThermalNode(); node.setTimeProvider(new TimeProvider()); \[/code\]

But in Spring you define this structure outside of your main program, and the above would be written somewhat like this:

\[code='xml'\] \[/code\]

And thus the structure of your object graph has been moved away from your compiled code.

Where this got really interesting for me was when I started introducing parameters for the thermal nodes, e.g. thermal capacicities. I would have for instance this sort of structure:

```
+---------------+
|  ThermalNode  |
|---------------|
|  capacity1    |
+---------------+
       |
       \
       /
       \ conductance
       /
       \
       |
+---------------+
|  ThermalNode  |
|---------------|
|  capacity2    |
+---------------+

```

What you then start having are beans whose properties (or constructor arguments, which is the way I prefer doing it) are not only references to other beans but also values.

Now a requirement for this project of mine is that it should be easily customizable by the end user. And that means not having the poor user coming and manually edit Spring config files.

Instead, Spring lets you define properties in plain property files, e.g.

```
# A property file
capacity1=300
capacity2=250

```

Then these properties are available to your main Spring config file through this kind of incantation:

```
<context:property-placeholder
    location="classpath:my.properties"/>
```

And your beans can then refer to these properties like this:

\[code='xml'\] \[/code\]

I have found this way particularly useful, namely **put the structural data in the Spring config file, and put the parameter data in its properties file**. Doing so not only makes it easy for the user to run the program with different parameters. It also lets you stash away the Spring config file in your application's jarfile, putting it out of the way of the user. And that, I believe, is a very good thing, because you typically do not want to confuse the user with Spring's syntax.

[![Reblog this post \[with Zemanta\]](images/reblog_e.png)](http://reblog.zemanta.com/zemified/6a020740-079d-46d3-be0c-2bc492a13737/ "Zemified by Zemanta")

<script type="text/javascript" src="http://static.zemanta.com/readside/loader.js" defer="defer"></script>
