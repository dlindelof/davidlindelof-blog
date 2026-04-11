---
title: "MATLAB's inane idea of time"
date: 2010-06-24
categories: 
  - "programming"
tags: 
  - "matlab"
---

MATLAB seems to have a very peculiar notion on how to represent dates and times. Yesterday I spent a wonderful couple of hours debugging some code that's supposed to compute the sun's position, most of which could have been avoided if the MATLAB designers had followed a simple convention used by, I believe, most computing platforms.

In MATLAB, dates and times are represented internally by a so-called \*serial date number\*, defined as the number of time units counted since a given reference date. If you are like me you will, I suppose, assume that this reference date is the standard UNIX \*epoch\*, i.e. midnight, January 1st, 1970. Well you're only about two millenia off---the reference date in MATLAB is the hypothetical (and non-existent) date of midnight, January 1st, 0000. Never mind that there never was a year 0000---the calendar goes straight from 1 BC to 1 AD.

And if you \*really\* are like me you will of course assume that the unit of time in which this serial date number is counted is seconds, or at least milliseconds. Wrong again---MATLAB choosed \*days\* as its fundamental unit of time. And of course, Octave was forced to follow MATLAB's choice:

octave:4> format long octave:5> now ans = 734313.962094548

Besides making it much more difficult to make MATLAB interoperate with, say, Java libraries, there are several problems with this approach (documented in Octave's help file, haven't checked in MATLAB):

1\. The Julian calendar is ignored, so anything before 1582 will be wrong; 1. Leap seconds are ignored. In other words, MATLAB ignores days that happened to be 86401 seconds long (yes, there are).

When working with timeseries data, in particular climate data, I always try to count time from the UNIX epoch---ideally as the number of seconds from the epoch, the way \`date(1)\` works when called with the \`+%s\` format argument:

18:08:49@netbook$ date +%s 1277309333 18:08:53@netbook$ date +%s 1277309336

In Java, \`System.currentTimeMillis()\` will return the number of milliseconds since the epoch:

scala> System.currentTimeMillis res0: Long = 1277395240485

In R, converting a \`DateTime\` object to numeric yields the number of seconds:

\> as.numeric(Sys.time()) \[1\] 1277310008

In short, every computing platform I've touched in the recent weeks represents time starting from the standard UNIX/POSIX epoch, and always do so in a unit related to seconds. In other words, there is no justification for MATLAB's decision to represent time since year 0000, and even less for doing so in number of days. I don't mean to bash MATLAB (well... a bit, maybe). I just regret that anytime I need MATLAB to interoperate with some other code, I need to include a factor of 86400 and shift everything by 1970 years.
