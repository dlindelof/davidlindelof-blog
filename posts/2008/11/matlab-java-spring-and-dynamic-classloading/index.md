---
title: "MATLAB, Java, Spring and dynamic classloading"
date: 2008-11-28
categories: 
  - "home-automation"
  - "programming"
---

I have sort of a love-hate relationship with MATLAB, and always had since I read its tutorial in January 2003.

On one hand it's a proprietary closed-source system, which in my book rules it out for any scientific work. My one and only encounter with a Mathworks sales representative did nothing to help my misgivings. It is virtually impossible to reproduce any scientific work done on the MATLAB platform without a licence—rendering it almost by definition **un**scientific.

Furthermore, MATLAB as a language is very low-level, and lacks constructs found in most modern languages. Object-orientation is a joke. You can't loop on anything else than vectors. There are no primitives per se apart from the matrix (a single scalar is a 1x1 matrix—come ooooon).

These gripes aside, MATLAB is remarkably useful in its own domain, namely technical computing. And the more I use Simulink, its embedded simulation tool, the more impressed I am.

A side project of mine involves a Simulink-based physical model of an office room, complete with wall and air temperatures, daylight illuminances, heating elements and power consumptions. But what's really cool on this project is that we've extended the Simulink model with Java code running on the JVM that ships with MATLAB. This code exposes through RMI the heating, lighting and blinds control in the office room to any remote process.

I've used this model quite extensively on my [PhD thesis](http://library.epfl.ch/theses/?nr=3918), and I'm now trying to make it somewhat more useful to the wider community of building control algorithm designers. To that end I have explored the possibility of basing this Java code on the [Spring](http://www.springframework.org/) framework, in particular the parts that require database queries.

Well the proof of concept I wrote worked out just fine, with the following caveats. First, forget about dynamically loading Java classes from MATLAB. Second, FORGET ABOUT DYNAMICALLY LOADING JAVA CLASSES FROM MATLAB. It just doesn't work beyond baby-style HelloWorldish applications. And it certainly will not work for any code relying heavily on the Class.forName() construct, which is vital for Spring.

I think part of the reason is that it's not the same classloader that does the dynamical loading and the static one. According to [this bug report](http://www.mathworks.com/support/solutions/data/1-1P9USG.html?solution=1-1P9USG), if your classes are on the dynamic path then you **must** use the following signature:

`java.lang.Class.forName('com.mycompany.MyClass',true,cloader)`

where cloader is the classloader that loads classes from the dynamic path. But who's going to dive in and change the Spring code for that?

So forget about dynamic classloading in MATLAB. Just edit classpath.txt to point to your jarfiles and everything will be fine. Really. I have packages the Java code using Maven's jar-with-dependencies predefined assembly descriptor, yielding a single jarfile with all my dependencies, including Spring and the MySQL connector. Just splendid.

We even have a webpage for this project, but be warned that there's not much there yet. The URL is [http://smartbuildings.sf.net/coolcontrol/](http://smartbuildings.sf.net/coolcontrol/)
