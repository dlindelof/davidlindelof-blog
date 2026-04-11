---
title: "Canonical data formats, middleware and GCC"
date: 2009-01-26
categories: 
  - "programming"
  - "tools"
tags: 
  - "gnu-compiler-collection"
  - "xsl-transformations"
---

These days I'm working on a middleware application that bridges a company's ERP and its warehouses. The ERP posts messages in a given XML schema, our application reads these messages, transforms them into the schema understood by the warehouse management system, and uploads onthem on the warehouse's FTP server.

We use [XSLT](http://en.wikipedia.org/wiki/Xslt) to transform messages in one schema to messages in the other. In the example above, one XSL file can handle the whole transformation.

But what happens when you deal with more than one schema on either end? Suppose you have on the ERP side one schema for orders, one schema for defining the product catalogue, and so on. And on the warehouse side you might have more than one schema for different kinds of messages.

Say you end up with N schemata on the input and M on the output side, and suppose (for the sake of argument) that your application must handle every possible combination. If you use one XSL file per transformation, that's NxM files. If the customer changes one schema on the input side, or adds one (and we have no control over that) then we must revise M files.

The classical solution to this combinatorial explosion is the [Canonical Data Model](http://enterpriseintegrationpatterns.com/CanonicalDataModel.html) messaging pattern. We have defined a common data format for our middleware application, and we transform all incoming messages to this common format before transforming them into the proper outgoing format.

<iframe src="http://rcm-de.amazon.de/e/cm?t=compandsmarbu-21&amp;o=3&amp;p=8&amp;l=as1&amp;asins=0321200683&amp;md=1M6ABJKN5YT3337HVA02&amp;fc1=000000&amp;IS2=1&amp;lt1=_blank&amp;m=amazon&amp;lc1=0000FF&amp;bc1=FFFFFF&amp;bg1=FFFFFF&amp;f=ifr" style="width: 120px; height: 240px;" marginwidth="0" marginheight="0" frameborder="0" scrolling="no"></iframe>

With this solution, whenever a schema changes or is added we only need revise ONE XSL file. Pretty neat and innovative solution, right? I thought so too. Until I listened to [this interview](http://www.se-radio.net/podcast/2007-07/episode-61-internals-gcc) about the GCC internals.

The [GCC](http://en.wikipedia.org/wiki/GNU_Compiler_Collection) can compile C, C++, Fortran, Ada, Java (and probably lots more languages) to an amazing number of platforms. How can it do this and avoid the combinatorial explosion when a language changes, or the definition of one platform changes?

<iframe src="http://rcm-de.amazon.de/e/cm?t=compandsmarbu-21&amp;o=3&amp;p=8&amp;l=as1&amp;asins=0954161793&amp;md=1M6ABJKN5YT3337HVA02&amp;fc1=000000&amp;IS2=1&amp;lt1=_blank&amp;m=amazon&amp;lc1=0000FF&amp;bc1=FFFFFF&amp;bg1=FFFFFF&amp;f=ifr" style="width: 120px; height: 240px;" marginwidth="0" marginheight="0" frameborder="0" scrolling="no"></iframe>

Simple. It uses a canonical data format. More specifically, GCC's frontend compiles the source code into an intermediate language-neutral and platform-neutral representation called [GIMPLE](http://en.wikipedia.org/wiki/GIMPLE). This representation is then translated by GCC's backend into platform-specific code. If a language is modified, only the frontend must be revised. If a platform changes, only the backend must be revised.

The GCC folks (and probably many others) had been doing Canonical Data Format for decades before this pattern became recognized as such. And I thought we were being so clever...

[![Reblog this post \[with Zemanta\]](images/reblog_e.png)](http://reblog.zemanta.com/zemified/00c90648-5a99-4dae-95b6-ea33ce549a96/ "Zemified by Zemanta")
