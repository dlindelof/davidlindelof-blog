---
title: "Looking up an EJB from a Web Service under JBoss 4.x"
date: 2009-08-14
categories: 
  - "programming"
tags: 
  - "ejb"
  - "jboss"
  - "jndi"
  - "web-service"
  - "webservice"
---

[EJB injection in Web Services does not work with JBoss](http://www.jboss.org/index.html?module=bb&op=viewtopic&t=154200) (yet), so when you want to use an EJB from your @WebService annotated POJO you have no choice but to look it up yourself.

This can get a little tricky, because each J2EE container can use its own JNDI naming convention when registering the EJB in the global naming context. Here I document how I configured JBoss to register my EJB with a name that I choose, and how I mapped a proper EJB name to that JNDI name.

### Naming the EJB

Give your EJB a reasonably unique name in its annotation:

@Stateless(name="MyServiceBean") @Local(SomeInterface.class) public class ServiceBean implements SomeInterface { ... }

### Tell JBoss what JNDI name to register it under

Include the following in your jboss.xml file:

MyServiceBean myapp/MyJNDIName

### Tell JBoss to map an EJB name to the JNDI name

In your WAR, configure your jboss-web.xml file to include this:

ejb/MyEJBName myapp/MyJNDIName

### Lookup the EJB from your Web Service

You can now lookup the EJB directly from your Web Service:

@WebService public class MyWebService { private SomeInterface getMyBean() { try { return (SomeInterface) new InitialContext().lookup("java:comp/env/ejb/MyEJBName"); } catch (NamingException e) { throw new EJBException(e); } } }
