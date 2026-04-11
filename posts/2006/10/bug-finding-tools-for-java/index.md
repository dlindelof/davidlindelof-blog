---
title: "Bug finding tools for Java"
date: 2006-10-30
categories: 
  - "programming"
  - "tools"
---

I came across an article in the 15th International Symposium on Software Reliability Engineering (2004) titled "[A Comparison of Bug Finding Tools for Java](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1383122 "A Comparison of Bug Finding Tools for Java")". The authors, Nick Rutar, Christian B. Almazan, and Jeffrey S. Foster, have carried out probably the first detailed comparison of the most popular automatic bug finding tools for Java.

They tested [PMD](http://pmd.sourceforge.net/ "PMD"), [FindBugs](http://findbugs.sourceforge.net/ "FindBugs"), [JLint](http://jlint.sourceforge.net/ "JLint"), [ESC/Java](http://secure.ucd.ie/products/opensource/ESCJava2/ "ESC/Java") and [Bandera](http://bandera.projects.cis.ksu.edu/ "Bandera"). They ran most of these tools on five open source projects: [Azureus](http://azureus.sourceforge.net/ "Azureus"), [Art of Illusions](http://www.artofillusion.org/ "Art of Illusions"), [Tomcat](http://tomcat.apache.org/ "Tomcat"), [JBoss](http://labs.jboss.com/portal/ "JBoss") and [Megamek](http://megamek.sourceforge.net "Megamek").

From reading their article one gets the impression that the usefulness of these tools is greatly hurt by their tendency to report false positives, i.e. warnings that really are not bugs. Neither does there seem to be a great correlation between the tools, but this might be considered a good thing: some tools are better at finding certain categories of bugs than others.

I have used FindBugs before on a small project with three developers, and its use helped us uncover hidden bugs that mights have caused us much shame. One of us, for example, was casting to float an integer division, mistakenly assuming that 1/2 would be equal to 0.5. FindBugs caught that sorts of thing.

I have the feeling that the author's choice of test data was perhaps not optimal. Popular open source projects tend to have code of excellent quality, which might be a reason for the high ratio of false positives. There simply aren't enough bugs of the kind that can be caught by automatic tools. On more typical projects, I firmly believe that regular sweeps with this kind of tools have their place.

Oh, so what's this got to do with smart buildings? Well, as I've argued [elsewhere](http://www.visnet.ch/~lindelof/smartbuildings/archives/17), the OSGi programming framework is ideally suited for programming home automation systems, and runs on Java. I therefore expect a lot of Java code to come the way of home automation in the near future, and any tools that might help in ensuring the code's quality are welcome.
