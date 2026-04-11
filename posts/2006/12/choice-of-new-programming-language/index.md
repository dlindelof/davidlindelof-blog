---
title: "Choice of new programming language"
date: 2006-12-04
categories: 
  - "programming"
  - "tools"
---

If you are regularly programming in your work you should invest some time to keep your programming skills sharp. And one of the best ways to do that is to master a new programming language.

I have now been through two major programming projects in Java, and am starting on a new one in Python. I am relatively new to that language but I was not too sure whether I should invest all my time into learning it. I wanted to master a new language, but was not sure which one.

Most of my programming consists in analyzing data and producing graphs and results. After some research I found five major languages that help in doing that. They are Lisp, Python, Ruby, S and Mathematica.

I then rated each language according to four criteria:

1. Power. How powerful is the language at expressing things?
2. Performance. How fast are typical implementations of the language?
3. Libraries. Are vast libraries available, built-in into the language?
4. Literate Programming. Does the language naturally support the [Literate Programming](http://www.literateprogramming.com/ "Literate Programming") style, proposed by [Donald Knuth](http://www-cs-faculty.stanford.edu/~knuth/ "Donald Knuth")?

After some research I rated each language on a scale of 1 to 4 on each criteria. My judgement had at times to be very subjective, or based on hearsay. I found the following results, summarized in the table below. In the right-most column I sum the scores of each language for each criteria.

|   | Power | Performance | Libraries | Literate Programming | TOTAL |
| --- | --- | --- | --- | --- | --- |
| Lisp | \*\*\*\* | \*\* | \*\* | \* | 9 |
| Python | \*\*\* | \*\*\*\* | \*\*\*\* | \*\* | 13 |
| Ruby | \*\*\* | \*\*\* | \*\*\* | \* | 10 |
| S | \*\*\* | \*\*\* | \*\*\* | \*\*\*\* | 13 |
| Mathematica | \*\*\*\* | \*\*\* | \*\* | \*\*\* | 12 |

All languages are about eaqually powerful, but Lisp and Mathematica get the top prize. The performance criteria had to be very subjective. I have not run any benchmarks whatsoever, I just report the feeling I got from what I read about the languages. Libraries seem to be the weak spot of Lisp. The language does not seem to come with built-in libraries for regular expressions, database connections, networking or such things. I might be mistaken, but that is the impression I got.

Literate programming is for me the capability of writing a report and programming a data analysis in the same document. Here S (in particular its open source implementation R) shines with its Sweave tool, that allows one to mingle S code with LaTeX. The Mathematica notebook concept is somewhat similar but won't give as beautiful results. For Python I found a program called [Leo](http://webpages.charter.net/edreamleo/front.html "Leo"), which is apparently a very direct implementation of Knuth's original literate programming ideas.

So in the end I end up with a tie between S and Python. Mathematica follows closely, and should perhaps also deserve 13 points because its library is very powerful for mathematical applications.

What I did, in the end, was to use S as much as I can for analyzing data and producing reports and articles, and to use Python for everything else, including producing the data in the first place. Sounds like the best of all worlds.
