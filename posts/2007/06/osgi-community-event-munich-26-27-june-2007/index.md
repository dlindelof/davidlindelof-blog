---
title: "OSGi Community Event, Munich 26-27 June 2007"
date: 2007-06-30
categories: 
  - "home-automation"
  - "osgi"
  - "programming"
  - "tools"
---

I have already mentioned [elsewhere](http://www.visnet.ch/smartbuildings/review-decompiling-java/) that the [OSGi](http://en.wikipedia.org/wiki/Osgi) technology is likely to play an important part in the computerization of current and future buildings. It is a very attractive programming model for building management systems, especially with respect to its software lifecycle model (stopping, updating and restarting) that does not require a reboot of the whole system---nor indeed of your own application.

In a nutshell, OSGi is an extension to the Java programming language whereby a framework program (just called the "framework") runs continuously, in which small applications packaged as "bundles" (which are nothing else but jarfiles with some extra description information in their manifest) are installed, registered, started, stopped, updated and uninstalled. Each bundle can register "services" in the framework, i.e. objects available for use to other bundles. In a carefully designed OSGi program, when a bundle is uninstalled all bundles forget everything about it, and in particular its classes are eventually unloaded---something that never ever happens in classic Java (or any other language that I know of). For this reason, OSGi has more than once been referred to as "ClassLoaders on steroids".

This being my weblog on building automation, I report here what I found to be relevant for that field in the [OSGi Community Event](http://www2.osgi.org/Conference/2007CommunityEvent) held in Munich, Germany, June 26-27 2007.

(Full disclaimer: my trip was financed by [Adhoco AG](http://www.adhoco.com), with whom I work, but I promise will be as unbiased as I can.)

![OSGi Community Event](images/648174077_5adbbf5e58_m.jpg)

### OSGi and home automation

There wasn't actually that much of a specific focus on building automation per se---only Miguel García Longaró, from Telefónica Ivestigación y Desarrollo in Spain, and Marquart Franz from Siemens showed us products for the home automation. I found Miguel's product to be particularly intriguing, as he claimed it could indifferently talk to devices on different kinds of underlying hardware (he listed EIB/KNX, Hometronic, Busing, Dinitel and X10). This is exactly what we offer with Adhoco's product too.

One discussion that always comes up when discussing home automation with potential customers (and that is very often ignored by academicians) is the cost of the system. Miguel argues that for home automation to become a reality the residential gateways must cost less than about € 100.--. Over coffee I had an interesting discussion with Fred Verstraaten from Luminis, in the Netherlands. He argued that in the future, home automation should be a feature of the modem/router boxes you get for (almost) free when you sign up for high-speed internet. Those who want home automation pay higher monthly fees and get the bigger box, and buy the sensors/actuators separately.

I find it difficult to find faults with that line of reasoning. It's in the interest of providers of home automation to guarantee a steady stream of revenue, something a subscription model can provide. And the cost barrier is, indeed, probably a major reason why home automation is not more widespread than it is today.

Home automation and industrial automation have a lot in common. Daniel Grossmann (from the Technical University of Munich) described an architecture whereby a central server manages all devices in a plant or factory, and provides OSGi bundles to client machines that need to access the data in these devices. Providing data from an arbitrary number and types of devices to client systems is a challenging problem, one that we face with home automation too. Daniel told us about the [Electronic Device Description Language](http://www.eddl.org/) (EDDL), a formal language that describes the functions and data available from any device. His server reads this information from the devices in the plant and provides the adequate OSGi bundles.

I suppose this is an approach we could try with home automation as well, but what he is doing sounds awfully similar to the Device Access service specified in the official OSGi specs. When I asked him about this, he replied that device manufacturers prefer to distribute EDDLs for intellectual property reasons, which was (apparently) why he couldn't use this service.

I must however confess being thoroughly confused by this service specification at the moment. I spent three hours on the train trying to understand it (once more) but gave up. I've started a thread about this on the Apache Felix (an open-source OSGi implementation) [mailing-list](http://www.mail-archive.com/users@felix.apache.org/).

I've often wondered whether it is better to have one central service responsible for dealing out references to the devices to client bundles, or if each device should be represented by a service. (This dilemma is faced by anyone architecting a distributed computing environment, such as network of automatic teller machines---do you have each ATM communicate with on object that represents the bank, or with thousands of smaller objects that each represent an account?) Richard Hall, author of the Apache Felix OSGi implementation, suggested that the latter model is better, as it allows client bundles to react to the "disapperance" of devices.

![OSGi technical discussions](images/648174807_0a14c9cfaf_m.jpg)

### OSGi technical discussions

BJ Hargrave gave us a quick overview of the new features in OSGi 4.1. Only two important changes for the normal OSGi user:

1) Bundles can now be transiently started/stopped. This means, e.g., that if I transiently stop a bundle but forget to restart it, and the framework restarts for some reason, then the bundle will be restarted too. In release 4.0, if a bundle was stopped, this status was persistently saved no matter what, until you remembered to start the bundle again.

2) Lazy activation: it is now possible to specify that bundles are to be activated "for real" only when a class from them is loaded for the first time. They are still marked as Active before that (as I understood it). That can be nice if you have a large number of bundles that each take quite a long time to start but whose services are not necessarily immediately required.

Then we had also BJ Hargrave and Peter Kriens, resident [OSGi evangelist](http://www.osgi.org/blog), give a duet talk on OSGi best practices. This is what I noted:

**Portable Code**

You never know against what virtual machine your code will run, so always compile your code against the minimum suitable class libraries. OSGi defines Execution Environments (EE) for that.

**Proper Imports**

Never, ever import classes from libraries without a corresponding Import-Package statement in your manifest. The exception is java.\* libraries. You should never assume the existence of library classes on your system---in particular libraries such as javax.\*. (I could trade endless horror stories about my fights with XML parsers.)

By giving the proper Import-Package statement you guarantee that your application will die early (upon resolving, in fact) if those libraries are not available.

**Minimize dependencies**

A strong value that OSGi provides is the possibility to use different implementations of the same service. It usually makes no sense (and makes your application unnecessarily complex) to require a specific implementation of a given service.

Thus, prefer the use of Import-Package over Require-Bundle. The latter binds your application irrevocably to a particular bundle (and its provider) while the latter lets you chose which bundle, that implements the service you need, you want to install.

For related reasons, do not overspecify the bundle version you require but use version ranges.

**Hide Implementation Details**

Contrary to normal Java jarfiles, OSGi allows you to select which packages in the jarfile to make publicly available (to export, in OSGi parlance). It is generally recommended to put everything the client bundle needs (i.e. service interfaces) in the exported package and to hide all the implementation in their own, unexported packages.

I've seen different styles on how to implement this. You usually end up with two packages per service (or set of services). I have seen these naming conventions (with the interface package coming always first):

```
foo.bar.service.*
foo.bar.serviceImpl.*Impl

foo.bar.*
foo.bar.impl.*

foo.bar.service.*
foo.bar.*

foo.bar.osgi.*
foo.bar.*

```

It's a matter of taste and readability. I am uncomfortable with having an interface and its implementing class with the same names (but in different packages), but on the other hand I dislike all these dangling Impls. I personally prefer the two latter examples.

An added advantage with having the "real" classes in the package with the shorter name is if your bundle is designed to be usable outside of the OSGi framework. You want people to import foo.bar.\*, not import foo.bar.impl.\*.

**Avoid ClassLoader Hierarchy Dependencies**

Dan Bandera, president of the OSGi Alliance, closed the OSGi event by saying that there must have been some really good technical talks because he did not understand any of it. I feel a bit the same with this point.

The bottom line was, don't use Class.forName(). Don't ask me why.

**Avoid Start Ordering Dependencies**

A canonical mistake I know I have been doing (now) is to fiddle with the framework's start levels to make sure that my client bundle does not start before that HttpService bundle has been started.

It is much better, safer and cleaner to use the ServiceTracker or ServiceTrackerCustomizer classes. Your bundle should start as normal and wait until the HttpService service has been registered with the framework.

**Handle Service Dynamism**

This is very related to the point above: your bundles will be all the more robust if you remember that services can come and go. Always write your bundle as if there was a chance that the services it depends on could be (even temporarily) unregistered. Again, the ServiceTracker or ServiceTrackerCustomizer make this job easy.

**WhiteBoard Pattern**

Suppose you register an object as a listener with, say, LogReaderService.addLogListener(). Now the LogReaderService holds a reference to your object and will never, ever release it unless you call removeLogListener(). But suppose your bundle gets stopped, uninstalled or updated before?

This is an example where the classic Observer design pattern encounters problems with OSGi. You cannot any longer simply pass objects as event listeners if there's any chance that these objects parent bundle can go away, with no possibility to inform the observed object.

The somewhat surprising idea is instead to have each listener register itself as a service. Then the observed object can query the service registry for all registered listeners and notify them of the event.

There a good whitepaper on this approach [here](http://osgi.org/documents/osgi_technology/whiteboard.pdf).

**Extender Model**

Suppose you have a desktop application with a help system. You'd like to give client bundles the possibility to provide content to this help system.

One possibility is to have each client bundle register their content themselves with the help system. The problem is, again, what happens if the bundles goes away and does not remove the content?

The proposed solution is to have the help system (or any other content publisher) specify the format and location of the data it expects from each bundle---and then goes and fetches the data himself from the active bundles. For instance, it could specify that all help content should follow such-and-such XML format and be given in a help.xml file under META-INF. Then any client bundle who wants to publish help information includes that data in this help.xml file, which is retrieved by the content publisher.

**Avoid OSGi Framework API coupling**

This basically says that you should always keep the number of classes that import things from org.osgi.\* to a minimum.

Personally I always try to design a bundle as if it would be used outside of OSGi. Most, if not all, of the OSGi calls can be restricted to a small number of classes (including the bundle activator). This will also make your application much easier to test and debug---you won't necessarily have a OSGi framework handy when running your unit tests.

**Return Quickly from Framework Callbacks**

Although the specs are often silent on this point, most framework callbacks are synchronous. For instance, the BundleActivator.start() methods are usually called one after the other. But this means that if your bundle's startup time is significantly long (say, more than one second) then the total startup time of your application can become unacceptable. Again, this depends on your kind of application.

But try to keep those startup times short. Less than one second is good. Use lazy activation if you can, now that it is available. Have all framework callbacks return in a timely manner. As a last resort, consider spinning a new thread off so the callback can return while you continue the "real" activation of your bundle.

**Thread Safety**

Like many other of these best practices, this one holds for any Java application and is not restricted to OSGi. This is a complex subject, with some members of the meeting nominating Brian Goetz et al's book _Java Concurrency in Practice_ as a required reading for any serious Java developer.

I am by no means a concurrency expert, but a common cause of deadlocks is when you make foreign method calls inside a synchronized block. Do not, ever, do this. You have no idea what that method you are calling might be doing---in particular, it might well try to acquire your own lock, resulting in a deadlock and a frozen application.

![OSGi evangelist in action](images/648206061_4770680940_m.jpg)

### Miscellaneous

When he wrote the original open-source Oscar implementation of the OSGi specs, Richard Hall introduced the idea of a bundle repository: a centralized place from where OSGi bundles can be downloaded, and whose contents are described in a XML format.

He gave a talk on the history of what is today called the [OSGi Bundle Repository](http://www2.osgi.org/Repository/HomePage) (OBR), the logical continuation of his original idea. This is the official OSGi bundle repository to which vendors are encouraged to contribute, but the OBR also allows one to setup a private bundle repository. Felix comes with a OBR service to communicate with such repositories.

In my line of work I have found the OBR idea very useful, and a great tool for setting up a remote management system. Such a repository can hold different versions of the same bundle, making lifecycle management easy. What makes the developer's life even easier is the availability of the [Bindex](http://www2.osgi.org/Repository/BIndex) tool from Peter Kriens to generate the repository's description XML file.

Stuart McCulloch talked about other tools for bundle developers. It was from him that I heard for the first time about the [Bnd](http://www.aqute.biz/Code/Bnd) tool to help create OSGi bundles. Like probably many others, I'm still relying on good old Ant scripts to do that, so any tool that might make it easier is welcome indeed.

Remote management was often mentioned during the event. Kai Hackbarth, from ProSyst AG, gave a talk on the challenge of managing the lifecycles of potentially millions of OSGi devices in the field, not all of which can be assumed to be connected to the internet at all times. He presented the [mPRM](http://www.prosyst.com/products/back_end_mgmt.html) software product that his company makes, a product that helps automate this daunting task.

![OSGi discussions](images/648174457_383db4bbc8_m.jpg)

### Overall impression

This was the second OSGi event I attend, the first one having been the 2005 OSGi World Congress in Paris. I personally found the Munich event somewhat less informative for my own interests, possibly due to the high percentage of business presentations. The technical presentations were, however, excellent and I managed to make more contacts than in Paris. I would have loved to see more "hands-on" presentations, showing examples of the use people make of OSGi but more into the technical aspects. But I guess that's just not possible in a two-day plenary meeting, and the organizers did a fantastic job for this community event.
