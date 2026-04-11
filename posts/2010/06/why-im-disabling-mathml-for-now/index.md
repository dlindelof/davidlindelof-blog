---
title: "Why I'm disabling MathML for now"
date: 2010-06-02
categories: 
  - "tools"
---

In a previous post I described how I tweaked my WordPress installation to support the display of MathML markup, for displaying mathematical equations.

One of the steps involved changing the content-type from application/html to application/xhtml+xml. That step was necessary, or else Firefox would simply not render the MathML markup properly.

Unfortunately, application/xhtml+xml is simply not supported on a host of other browsers, including Internet Explorer. Which means that this blog became unreadable overnight to anyone coming to it with anything else than Firefox.

This is why I'm disabling direct MathML support on this blog. If you're interested you can view the original blog post [on my blog's old server](http://visnet.ch/smartbuildings/how-to-include-mathml-in-a-wordpress-blog).

There are, however, alternative (and arguably simpler) ways to display mathematics on the web, such as [MathJax](http://www.mathjax.org), or [jsMath](http://www.math.union.edu/~dpvc/jsMath) (a Javascipt library used on the Maths Q&A site [MathOverflow](http://mathoverflow.net)
