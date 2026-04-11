---
title: "Git and Scientific Reproducibility"
date: 2011-01-24
categories: 
  - "research"
  - "tools"
tags: 
  - "git"
  - "science"
---

I firmly believe that scientists and engineers---particularly scientists, by the way---should learn about, and use, version control systems ([VCS](http://en.wikipedia.org/wiki/Revision_control)) for their work. Here is why.

I've been a user of free VCSs for a while now, beginning with my first exposure to [CVS](http://savannah.nongnu.org/projects/cvs) at CERN in 2002, through my discovery of [Subversion](http://subversion.apache.org/) during my doctoral years at EPFL, culminating in my current infatuation with [Git](http://git-scm.com/) as a front-end to Subversion. **I'm now a complete convert to that system** and could not imaging working without it. Every week I discover **new use cases** for this tool that I had not thought about before (and that I suspect the Git developers didn't, either).

This week I found such a use case for Git: **enforcing scientific reproducibility**. Let me explain. I'm currently working on prototype software written in [MATLAB](http://www.mathworks.com/) that implements some advanced algorithms for the smart, predictive control of heating in buildings. As part of that work we need to evaluate several competing algorithm designs, and try out different parameters for the algorithms.

The traditional way of doing this is, of course, to set all your parameters right in your code for the first simulation, to run it, then to set the parameters right for the second one, to run it again, and so on. **There are several problems with this approach**.

First, you need a really good naming convention for the data you are going to generate to make sure that you know exactly which parameters you set for each run. And coming up with a good naming scheme for data files is not trivial.

Second, even if your data file naming convention is good enough that you can easily reproduce the experiment, how can you be sure that the settings are exactly right? That you didn't, perhaps, tweak just that little extra configuration file just to work around that little bug in the software?

Third, **how will you reproduce those results**? Even assuming that you ran all your simulations based on a given, well-known revision number in your VCS (you do use a VCS, don't you?), you will still need to dive in the code and set those configuration parameters yourself. A tedious, error-prone process, even if you manage to keep them all to one source file.

I think a system like Git solves all these problems. Here is how I did it.

I needed to run 7 simulations with different parameters, based on a stable version of our software, say r1409 in our Subversion repository.

I'm using Git as a front-end to Subversion. I began by creating a local branch (something Git, not Subversion, will let you do):

```
$ git checkout -b simulations_based_on_r1409
```

This will create a new branch from the current HEAD. Now the idea is to make a local commit on _that local branch_ for each different set of parameters. Here is how:

1. Edit your source code so that all parameters are set right.
2. Commit the changes on your local branch:
    
    ```
    $ git ci -am "With parameter X set to Y"
    [simulations_based_on_r1409 66cea68] With parameter X set to   
    ```
    
3. Note the 7 characters (66cea68 above) next to the branch name. These are the first 7 characters of the SHA-1 hash of your entire project, as computed by Git.
4. Run your simulation. Log the results, along with the short hash.
5. Repeat the steps above for each different configuration you want to run the experiment with.

By the end of this process, you should have in your logbook a list of experimental results _along with the short hash of the entire project as it looked during that experiment._ It might, for instance, look something like this:

| Hash | Parameter X | Parameter Y | Result |
| --- | --- | --- | --- |
| 66cea68 | 23 | 42 | 1024 |
| a4f683f | etc | etc | etc |

As you can see there are at least two reasons why it's important to record the short hash:

1. It will let you go back in time and **reproduce an experiment** **exactly** as it was when you ran it first.
2. It will **force you to commit all changes before running the experiment**, which is a good thing.

I've been running a series of simulations using a variation on this process, whereby I actually run several simulations in parallel on my 8-core machine. For this to work you need to _clone_ your entire project, once per simulation. Then for each simulation you checkout the right version of your project, and run the experiment.

Quite seriously, I would **never have been able to do anything remotely like this with a centralized version control system**. The possibility to create local branches and to commit to them is a truly awesome feature of distributed version control systems such as Git. I don't suppose the Git developers had scientists and engineers in mind when they developed this system, but hey, here we are.

Are you a scientist or an engineer wishing to dramatically improve your way of working? Then run, do not walk, to read the [best book on Git there is.](http://progit.org/)
