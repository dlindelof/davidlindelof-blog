---
title: "Git workflow at Neurobat"
draft: true
---

This is a rough outline of the Git workflow we use at Neurobat.

It has taken several months, or even years, to arrive at the workflow we have now. It is probably not perfect yet but it is currently what works out best for us.

The fundamental principle is the following: _Origin remains clean no matter what_. Other versions of this principle include _No junk on the trunk_.

Other principles include:

. All pull requests must have been either reviewed or pair-programmed.

We all fork from a common, master repository that has only two branches: `master` and `next`. Yes, we have been partially inspired by the workflow used by the Git project.

When work begins on a new feature/story/bugfix, the first thing the developer does is to checkout a new branch in his private repo, preferably rooted in `master`:

```
git co -b some_topic
```

After a number of commits to this branch, the developer is ready to request a pull by the maintainer of the origin repository. But before they are allowed to request such a pull, the whole work so far must be either a) formally reviewed, or b) be the product of pair-programming. In other words, nothing can be pull-requested that has not been seen by at least two pairs of eyeballs.

(Note: we are currently reviewing our, well, review processes. The most notable recent change is that we now requite the author in a review to provide proof that his work performs as advertised.)

The maintainer of the origin repository can now merge the pull request. Whether to merge into `master` or `next` depends on how trivial the change is. If it is a trivial change that affects non-critical files (e.g. typo corrections, small fixes to our data plotting scripts etc) then it can be merged directly to `master`. But most of the time, it will be merged into `next`.

The `next` branch will therefore always contain the set of changes that are scheduled for inclusion in the next release. Once they have been merged into `next`, two things must happen before `next` can be merged back into `master`:

1. A heating controller built from `next` must have run without errors for at least one week in at least two test sites, and
2. The developer must have demonstrated the feature/bugfix to the product owner.

To be honest, we are still a little bit unsure on how to handle certain use cases, such as one feature in `next` not working. But as I said, this process is still new to us and we just have to try it out for a couple of weeks and see how it works out for us.
