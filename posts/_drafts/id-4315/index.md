---
title: "Slaying process dragons"
draft: true
---

It is what every junior programmer dreams of; it is what every experienced programmer dreads: being pulled from your project to rescue a project in trouble whose key contributor is on holiday.

The Fundamental Flaw of many organizations wishing to build an d deploy machine-learning applications is having software engineers report to a different management chain than the data scientists. Few managers overcome the tempration to keep both areas of expertise separate, leading to data scientists delivering perfectly fine algorithms that turn out to be difficult to deploy, understand, test, maintain, and modify.

On a recent project, the data scientist had done an excellent job at building all the components of the application---except it didn't scale. Well, no problem, right? That's the software engineer's job, isn't it?

Maybe.

Like when all you need to do is throw more cluster nodes, or JVM RAM, or bandwidth at your problem. But none of that helped. In what was possibly a panic move, they tried to port all the Pandas code to Koalas, a Pandas-mostly-compatible API that manipulates Spark dataframes instead of numpy arrays. But that only made the application crash less quickly, making it even harder to quickly hypothesize and test new ideas.

Then the data scientist left on holidays, which would have been perfectly fine if in the meantime the product team hadn't decided to bump up the priority of the project a few notches. And that's how yours truly got pulled from his own project to help with this one.

The main problem, it turns out, was with a piece of the pipeline that used a home-grown autoregressive model. Autoregressive models predict the future one timeset at a time from the past, using data from a
