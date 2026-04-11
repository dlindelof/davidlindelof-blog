---
title: "The two most important tasks of the ScrumMaster"
draft: true
---

In "Adrenaline Junkies and Template Zombies", the authors warn us against what they call "talk show" team meetings; i.e., meetings where there's more talk than action.

One especially dangerous form of talk show meeting is what they call **All roads lead to design**. You've seen such meetings, I am sure. It's the standup meeting where you can't mention any impediment without everybody feeling obligated to trying to fix the issue. It's the product change review board where changes are not being approved, but designed. Such meetings are toxic because they appear very productive (after all, we are designing something, right?) but in fact no action is being taken.

As a ScrumMaster, it is your responsibility to make sure that standup meetings never degenerate into such design meetings. If someone has a problem or a question, and it looks like another team member may have an answer, schedule an off-line meeting between the concerned parties. Don't let this discussion take over the standup meeting.

In fact I'd like to go one step further and define what I believe are the two most important duties of the ScrumMaster.

## Make sure everybody understands what was said during the standup meeting

This may sound obvious. However, keep in mind that some team members are so engrossed in the details of their work that they lose sight of the bigger picture, and may not realise that the rest of the team understand the what and the why of their work.

As an example, I've recently configured the SSL security for our Neurobat Online service. That involved generating an SSL key, a certificate, a certificate signing request, having that request approved, installing the necessary files on the server etc. At a standup meeting, which would be best:

> Yesterday I've generated the `nolserver.key` and `nolserver.crt` files and uploaded them to GoDaddy. Today I'll install them to `/etc/ssl/certs` and `/etc/ssl/private` and see if `openssl s_client` can connect to the server.

or

> Yesterday I generated the SSL certificate/key pair for the NOL server and sent them for signing by the CA. Today I'll finish setting up the SSL security on the server and test it.

When you hear a team member go too much into detail, you have the right--nay, the _duty_\--to interrupt and ask him for a higher-level overview of what he's doing. If he says he's laying bricks one of top each others, ask him to clarify that he's building the north wall of a cathedral.

## Make sure the retrospectives are held

The retrospective meeting is probably the most misunderstood, yet the most important meeting in any agile process. Without it, your team will follow a process sprint after sprint without ever questioning whether your practices are the most applicable ones.

At Neurobat we hold retrospectives at the beginning of each sprint. Those meetings have helped us formulate changes to the "canonical" Scrum methodology that we began with, almost three years ago. Some of the most important, and long-lived decisions, include:

- Using a Kanban-style process instead of Scrum, found to be more suitable for a development process with a strong research component;
- Assigning a _Process Pest_: each team member is responsible for making sure the processes are being followed;
- Defining clear testing goals and suites for our release process, which enables us to deploy new release candidates twice a month (not bad for an embedded product, if you ask me).

Why aren't sprint retrospectives more often applied? One reason, I believe, is simply that they are _hard_ to moderate effectively. It takes skill and practice. We are far from perfect at it. Several resources have helped us in that respect, including:

- The [Facilitating Discussion](http://www.toastmasters.org/MainMenuCategories/Shop/ManualsBooksVideosCDs_1/MANUALSBOOKSVIDEOSCDs/TheCommunicationProgram/THEDISCUSSIONLEADER406.aspx) advanced Toastmasters manual has been a great help for me, and was a great way to practice the discussion moderation techniques discussed in:
- "Agile Retrospectives", which I still believe is the only book on retrospectives you need to read. But read it you need.
