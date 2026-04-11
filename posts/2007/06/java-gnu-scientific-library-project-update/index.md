---
title: "Java GNU Scientific Library project update"
date: 2007-06-01
categories: 
  - "announcements"
  - "programming"
  - "tools"
---

The [GNU Scientific Library](http://www.gnu.org/software/gsl/) (GSL) is a rich state-of-the-art C library of mathematical routines. Pretty much everything you could think of---special functions, linear algebra, function optimization, fast Fourier transforms, and much, much more---is covered by this library.

I have taken over the open-source [Java GNU Scientifc Library](http://sourceforge.net/projects/jgsl) project at [SourceForge](http://sourceforge.net). The plan is to write a Java wrapper around this library and make it available for Java developers. There is, for the time being, strictly nothing to see on SourceForge---I'm still planning this whole thing.

I have done some preliminary testing and compared the speed for calculating natural logarithms. I wrote the appropriate JNI wrappers and this test class:

```
import java.util.Random;
public class LogTest {
public static void main(String argv[]) {
        System.loadLibrary("gsl_sf_log");
        double[] sample = new double[5000000];
        Random rnd = new Random();
        for (int i=0; i<sample.length; i++) {
            sample[i] = rnd.nextDouble();
        }
        double tmp;
        long tic = System.currentTimeMillis();
        for (int i=0; i<sample.length; i++) {
            tmp = Math.log(sample[i]);
        }
        long toc = System.currentTimeMillis();
        System.out.println("Built-in log: " + (toc-tic) + " ms.");
        tic = System.currentTimeMillis();
        for (int i=0; i<sample.length; i++) {
            tmp = gsl_sf_log.gsl_sf_log(sample[i]);
        }
        toc = System.currentTimeMillis();
        System.out.println("GSL log: " + (toc-tic) + " ms.");
    }
}

```

In this program I time the computation of five million randomly chosen doubles between 0 and 1, first with Java's built-int Math.log function (which I understand is based on [netlib](http://www.netlib.org/)), and then with GSL's. This is the output:

```
[lindelof@lesopriv3 jgsl_test]$ java -D -Djava.library.path=./ LogTest
Built-in log: 1327 ms.
GSL log: 1164 ms.

```

Not a big difference, except the GSL version runs slightly faster.

My idea is to cross-compile the GSL library and its Java wrappers, at least for the i386 and arm targets, and package it together with the Java classes in target-specific jarfiles.

The idea is to start work on this right after I finish writing my PhD manuscript, by the end of June at the latest. Help and contributions welcome. I will regularly post updates about this project in this column.
