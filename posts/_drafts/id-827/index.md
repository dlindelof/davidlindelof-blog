---
title: "My work environment's  Spinellis score"
draft: true
---

Recently Diomenides Spinellis posted an article titled "The Frictionless Development Environment Scorecard". That article got me to revisit my own work environment.

I use a laptop running Ubuntu 13.10 at work, and a MacBook Air when on the move (which is more often than I like).

### Workstation setup

> Are my personal settings and preferences consistent on all the computers I am using? Are they stored under version control? Can I install them on a new computer with a single command?

I currently keep all my so-called dotfiles synchronized across my computers via Dropbox; for example, my vim configuration file sits under `~/Dropbox/.vimrc`. Once a new machine has been Dropbox-synchronized, I create symbolic links from my home directory, such as `.vimrc -> Dropbox/.vimrc`.

This approach is simple; when I modify a configuration file it synchronizes automatically across all my machines. There is also a sort-of version control, since a file under Dropbox can always be reverted to one of its previous versions.

However, I'm less and less happy with this approach. I am more and more frustrated that my settings are not the "right" ones on the servers I administer, and installing Dropbox on production machines is, of course, out of the question.

A popular approach consists of keeping all your configuration files on GitHub. Searching for "dotfiles" yield currently 29498 repositories, and is the conventional name that GitHub users use for storing their configuration files.

> Are my favorite key bindings configured to be the same for the shell, command-line tools, and GUI environments?
