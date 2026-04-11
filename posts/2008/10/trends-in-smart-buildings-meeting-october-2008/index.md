---
title: "Trends in Smart Buildings Meeting, October 2008"
date: 2008-10-15
categories: 
  - "research"
  - "trends"
---

After a two-month hiatus, we resumed our monthly meetings at LESO-PB to discuss recent developments in building automation and simulation. Frédéric Haldi, David Daum and yours truly attended. We had a smaller group this time, but that turned out to be a good opportunity for going into more detail about some of the research that's currently being done at LESO-PB.

[![20081006\_2217](images/2942639574_443a37e9bb.jpg)](http://www.flickr.com/photos/13583850@N00/2942639574/ "20081006_2217 by david.lindelof, on Flickr")

I had not been on [Adhoco's](http://www.adhoco.com) website for a while and I was recently surprised to see that their range of products had greatly increased in the past months. My opinion is of course completely biased, having contributed some source code to their main product, but I still wanted to mention it.

There was a [paper](http://dx.doi.org/10.1016/j.buildenv.2007.12.003) recently in Building and Environment describing how the simulation program [IDA](http://www.equa.se/eng.se.html) had been coupled to a Genetic Algorithm optimization program in order to derive optimal parameters for a family house. Building parameter optimization is, of course, a key area of research for LESO-PB, but during my time there I've always felt they were a bit weak on the simulation end. So it will be very interesting to see if some of the current research tries to remedy this situation.

[![20081006\_2218](images/2919358721_5049afde24.jpg)](http://www.flickr.com/photos/13583850@N00/2919358721/ "20081006_2218 by david.lindelof, on Flickr")

David Daum pointed out (quite rightly, in my humble opinion) that there are few if any universally accepted guidelines on how the assessment of a building control algorithm should be carried out. All too often, researchers bury their readers under tons of equations and models and conclude by quoting a single number, such as "Our super-duper algorithm yielded 20% energy savings compared with the ultra-realistic user model that keeps all the heating turned on throughout the year in southern Greece." We seldom see the assumptions being thoroughly documented, or how the energy demand evolves over time. Does the algorithm help equally well in summer and in winter? If not, why not?

Speaking of new developments at LESO, I don't know any details, but I've heard that they now have a N-cluster of PCs (for a largish N), dedicated to running building simulations. Oh, how I wish I had another PhD to do...

[![20081006\_2219](images/2920205052_bb4f72e610.jpg)](http://www.flickr.com/photos/13583850@N00/2920205052/ "20081006_2219 by david.lindelof, on Flickr")

Much of the meeting was spent discussing Fred's current research on window opening/closing by the building occupants. Perhaps some background is in order here. For the past five years or so LESO-PB has carried out research on modeling the behaviour of building occupants, in order to have more realistic models than the current ones. Jessen Page did his PhD [thesis](http://library.epfl.ch/theses/?nr=3900) mostly on modeling the occupancy patterns, and Fred is working on modeling the way people interact with their environment, by opening/closing windows, using appliances, etc.

Fred explained to us that after analyzing the data that had been recorded on the LESO building for the past 7 years he concludes that the majority of window events happen immediately after the user enters the room or immediately before they leave it. And the event probability for these two kinds of events is correlated with the indoor temperature.

For intermediate events, that is, window openings/closings that happen while the user remains in the room, he found that the probability per unit of time correlates well with outdoor temperatures. The problem he's now trying to solve is the exact relationship between outdoor temperature and window event probability.

We spent some time discussing this relationship, but until more browsers support MathML I won't go into much detail.

That's about all I remember from this evening. I've setup a mailing list for out meetings, [smarrtbuildings-trends](https://lists.sourceforge.net/lists/listinfo/smartbuildings-trends), and anyone interested is welcome to join us.
