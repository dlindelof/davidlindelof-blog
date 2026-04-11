---
title: "Why I (still) use C++"
date: 2019-03-11
categories: 
  - "c"
---

When I joined Neurobat in 2010, the company's vision was to develop an add-on component that would compute optimal setpoints for your heating system. Such a device had to be small, cheap, and run reasonably fast. That ruled out modern embedded PCs that nowadays can comfortably run Python; the entire application, including the "smart" model-predictive control library, had to be programmed in a language compiled to native instructions.

Most of that library was initially written in C. Soon, we realized that the design could greatly benefit from full object-orientation. So once we made sure that our toolchain supported C++ we began to port many modules to that language. (That was C++98, the most recent version of C++ our toolchain would support.)

<figure>

![](images/C-Programmers.jpg)

<figcaption>

Source: [https://www.improgrammer.net/c-programmers-humor/](https://www.improgrammer.net/c-programmers-humor/)

</figcaption>

</figure>

But around 2016, the company's strategy began to shift from single homes in favour of large, commercial buildings whose facility managers were less price-sensitive than homeowners. It had become economical to shift to more powerful devices that could run Python, or even to cloud-based platforms. There was less of an imperative to stick to C++, and some team members experimented with porting our library to Python. In the end, I was perhaps the only one in a team of six engineers who knew the library, and C++, well enough to maintain it.

And yet, I've made a concerted effort to keep my C++ skills sharp, not only before we shut down the company but also afterwards. I've read Effective Modern C++, Modern C++ Design, and I listen to every episode of both [CppCast](http://cppcast.com/) and [cpp.chat](https://itunes.apple.com/gb/podcast/cpp-chat/id1378325120?mt=2). For the first time, I used C++ instead of Python for the annual [Google Code Jam competition](https://codingcompetitions.withgoogle.com/codejam). Why do I do that? And more importantly, should you?

If you're doing _any_ kind of programming, I believe you would benefit from knowing C++, and here's why.

1. C++ has been around for 30 years, and is likely to remain highly relevant for many more years. It is probably the most popular language that gets compiled to machine instructions, as opposed to "managed" languages that are either interpreted or compiled to bytecode. And it clearly dominates that niche; I can't think of any alternative besides D, Rust, and possibly Go. C++ is probably the most expressive language that runs on bare metal, and that alone would be reason enough to learn it.
2. C++ remains the best option for writing extensions to other languages or environments. Without C/C++, the only way you can extend existing systems is by writing libraries in the same language, which will only be as performant as that language platform. For example, I'm currently predominantly working with R, and C++ is a very natural choice when writing high-performance extensions for that environment.
3. For better or for worse, C++ features almost all programming language features known to man. It's been called a multi-paradigmatic language and with good reason. It combines aspects of procedural, functional, object-oriented, and generic programming. And it is currently undergoing something of a renaissance, judging from the rate of new features being considered and released. If you're looking for some intellectual challenge, do your brain a favour and feed it some C++.

I know that C++ has gotten some bad reputation because of its complexity and syntax, but I believe that most of these criticisms are ill-founded. I know just as many programmers who sincerely claim they love C++ as who claim they love Python. The learning curve is steep, but well-worth the climb. Will you join me on the journey?
