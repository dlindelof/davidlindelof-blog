---
title: "Trends in Smart Buildings Meeting, July 2008"
date: 2008-07-11
categories: 
  - "home-automation"
  - "research"
  - "trends"
---

On 4 July 2008 we held at LESO-PB the first of (hopefully) a series of meetings for people interested in home/building automation. The idea is to give people of widely different backgrounds a venue, time and opportunity to share, discuss and explore new ideas.

It was my pleasure to facilitate this meeting and although I did not hold any minutes, you can find here pictures of the notes I took during the meeting.

*The original Flickr photos of the meeting notes are no longer available.*

We started with introductions. It was great to have people from industry, academia and just plain hobbyists (like yours truly) interested in this subject. One thing we agreed on quite early was to discriminate between _building_ automation (BA) and _home_ automation (HA). BA will typically use completely different hardware and control algorithms than HA, so when a distinction needs to be made we agreed that HA is a subset of BA.

We started the discussion with two questions. 1) What is the state of BA today and 2) What is the role of building simulation in BA.

David started by telling us about the preliminary research he's been doing for his PhD work at EPFL. He's looking for building simulation software that would be modular enough to easily allow testing of different algorithms. This problem was similar to one I'd been working on during my own PhD so we talked a bit about the software I had used, SIMBAD, and in particular how it had been extended with Java/RMI to allow remote processes to connect to it.

One thing that Antoine stressed was the importance of building simulations for BA designers. The nature of the problem makes it impossible to run tests of control algorithms on real, occupied buildings and to get feedback in a timely manner. And the results would need to be compared to some base case anyway.

We talked a lot about the academic efforts in building simulation, especially the need for a good model of the users' behaviour. The fact is that modern simulation packages do not have a good user model, and it is very difficult to estimate the errors being made on energy demand predictions.

On the other hand, it was very unclear whether such user models could be directly used by BA systems to anticipate user actions. Users usually act after some discomfort threshold has been exceeded, but any BA system should try to act before.

We briefly reviewed the user behaviour models that LESO had been working on for the past years, most notably Jessen's occupancy model (the subject of his PhD thesis) and Fred's window opening model.

Someone mentioned a research group in Zurich. I'm not 100% positive about this but I think this could be the group of Prof. Morari, with whom I had had a brief email exchange a couple of years ago.

Antoine stressed again the importance of reliability in BA systems. The reliability issue brought up a discussion on centralized vs distributed control systems.

We were shortly running out of time, so I asked the audience their recommendations for academic or trade publications of interest to BA. We concluded the meeting by regretting the lack of real innovation in BA, both academic and industrial, and observed that the big challenge facing building simulation today was the modelling of human factors and the urban environment.

Thanks to everyone who participated, and see you next time!
