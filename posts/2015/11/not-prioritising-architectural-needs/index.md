---
title: "Not prioritising architectural needs"
date: 2015-11-23
categories: 
  - "agile"
---

From Mike Cohn's [User Stories Applied](http://amzn.com/0321205685), there was this little paragraph that I think many teams (including my own) tend to forget about:

> **Developer Responsibilities**
> 
> You are responsible for providing information (sometimes including your underlying assumptions and possible alternatives) to the customer in order to help her prioritize the stories.
> 
> You are responsible for resisting the urge to prioritize infrastructural or architectural needs higher than they should be.

Indeed, on a team with technically strong members you will sometimes see proposals for stories such as:

> **Define our services's API**
> 
> As a developer, I want a clear and stable API so that I can develop the client-side code more effectively.

This story has all the virtues of a well-written user story: a clear title, a clear stakeholder, yet left intentionally vague to make sure that people will speak among themselves about it. Yet something is wrong here.

The problem is that the story brings value neither to the business nor to the users. It is part of a larger story; it is a task, or a TODO item, masquerading as a user story. It is a (no doubt well-intentioned) attempt at breaking down a larger story into small ones. But it doesn't work.

It doesn't work because once it is done, you are worse off than when you began. How is this possible? It's possible because you now own software that is neither finished nor potentially shippable. It is by definition unfinished work, and chances are that the mass of unfinished work will only grow over time. Unfinished work is like inventory: it is waste and it costs money.

Instead, it is your responsibility to gently nudge the team towards what's sometimes known as a [Walking Skeleton](http://alistair.cockburn.us/Walking+skeleton), i.e. a system that implements a small functionality end-to-end. Try hard to achieve this, and be prepared against any objections the team may have. The benefits are immense, and experience has shown that the resulting system will be better designed and easier to test.
