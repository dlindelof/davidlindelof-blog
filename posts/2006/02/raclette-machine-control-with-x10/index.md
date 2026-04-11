---
title: "Raclette machine control with X10"
date: 2006-02-14
categories: 
  - "home-automation"
---

This Saturday I turned on our new raclette machine at our flat from my computer.

There is a fairly well-established home automation standard in the U.S. called [X10](http://en.wikipedia.org/wiki/X10_%28industry_standard%29), invented in 1975. It allows for the simple control of appliances, lights and other home equipment, using a communication protocol over the power lines.

It has however never been much popular here in Europe, and for a time I could never find a distributor of X10 equipment compatible with our swiss eletrical outlets. There is one however; on their [website](http://www.x10europe.com/) we europeans can finally find all the necessary equipment to carry out most of the hacks described in the book ["Smart Home Hacks"](http://www.amazon.com/gp/product/0596007221).

I had our laboratory order some starter kits and elementary equipment in order to test things out. I will regularly post to this weblog updates on my tests and projects with this equipment; in the meantime, I would like to share my experience in setting up my computer to communicate with X10 from a Java program.

First I downloaded the software written by the [Java X10 Project](http://x10.homelinux.org/). This software includes useful examples to control simple appliances or lamps. However, it also needs an implementation of Sun's Comm API, necessary for communicating over the serial interface.

I have had some very bad experiences with commercial implementations of this API so this time I tried out the open source [RXTX](http://www.rxtx.org/) implementation. You need to download the source and follow the INSTALL file scrupulously for this to work, including the contrib/ChangePackage.sh script. The compilation will look like it's stuck in an endless loop but in fact it isn't. Just be patient.

Once this was done, I could run the appliance example of the Java X10 project, which displayed a window with a single On/Off button. After making sure that my raclette machine was connected to an X10 applicance module with the right house and unit addresses, I clicked "On", and heard the actuator switch on in the kitchen.

PS. If you are going to try this at home, make sure all the protective cellophane has been removed from your raclette machine first. I could switch the machine off in time to open the windows and ventilate before my wife could notice the heavy smoke. I guess no computer will ever completely prevent human errors. :-P
