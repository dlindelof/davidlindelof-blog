---
title: "Trends in Smart Buildings Meeting, November 2008"
date: 2008-11-25
categories: 
  - "research"
  - "trends"
tags: 
  - "add-new-tag"
  - "marc-fleury"
  - "python"
  - "stackoverflow"
---

We met again on November 3 to discuss recent events in the field of building simulation and automation. This time we were joined by [Adil Rasheed,](http://www.adilrasheed.com/blog/index.php) a PhD student at LESO-PB working on the so-called "meso scale modelling of urban heat island effect." David Daum and Antoine Guillemin were the other participants, besides yours truly.

Antoine had brought a prototype [aHeart](http://adhoco.com/products/central-unit/adhoco.h1/) central unit, the "brains" behind Adhoco's home automation solution. He described it to the other participants, most of which had never seen it before.

He told us also about some of the newer features, such as the possibility for installers to specify their own custom rules through the web interface. Although difficult to implement, this was actually something that the market demanded specifically and that Adhoco had to offer.

[![20081103\_2412](images/3015671568_b7a6beb805.jpg)](http://www.flickr.com/photos/13583850@N00/3015671568/ "20081103_2412 by david.lindelof, on Flickr")

I had previously mentioned on this blog Marc Fleury's [OpenRemote](http://www.openremote.org) project and asked the attendees if they had heard about it, but nobody had. Antoine knew about a certain Marc Fleury, working for a swiss company called [Ergo3](http://www.ergo3.ch/), makers of a home gateway device, but I'm pretty sure it's not the same person.

David gave us his update on his project and explained a bit more how the [IDA](http://www.equa.se/eng.se.html) simulation engine worked. What I found particularly compelling was the way that IDA would adapt its simulation timesteps depending on the needs. We discussed the possibilities to use IDA for simulating the performance of Java-based controllers such as Adhoco's, but we are not sure whether IDA can call Java code.

[![20081103\_2413](images/3015671656_a59b728aeb.jpg)](http://www.flickr.com/photos/13583850@N00/3015671656/ "20081103_2413 by david.lindelof, on Flickr")

Speaking of processes talking to each others, we briefly reviewed the canonical four ways that two processes can talk:

1. Through the exchange of files, whether on the same filesystem or through FTP;
2. Through a shared database;
3. Through some form of remote procedure call (RPC), such as RMI in Javaland;
4. Through a messaging solution, such as JMS.

But this review still didn't help us understand how C code could call foreign code, such as Java or Python. The reverse is relatively straightforward, see eg [this answer on StackOverflow.](http://stackoverflow.com/questions/83299/whats-the-easiest-way-to-use-c-source-code-in-a-java-application#83364)

[![20081103\_2414](images/3014835805_07ddfd1be3.jpg)](http://www.flickr.com/photos/13583850@N00/3014835805/ "20081103_2414 by david.lindelof, on Flickr")

Thanks to everyone who participated, and see you around next time.
