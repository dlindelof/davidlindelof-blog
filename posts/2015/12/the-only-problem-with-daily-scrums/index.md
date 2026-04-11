---
title: "The only problem with daily scrums"
date: 2015-12-04
categories: 
  - "agile"
---

Over the past five years, our team has attended more than 120 daily standup meetings, carefully following the "canonical" format and having each team member answer the usual questions:

1. What did you do yesterday?
2. What will you do today?
3. Any impediments?

[![](images/9051bb106cb801301d46001dd8b71c47)](http://dilbert.com/strip/2008-04-16)

There seems to be one flaw with this format, however. **The flaw is that you cannot say what you will do for the day before having heard if anyone else has an impediment.**

For example, if Alice says her bit, announcing what she intends to do for the day and declines to mention any impediments, then when Bob's turn comes and he mentions that he's having some trouble and could use some help, then Alice will have to come back to what she has just said and amend her plans for the day.

In Neurobat we've implemented a partially debugged hack around this problem by having two standup rounds. During the first round we do the canonical standup meeting, then the ScrumMaster asks if anyone needs a second round. The goal of this second round is two-fold:

1. To let anyone say something he may have forgotten about during the first round.
2. To let anyone amend their plans for the day due to something they may have heard during the first round.

This solution is far from ideal, and sounds annoyingly like a two-pass compiler. But it is, for now, the best approach we have found to deal with what I perceive to be the main drawback to the canonical form of the daily scrum.
