---
title: "Scrum team members play a Nash equilibrium"
draft: true
---

Consider the following software development team, all abiding by the canonical Scrum rules; in particular, every working day begins with a traditional daily Scrum when each team member is supposed to flag any impediment they may encounter.

Most Scrum resources will assume that all team members will play by the rules and truthfully report any problems, not being ashamed of any stigma attached to not making as much progress as the others.

Ok. So you've met the human race I presume? Chances are that your team members are human and won't like being singled out as the day's problem child. Unless, of course, someone else also reports impediments.

Game theory to the rescue. Let's say that there are only two team members, both blocked. Call them Alice and Bob. Each wants to avoid looking bad at the standup, but their "looking-goodness" depends on the other's statement, as in the utility table below (where we assume they will speak simultaneously; later we will relax this assumption).

| A\\B | Truth | Lie |
| --- | --- | --- |
| Truth | \-1/-1 | \-3/1 |
| Lie | 1/-3 | 2/2 |

So given this payoff matrix, how should you "play" if you're A? If both players are equally rational, they will both select the same strategy. Knowing that, they will obviously both prefer to hide the truth. This remains true even if we relax the assumption of simultaneous play, but assume they will have selected their strategy before the meeting and stick to it.

Now notice that the payoff matrix does not assume that the team members are really blocked or not. In other words, this payoff matrix biases team members against reporting any impediment, whether they really are blocked or not.
