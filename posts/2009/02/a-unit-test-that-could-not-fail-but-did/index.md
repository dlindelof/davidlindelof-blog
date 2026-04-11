---
title: "A unit test that Could. Not. Fail. (but did)"
date: 2009-02-17
categories: 
  - "programming"
tags: 
  - "daylight-saving-time"
  - "java"
  - "unit-testing"
---

I am now convinced that even the most trivial pieces of code must be unit-tested.

Recently I've been working on a Java implementation of a building thermal model. A textbook model with thermal nodes and thermal capacities and conductances between them. This is supposed to eventually become part of a generic testing harness for home and building control algorithms. If you're interested feel free to visit the project's [homepage](http://smartbuildings.sourceforge.net/heartbreak/).

I needed to implement thermal nodes whose temperature was given by an external schedule, e.g. read from a database of climactic data. Before I jumped in, I wanted to write a simplified node implementation whose temperature could be a simple function of time.

So I wrote a node implementation whose temperature would be a sinewave, oscillating between 20 degrees at noon and -20 degress at midnight. I defined a `FunctionOfTime` interface and implemented it with a `SineWave` class, the gist of which is shown here:

\[code='java'\] public class SineWave implements FunctionOfTime { private final long phase; private final double omega; private final double amplitude; private final double offset;

public SineWave(double amplitude, double omega, long phase, double offset) { this.amplitude = amplitude; this.phase = phase; this.omega = omega; this.offset = offset; }

public double getAt(Calendar time) { return offset + amplitude \* Math.sin((time.getTimeInMillis() - phase) \* 2 \* Math.PI / omega); } } \[/code\]

This code was extremely straightforward, but I had some time on my hands and wrote anyway a [unit test](http://en.wikipedia.org/wiki/Unit_testing "Unit testing") for it:

\[code='java'\] public class TestSineWave extends TestCase { private SineWave sineWave; private Calendar calendar = Calendar.getInstance();

protected void setUp() throws Exception { calendar.set(2009, 0, 1, 6, 0); sineWave = new SineWave(20, 24\*3600\*1000, calendar.getTimeInMillis());//-20 at midnight, 0 at 6am, 20 at noon }

public void testGetAt() { Calendar calendar = Calendar.getInstance(); calendar.set(2009, 4, 23, 12, 0); assertEquals(20, sineWave.getAt(calendar), 1e-5); } } \[/code\]

You see what this is doing? The sinewave function will oscillate between -20 and 20 degrees with a period of exactly one day, 86400000 miliseconds. Its phase is defined so that on January 1st 2009 at 6am the temperature is 0 degrees. Therefore, on any day, you expect the temperature at noon to be 20 degrees.

Now when I ran it I got this:

\[code='text'\] Tests run: 1, Failures: 1, Errors: 0, Skipped: 0, Time elapsed: 0.025 sec testGetAt(ch.visnet.heartbreak.TestSineWave) Time elapsed: 0.004 sec junit.framework.AssertionFailedError: expected:<20.0> but was:<19.318516902217773> at junit.framework.Assert.fail(Assert.java:47) at junit.framework.Assert.failNotEquals(Assert.java:282) at junit.framework.Assert.assertEquals(Assert.java:101) at junit.framework.Assert.assertEquals(Assert.java:108) at ch.visnet.heartbreak.TestSineWave.testGetAt(TestSineWave.java:23) \[/code\]

I expected 20 degrees but got 19.3. It just did not make any sense. The rounding error hypothesis was easily ruled out: you just don't make 3% rounding errors with modern implementations of the sine function. I tried with other days of the year, and always got the same result, 19.3 degrees.

The discrepancy being relatively small I was at this point very tempted just to ignore the thing, and to subconsciously blame it on some peculiarity inherent to Java's Calendar implementations. I think I even entertained the thought that some days might have more seconds than others.

Come to think of it, this was actually not so far off the mark as it sounds. Are there days that do not have exactly 86400 seconds? The answer came instantenously when I tested for days in February: the answer came out right, 20 degrees.

Silly me. [Daylight Saving Time](http://en.wikipedia.org/wiki/Daylight_saving_time "Daylight saving time"). Of course.
