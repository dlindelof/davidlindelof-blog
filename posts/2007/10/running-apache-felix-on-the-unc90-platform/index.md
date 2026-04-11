---
title: "Running Apache Felix on the UNC90 platform"
date: 2007-10-10
categories: 
  - "osgi"
  - "programming"
---

We have made [Apache Felix](http://felix.apache.org) run successfully on the [UNC90](http://softgun.sourceforge.net/unc90.shtml) embedded platform and here I'd like to share our experience.

Our UNC90 runs on an ARM9 chip with 16 Mb flash and 32 Mb RAM. It runs the [uClinux](http://uclinux.org/) operating system. The flash is divided in four partitions according to the linux/drivers/mtd/maps/modarm9.c file in uClinux's source distribution:

/dev/mtdblock/1: 256 kB for the U-Boot loader /dev/mtdblock/2: 2.75 MB for the uClinux kernel /dev/mtdblock/3: ~3 MB for the root partition /dev/mtdblock/4: ~6.4 MB for user applications, mounted on /mnt

We have chosen the Mika Java Virtual Machine, made by [/k/ Embedded Java Solutions](http://k-embedded-java.com/). We install it under /usr/bin and /usr/lib respectively, and its total footprint is about 1.67 MB. It claims to be compatible with at least Java 1.3, but already includes many features from Java 1.4.

We have installed Felix on the user applications partition under /mnt/felix. The framework is then started by a script similar to this:

```
  mika \
      -Dfelix.config.properties=file:felix.config.properties \
      -Djava.protocol.handler.pkgs=com.acunia.wonka.net \
      -jar bin/felix.jar

```

We had to slightly modify the default configuration file. We force the framework to export system packages as if we were running Java 1.4:

```
org.osgi.framework.system.packages=org.osgi.framework; version=1.3.0, \
 org.osgi.service.packageadmin; version=1.2.0, \
 org.osgi.service.startlevel; version=1.0.0, \
 org.osgi.service.url; version=1.0.0, \
 ${jre-1.4}
# ${jre-${java.specification.version}}

```

The \-Djava.protocol.handler.pkgs=com.acunia.wonka.net option is necessary if you want to do anything URL-related. See [here](http://felix.apache.org/site/faq.html) for a full discussion. Basically, we must specify the name of a package containing protocol handlers, which defaults to sun.net.www.protocol. But with Mika this must be set to com.acunia.wonka.net.

We have found this setup to be more than satisfactory in terms of stability, performance and memory usage. We have uncovered several bugs in Mika's class library, but the folks at /k/ have always patched them in a timely manner.

I'd be happy to answer any further questions you may have about running Felix on the UNC90 platform.
