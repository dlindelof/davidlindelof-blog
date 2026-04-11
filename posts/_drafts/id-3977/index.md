---
title: "Solving one of the 1C puzzles"
draft: true
---

On Saturday 6 May, a few minutes before noon, I sat down at the maternity's cafeteria, opened my laptop, and waited for the countdown until round 1C of the 2018 Google Code Jam would begin.

I could only spend one hour there (hint: it was the maternity after all) so I solved just one problem. Here I try to document my thought process as I recall it.

You're given N words, all of length L. You must then form a new word, the first letter of which must be taken from the first letter of the N words, the second letter from the second letter, etc up to the Lth letter.

For example, if N=3 and L=4, and you're given

FOUR  
LAST  
TIME

One solution would be FAME. (The new word does not need to be a "real" word.)

The trick in solving most programming puzzles like this lies in recognizing a well-disguised, but well-known algorithm. It's usually worth spending a couple of minutes thinking about the algorithms and data structures you are familiar with, seeing if you recognize something.
