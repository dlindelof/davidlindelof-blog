---
title: "I'm a programmer, just not a real one"
draft: true
---

Programming is obviously part of the day-to-day routing of scientists and engineers today. Yet most technologists I have worked with tend to view the computer with dread, and will write computer code only when they have to, and only in a very linear, script-like fashion that models the way they think.

I will argue that technologists have much benefits to draw from a formal, yet minimal introduction to the practice of programming. I will attempt to dispel some common misconceptions I've heard about programming from this population. Some of these remarks come from my experience in teaching programming to freshmen at EPFL. Others are from former colleagues with which I have been working while doing my doctoral thesis.

\*\* Programming is for computer scientists only

The word programming is naturally most associated with the academic field of study called computer science. Students who are interested in programming go study computer science. Those who are interested in mathematics major in mathematics. Those in physics, in physics. A common cliché among teachers at EPFL was that the further away you wanted to be from computer science (or mathematics for the matter), the closer you wanted to be to architecture.

However, students in all fields of engineering are expected to carry out practical work, which invariably involves collecting and analyzing data. It doesn't really matter how this analysis is carried out. The instant you enter a formula in a cell in a spreadsheet, you have defined a function---codified a computation, which is by definition programming.

Let me restate that: the very moment you ask a computer to carry out some operation over a set of data, you have become a programmer. Whether you want it or not.

\*\* Programming takes years to learn

I am both sad and glad that few students are aware of Peter Norvig's classic "[Teach Yourself Programming in 10 Years](http://norvig.com/21-days.html)". Sad, because I wish more students would understand that whatever they learn in class will never replace the learning experience gained from deliberate (or deliberative) practice. Students believe that a college degree is a free ticket for a dream job ranging from a technical job to a project management position.

I know this because this is exactly what I believed too, until I discovered that a degree in physics for analyzing X-Ray emissions from a quasar was not something prospective employers were necessarily looking for. That didn't leave me very much in terms of career opportunities, especially not in 2000 when the dot-com bubble had just burst. So I did what all graduate students do when they can't find a job: I pursued a doctoral degree.

It was during that time working on my thesis, that I grew to learn and love programming. I am today a reasonably good programmer, and I can trace the roots of my "serious" programming back to those days at CERN. I am still far from what I would consider a programming genius, and that's in spite of me having spent more than 10 years now programming, perhaps not every single day, but probably 2-3 days each week.

Becoming an expert at programming takes, time, much as it does for anything else in life. But I'm not suggesting you become an expert programmer. Remember, this book is not for programmers, but for non-programmers. To you I say that it does not take years to learn just enough programming to be able to do it well enough, so the computer becomes your tool and not your source of frustration.

\*\* You cannot program on Windows

When I did my diploma work at EPFL, I was assigned to the Geneva Observatory. That name a little bit of a misnomer nowadays, as the telescope they have there is seldom used except for amateurs coming to use it. Most of the professional astronomical work today is done in daylight, in front of computers.

My experience with computers up to then had been, with the exception of a few lab works done with Excel, an internship at ABB working with a scientific analysis package called Igor Pro (http://www.wavemetrics.com/). I had fallen in love with that piece of software, but that was way before I discovered alternatives such as R. Anyway, back in the observatory I was forced to sit down in front of a UNIX terminal day in and day out, and I quickly learned to hate it. Having to type in commands through the prompt seemed, to me, such a backwards step in time. And I had no computer on which I could install my copy of Igor Pro.

I was, in short, still convinced at that early time that I would be more productive in a Windows environment, but with hindsight I realize that this was only due to my affection for Igor Pro. I once asked my diploma advisor why the h\*\*k they had chosen UNIX workstations instead of more "modern" ones such as Windows. He just shrugged away the question, arguing that this the choice they'd made.

With time, however, I gradually discovered Linux. First as a dual-boot Slackware distribution on the laptop I was given when I worked at CERN. Then when I worked at EPFL, it was Windows that was more the secondary operating system I'd use. Then, when I began work at Optaros in 2007, I first installed Windows but immediately also installed Ubuntu. And a year later, I reformatted the whole disc and installed a pure Ubuntu distribution. Whenever I needed Windows I would to that through a virtual machine.

Sounds like I'm arguing as strongly as possible against the possiblity of using Windows for serious work, doesn't it. Well in a sense yes, but come to think of it I think I did most of my work at EPFL on a Windows machine. Oh wait no, I remember now. We had a tower PC there, on which I was running Windows, mainly in order to have MATLAB installed. The "serious" work I did on my laptop, where I wrote the R code and the thesis itself in LaTeX. Nevertheless, for a long time I had been using a combination of Emacs, MikTeX and Cygwin under Windows. So although clearly not as convenient as working under a native UNIX system, it's perfectly possible to use programming tools and techniques under Windows.

\*\* I have never programmed in my life

Doesn't mean a thing.

When I was working for the coffeeshop, we once staged a rebellion against management and demanded the right to interview ourselves the candidates that consulting companies would send our way to work with us. One of the assignments is the world-famous "FizzBuzz" programming puzzle (http://www.codinghorror.com/blog/2007/02/why-cant-programmers-program.html).

I recently met again one of my former colleagues and asked him how the interviews generally went. Like, what percentage of candidates passed the FizzBuzz question.

About 20%, he said.

That's right. 80% of supposedly professional programmers were unable to pass this most trivial of programming assignments. And it was expected of them to work on mission-critical, enterprise integration systems. These are supposed to be the cream of the crop, remember. People with a solid programming experience. What a joke.

In contrast, the FizzBuzz example is one that I give to my students, usually about halfway through the semester. The next day I usually ask for a show of hands, asking who managed to do the exercice. I usually get about 90% of positive answers. And these are mostly students who have never programmed in their lives before, who are then outdoing the so-called professional experts.

If they can get to speed, then certainly so can you.

\*\* Quick programming jobs need no special skills

This is probably the most pernicious of all these myths, because it is the easiest one to believe. It goes something like this: I, a scientist/engineer, need a quick little programming script/function to do X. Since this a one-off job I don't need to be particularly careful about it, and since it's a short program I'm pretty sure it's going to be right when I write it first.

When I was working on my doctoral thesis I had inherited several such "short scripts" that had, over time, accumulated more and more code and who were now monsters of complexity, hard to read and even harder to modify. Some of these had to be simply thrown away. It was easier to start over again than to attempt to keep them. Why did they evolve that way? Because the original author thought that:

- I don't need to version control my programs
- I don't need to keep test programs around
- I will always be around to modify these scripts if needed
- I will never give these programs to anyone else.

I'm not saying that those programs didn't work. In fact, I don't think anyone can make that claim, not even the original author because there were no test programs available to make that assertion, or to contradict it. The correctness of these programs, on some of whose foundations entire thesis had been written, had slowly devolved into the category of unprovable statements.

In this book I'm not going to make you into professional programmers, but I'm going to give you the necessary tools to write code that's better than 99% of the scientific/engineering code that's out there.

\*\* Data analysis is not programming

However, life would be so much easier if it were. I'm not entirely sure what is meant here by "data analysis". However, one thing I'm sure of: my life can be roughly divided in two halves. In the first half, I thought that data analysis was something one did before writing a report or an article. In the second half, I realized that writing the article or the report is something one did at the same time as the data analysis was being made. Or more accurately, the code reponsible for doing the data analysis would be written at the same time as the report/article.

We're going to explore in more detail the important topic of literate programming later in this book, but to whet your appetite let me tell you that my entire doctoral thesis, by the end of my time at EPFL, was a series of text files (one for each chapter), each of which contained executable code reponsible for doing the data analysis and producing the plots that then went into the final document. My report had become my analysis. My analysis had becore my report. My code was my report.

\*\* No one will ever ask me for my code

There is an unfortunate tendency for modern scientific journals not to question the analysis results submitted to them. I hope eventually to revert that tendency, and I have always posted my analysis code publicly when I submitted a journal article. Granted, I haven't published a lot (three peer-reviewed articles so far), but for each article the analysis code is publicly available and can be examined. I'm not always particularly proud of the code I wrote, but at least it is available for scrutiny.

I hope for the sake of your professional development that you will be lucky enough to work in an enviroment where your code will be asked of you, if only for helpful review. Avoid working at places where no-one shows any interest in your programs. Avoid thesis supervisors who will not see you more than once a month, and only for face-to-face meetings. Demand (for you are entitled to it) that your work be reviewed by your peers, all of it, including the supporting code.

Maybe no-one will ever ask you for your code. Then it's up to you to change things.

\*\* Programming can be delegated

When I worked at EPFL our laboratory had its own staff of IT people, who were mainly responsible for managing the IT infrastructure of the lab (the PCs and servers), but who could also be called upon for certain programming gigs. For example, my predecessor ran an experiment which included having a window pop-up on everybody's screen about twice a day asking how they felt in terms of visual and thermal comfort. He didn't write the code for that application himself; he asked the IT staff to do it for him. And that probably made perfect sense, as it involved programming languages, techniques and tools that he didn't know about.

However, that kind of programming is, in my experience, the exception rather than the norm. In any reasonably sane environment, you will be expected to write your own programs, and to be personally responsible for their quality. No-one, in particular, will be available to write your data analysis code or to plot your own graphs. And if your work involves writing prototype code, then that's exactly what you will have to do yourself; no way any IT staff could, or should, be expected to do that kind of work for you.

\*\* I'm not a programmer if I only use office productivity tools

If you have ever written a Word macro, then you have been programming.

If you have ever started a cell with "=" then you have been programming.

If you have ever defined or used a style, you have been programming.

In fact, if you have ever used your "productivity" tool the way it was supposed to, then you have been programming. Programming is the formalization of intuitions we have about processes, nothing more. The instant you tell a machine or a human how to do anything, you've been programming.

Still, nit-picking aside, can the use of office productivity tools be considered programming? If you have ever found yourself changing by hand the formatting of a certain header level, instead of using styles, then you have done yourself a disservice by not employing your programming instincts. In fact, any repetitive, boring, silly-sounding task you have heroically undertaken yourself could probably, and probably should, have been programmed.

\*\* You have to know a lot of programming languages to be any good

I won't deny that over the years I've picked up a number of programming languages. I'm not sure whether that has made me a good programmer, but it certainly has made me a better one. Or let me qualify that. Learning different programming paradigms, rather than different programming languages, has certainly helped my programming. But again, whether this has made me a good programmer is open to discussion.

You obviously have to start somewhere when beginning to learn a new set of skills. And you can certainly become an excellent programmer even if you truly master only one or two languages. You might need to learn more programming languages if you ever plan on transcending the field, but the scope of this book is for non-professional programmers, right? People who need to know enough programming to get by in their daily, mostly scientific/engineering work. And for these folk I claim that knowing even just one programming language well can make a world of difference.

In fact, by the end of this book you may know more programming languages than you think. Some tools that we will discuss work on text files written in their own syntax, some of which come very close to (sometimes declarative) programming languages. Consider Makefiles, for instance. Or LaTeX source files. Would you consider the TeX syntax as a programming language? If not, what do you suppose LaTeX packages are programmed in?
