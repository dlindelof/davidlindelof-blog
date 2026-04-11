---
title: "Installing ESP-r on Ubuntu 9.10"
date: 2010-06-08
categories: 
  - "tools"
---

[ESP-r](http://www.esru.strath.ac.uk/Programs/ESP-r.htm), is an _integrated modelling tool for the simulation of the thermal, visual and acoustic performance of buildings and the assessment of the energy use and gaseous emissions associated with the environmental control systems and constructional materials_, in the words of its official website. In other words, it's a computer program for modeling a building's thermal and energy performance. It's especially popular in Europe, particularly among academia.

Recently I wanted to install it on my laptop running Ubuntu 9.10 (Karmic Koala). The standalone installers provided on the main downloads website didn't quite work, complaining about the lack of the libg2c library. Well of course it's not available. It's been [obsoleted and is now deprecated](https://bugs.launchpad.net/ubuntu/+source/gcc-4.4/+bug/477278).

Your best choice when installing ESP-r on Ubuntu is, quite frankly, to rebuild it from source. And it's not complicated either. Here's how I did it.

Check the project out from SVN:

`$ svn co https://espr.svn.cvsdude.com/esp-r/trunk espr   $ cd espr/src`

Ensure you have the required development libraries installed. In particular you will need libxml2-dev if you build with XML support and libX11-dev if you build the X version (which I recommend). Note that you really need the \-dev packages, these contain header files required when compiling an application against those libraries.

Choose now an installation directory. Being the only user of my machine, I installed under ~/programs/esru, but you might want to install under /opt/esru. Now you should be able to build:

`$ ./Install -d ~/programs/esru      ESP-r installation script.      Please consult the README file before commencing installation. This script will rebuild the ESP-r modules on your system. You can abort this process at any time by pressing c.      Please answer the following questions. Default answers are in []. To accept the default, press return.      Your computer identifies itself as Linux. Is this information correct (y/n)? [y]      ESP-r can be built with the Sun Fortran 90, GNU or intel compilers.   Compiler:   (1) Sun fortran 90 (cc and f90)   (2) GNU fortran (gcc 3.X and g77)   (3) Intel fortran (icc, icpc and ifort)   2      Install with experimental XML output support? This may significantly increase simulation run-time. (y/n) [n]   y   XML output enabled for bps   Graphics library: [2]   (1) GTK graphics library   (2) X11 graphics library   (3) no graphics library (text-only application)   2      ESP-r can optionally retain debugging symbols and object files for use with a debugging program such as GDB.      Retain debugging symbols? (y/n) [n]      Install ESP-r database files? (y/n) [y]      Install training files? (y/n) [y]         Proceed with installation of esp-r modules (y/n) [y]?         Installing ESP-r system. This may take some time.   ...`

Once the build is complete (took me an hour on a Asus 1005HA netbook), you should be able to run ESP-r:

`$ path/to/install/espr/bin/prj`

Enjoy!
