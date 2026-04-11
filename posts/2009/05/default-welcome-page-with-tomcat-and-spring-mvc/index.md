---
title: "Default welcome page with Tomcat and Spring MVC"
date: 2009-05-29
categories: 
  - "programming"
tags: 
  - "apache-tomcat"
  - "java"
  - "spring-framework"
  - "toastmasters-international"
  - "web-application"
---

In my professional development, I felt that I had always neglected the field of web aplication development. To correct this I've started a little side project with [Spring MVC](http://www.springsource.org "Spring Framework"), a web application to help a Toastmasters club's Vice-President Education with their duties.

Between the official documentation and the Spring in Action book, I found the documentation on Spring MVC more than satisfactory.

I wanted my webapp to display a default, welcome page. And just for extra points, I wanted to use the [Velocity](http://velocity.apache.org "Apache Velocity") framework instead of the default [Java Server Pages](http://en.wikipedia.org/wiki/JavaServer_Pages "JavaServer Pages").

So I defined my web.xml file thus:

\[code='xml'\] [Toastmasters International](http://www.toastmasters.org/ "Toastmasters International") - Education Assistant

tmi-education org.springframework.web.servlet.DispatcherServlet 1

tmi-education \*.htm

home.htm

\[/code\]

And the Spring configuration file looks like the following:

\[code='xml'\]

/home.htm

\[/code\]

With this setup, any URL whose filename ends with .htm should be mapped to a .vm velocity template, looked up from the WEB-INF/velocity directory. In particular, /home.htm is served based on the home.vm template.

And yet, when I point the browser to the root URL http://localhost:8080/tmi-education, I don't see the default page. All I get is a 404 error message. Even more surprisingly, http://localhost:8080/tmi-education/home.htm works perfectly.

So why wasn't [Tomcat](http://tomcat.apache.org "Apache Tomcat") serving up the right welcome page? After much fiddling, and based on examples from [this blog post](http://www.enavigo.com/2008/05/23/setting-up-spring-mvc-welcome-page-without-rewrites-or-redirection/), I finally found that you **must** include the following snippet in your web.xml file (at least under Apache Tomcat/6.0.18):

\[code='xml'\] tmi-education /home.htm \[/code\]

With this in place, the default welcome page works right.
