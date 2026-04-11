---
title: "Wordpress shortcode for syntax highlighting"
date: 2009-02-20
categories: 
  - "tools"
tags: 
  - "plug-in"
  - "source-code"
  - "wordpress"
---

There's a nice feature in Wordpress for including source code in your blog posts, but the Codex is not crystal-clear on how to activate it.

According to [this article](http://support.wordpress.com/code/), for example, all you have to do is to insert a \[sourcecode\] shortcode tag and anything that goes inside that tag will be automatically formatted.

But when I tried that on some Java code that I [recently posted](/smartbuildings/a-unit-test-that-could-not-fail-but-did/), it did not work. Only after some long work did I understand that in order to enable this nice feature you must install either the [SyntaxHighlighter](http://wordpress.org/extend/plugins/syntaxhighlighter/) or the [SyntaxHighlighter Plus](http://wordpress.org/extend/plugins/syntaxhighlighter-plus/) plugin. They both provide this shortcode, but SyntaxHighlighter Plus seems more advanced. That's the one I installed, and now it works perfectly:

\[code='xml'\] that is now nicely formatted and highlighted! \[/code\]

[![Reblog this post \[with Zemanta\]](images/reblog_e.png)](http://reblog.zemanta.com/zemified/e82288ac-d1f1-4c21-a8c9-142aec7a49d5/ "Zemified by Zemanta")
