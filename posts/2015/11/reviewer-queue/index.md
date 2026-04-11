---
title: "Reviewer queue"
date: 2015-11-27
categories: 
  - "agile"
---

During a recent sprint retrospective we raised a problem with the way we assign code reviews. Not the formal, whole-team ones, but the regular ones we solicit for each pull request.

The problem was that we tend to select our reviewers based on various subjective criteria, including how well we like the person. I admit I am guilty of this myself. What's more, during the discussion it became clear that my own help in reviewing code was not asked as often as it used to.

At Neurobat we currently have a rule that all pull requests must be reviewed by two other team members (one, if the pull request was paired on). To ensure these reviewers are selected fairly and without subjectivity, we have now introduced a **reviewer queue**: our names are listed on the main whiteboard and an arrow is drawn, showing who is next in the review queue. When a reviewer is assigned, the arrow moves to the next name.

[![Neurobat reviewer queue](images/review_queue-225x300.jpeg)](http://computersandbuildings.com/wp-content/uploads/2015/11/review_queue.jpeg)

We've had this in place for a couple of sprints now and the results have been very satisfying:

- people get to review parts of the code they had never seen before
- people are "forced" to review code written in unfamiliar languages
- the reviews are more likely to be honest and thorough
- the review work gets more evenly spread out among the team

An added benefit for myself is that by explicitly putting my name among the review queue, I announce my willingness to participate in the reviewing process as much as anyone else. As a result, I've been reviewing much more code this last couple of weeks than ever before.

If you have a problem in the selection of reviewers in your own team, do consider setting up a review queue and let me know whether that works out for you.
