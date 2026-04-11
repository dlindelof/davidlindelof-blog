---
title: "Trends in Smart Buildings Meeting, August 2008"
date: 2008-08-15
categories: 
  - "home-automation"
  - "research"
  - "trends"
---

Four people again attended this second meeting, the purpose of which is to share information among people interested in home and building automation. [As previously](http://www.visnet.ch/smartbuildings/trends-in-smart-buildings-meeting-july-2008/), here are photos of the group's collective memory along with my comments.

[![20080804\_1837](images/2749021743_cca65ab246.jpg)](http://www.flickr.com/photos/13583850@N00/2749021743/ "20080804_1837 by david.lindelof, on Flickr")

Fred told us first about a conference he had attended, organized and hosted by the [Demontfort University](http://www.dmu.ac.uk/) in Leicester, England. The main subject of the conference was mainly user comfort, but according to Fred there's a certain Cooper (or Copper, sorry if I got this wrong) who's doing fairly detailed CFD simulations coupled with state-of-the-art thermal comfort models.

Friedrich, who joined us for the first time, told us about his research. He's working on the non-visual aspects of indoor lighting, and on the important topic of **spectral control** on indoor lighting. I.e., he's investigating whether "cold" fluorescent lights could have an impact on people's feeling of well-being.

LESO has obviously been busy while I was away, as I learned that their sky scanner was being used again. It's a highly reflective spherical mirror, laid flat on LESO's roof, and a digital camera takes pictures of it from above. The mirror reflects the whole sky vault, so a computer that analyzes these pictures can then measure the sky luminance distribution. The sky can then be classified according to the standard CIE skies. (One ambition of LESO is to construct a catalog of representative skies for Lausanne, such as already exist for certain major cities.)

Friedrich is also using a head-mounted illuminance sensor that's sensitive to the spectral quality of its incoming light. With this device, as I understood it, you can measure over a full day the quality of the eye-level light a person receives.

Very exciting work, I must say. I'm looking forward to seeing published papers.

[![20080804\_1838](images/2749856836_f22cf77347.jpg)](http://www.flickr.com/photos/13583850@N00/2749856836/ "20080804_1838 by david.lindelof, on Flickr")

The (non-invasive) automatic data acquisition on an inhabited building has always been a strong point of LESO. I've been myself somewhat involved in that effort, and one of my great regrets was not having had the time to work on a **canonical data format** for data recorded on a building. I personally believe there's a need for this, because it is at the moment impossible for separate research groups to share their data without a major translation effort. It would have benefits for industry too, in the same way that [a standard XML format for business](http://www.oasis-open.org/committees/ubl/) activities helps the integration of legacy systems.

Someone raised a very interesting question at this point, the gist of which was "What's wrong with Excel files?". I have [ranted against the use of Excel in academia before](http://www.visnet.ch/smartbuildings/tools-that-anyone-can-use/), but to these arguments I would add the following.

Scientific data in our field is almost always structured (i.e., not tree-like nor with arbitrary fields for each data item). So how you store your data boils essentially down to a flat file, a relational database (RDB), or a proprietary program (Excel being the obvious example, but Matlab or Igor Pro are others).

I dislike proprietary program being used in scientific work on the principle that any such work must be repeatable and verifiable. This is by definition impossible with a proprietary program whose source code nobody can inspect, and whose license costs might be a barrier.

Flat files or RDB are my own, humble, personal preference, with a slight bias towards RDBs for any long-running measurement campaign that can yield thousands or millions (as for LESO) datapoints. Flat files are the format of choice for analysis, since they can be freely shared among co-workers and colleagues and even published along with their peer-reviewed article.

[![20080804\_1839](images/2749857020_0bd07e8ed8.jpg)](http://www.flickr.com/photos/13583850@N00/2749857020/ "20080804_1839 by david.lindelof, on Flickr")

Finally we talked about SUNtool, a simulation package to which LESO has contributed in the past but which has been plagued with difficulties. It appears that one commercial partner of that project has withdrawn its support, preventing the other partners from using their code. One ambition of LESO is now to start more-or-less from scratch and to develop a more open version of that tool.

That concluded our meeting, the next installment of which is tentatively scheduled for Moday September 1st.
