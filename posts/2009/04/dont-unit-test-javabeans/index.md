---
title: "Don't unit test JavaBeans"
date: 2009-04-07
categories: 
  - "programming"
tags: 
  - "javabean"
  - "soap"
  - "unit-testing"
  - "web-service"
  - "web-services-description-language"
---

Should unit tests cover JavaBeans just to get a higher [code coverage](http://en.wikipedia.org/wiki/Code_coverage "Code coverage")?

These days I am working on a payment processing application that exposes its main interface as a [SOAP](http://en.wikipedia.org/wiki/SOAP "SOAP") web service. The API requires the client to build a wrapper object that packages the information needed for processing, for instance, a credit-card debit authorization: customer name and address, credit card number and so on.

I wrote the application code-first, and let the web service stack automatically generate the [WSDL](http://en.wikipedia.org/wiki/Web_Services_Description_Language "Web Services Description Language") and other artefacts needed by the calling client software. From that WSDL and the generated XML schemas, the client can then generate the required Java supporting code to use the web service (almost) transparently.

This requires that I define those wrapper objects with a default no-args constructor, and that I define getters and setters for all its fields (the so-called [JavaBean](http://en.wikipedia.org/wiki/Javabean) convention. Personally I dislike this kind of programming for a variety of reasons, but it was forced upon me by the web service stack.

When the time came to write unit tests, I actually had more time available than I had planned for, so I thought I should try to increase my test code coverage as much as possible. That led to several refactorings that overall helped the code's testability, improved the test coverage, and probably improved the overall design.

But then I noticed that several of the wrapping objects' get/setters had not been exercised by the test code. I first thought of writing unit tests for these classes, but then I realized how stupid that would be. Come one, writing unit tests for getters and setters?

**A much better approach** is to understand why the unit tests did not cover these methods in the first place. Upon investigating I discovered that I had not written unit tests that covered certain, very special logic branches&emdash;the very ones that needed those unexercised get/setters.

I duly wrote unit tests for these special cases, and after a few more minutes like this my test code coverage reached more than 80%, or twice what it was when I started out.

Lessons learned:

- Write unit tests. Always.
- **Do not unit test JavaBeans**. Unit test the methods that use the JavaBean methods instead.
- **Monitor your test code coverage**. Tools such as [Cobertura](http://cobertura.sourceforge.net/) make this trivial.
- Improve your test code coverage through relentless refactoring. Not only will your coverage improve, but so will probably your design.

[![Reblog this post \[with Zemanta\]](images/reblog_e.png)](http://reblog.zemanta.com/zemified/9e14fa56-e2ce-4775-a783-510e7d8c5175/ "Zemified by Zemanta")

<script type="text/javascript" src="http://static.zemanta.com/readside/loader.js" defer="defer"></script>
