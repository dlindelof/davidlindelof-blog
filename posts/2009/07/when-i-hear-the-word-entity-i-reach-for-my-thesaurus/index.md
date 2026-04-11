---
title: "When I hear the word \"Entity\" I reach for my thesaurus"
date: 2009-07-14
categories: 
  - "programming"
tags: 
  - "business-to-business"
  - "business-to-consumer"
  - "domain-driven-design"
  - "entity"
  - "eric-evans"
  - "market-segment"
---

According to [Eric Evans](http://en.wikipedia.org/wiki/Eric_Evans "Eric Evans"), the author of _[Domain-Driven Design](http://en.wikipedia.org/wiki/Domain-driven_design "Domain-driven design"): Tackling Complexity in the Heart of Software_, one of your first goals as domain analyst is to define what he calls an _Ubiquitous Language_, i.e., a common vocabulary that your technical team and your business sponsor will agree on, and will use to communicate. Having such a common vocabulary will prevent misunderstandings and will probably help you name things in your program, such as class and method names.

<iframe src="http://rcm.amazon.com/e/cm?lt1=_blank&amp;bc1=FFFFFF&amp;IS2=1&amp;npa=1&amp;bg1=FFFFFF&amp;fc1=000000&amp;lc1=0000FF&amp;t=compandsmarbu-20&amp;o=1&amp;p=8&amp;l=as1&amp;m=amazon&amp;f=ifr&amp;md=10FE9736YVPPT7A0FBG2&amp;asins=0321125215" style="width: 120px; height: 240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" align="right"></iframe>

But what do you do when the business people seem unsure themselves of how to define certain concepts in their own domain? How do you even detect such situations?

I've found that certain words, when they begin to show up too often in conversations between the technical team and the business people, are good indicators that something needs to be clarified. Words such as _object_, _element_, _perform_, or _do_. But one word in particular seems to be particularly difficult to clarify once it has become accepted by business people: _entity_.

I was working on a business application that involved, well, _entities_ that sold widgets in the world on behalf of a certain company. I asked the business people to help me understand what an entity was, or what exactly their responsibilities were.

So is, for instance, an entity associated with a country? Well no, because entity 33 is responsible for more than one country. Ok, so is an entity responsible for a geographic zone, including one or more countries? Well no, because see here, entity 12 handles all the sales in country Foo but only [B2B](http://en.wikipedia.org/wiki/Business-to-business "Business-to-business") sales in country Bar. The best definition they seemed to be able to come up with was that an entity was something that sold widgets to some people. Not exactly helpful.

Then I asked them a simple question. "Could you give me a dump from your database of the names of all your entities?" Sure enough, they did. And when I read the list of entities, I saw that they all were names of companies incorporated in their respective countries. "Say", I asked, "aren't these, like, subsidiaries?"

Subsidiaries they were indeed. It turned out that the company had segmented the market in each country in B2B and [B2C](http://en.wikipedia.org/wiki/Business-to-consumer "Business-to-consumer") products, and the company's history explained why a given subsidiary got a given [market segment](http://en.wikipedia.org/wiki/Market_segment "Market segment") in a given country, even in another country than its own.

This realization led to an immediate simplification of our class diagrams, and a lot of class renaming. But the resulting code is now much, much clearer, something even the business people admit.

It almost always pays off to work on redefining vague or incomplete terms. It will help you as a developer, and it might well help your customer too.
