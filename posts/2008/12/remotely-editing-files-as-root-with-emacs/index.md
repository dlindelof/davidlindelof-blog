---
title: "Remotely editing files as root with Emacs"
date: 2008-12-09
categories: 
  - "programming"
  - "tools"
---

I often need to edit files on remote machines or on embedded devices, that is, machines without a monitor and on which a proper editor might not necessarily be installed.

In the past that has always left me with the rather painful choice between vi and nano. Now I have never invested enough time in learning vi beyond the most basic editing commands. And nano is okayish for small edits but hopeless for larger ones.

[![](images/51dake2iual_sl160_.jpg)](http://www.amazon.de/gp/product/0596006489?ie=UTF8&tag=compandsmarbu-21&linkCode=as2&camp=1638&creative=6742&creativeASIN=0596006489)![](images/ir)

So I was delighted to learn that you can edit files remotely through ssh with Emacs. If you want to remotely edit aFile on host aHost, open the following file:

`/aHost:/path/to/aFile`

The built-in [Tramp](http://www.gnu.org/software/tramp/) package will take care of the rest. You can even use Dired remotely with this mechanism, an extremely powerful feature.

But what was missing for me was a painless way of editing remote files as root. The Tramp version that's included in Emacs 22.2.1 was 2.0.57, with which I was unable to remotely edit files as root. The latest version of Tramp, 2.1.14, is in my humble opinion far easier to work with.

To install it, just follow the [instructions](http://www.gnu.org/software/tramp/#Installation). I created a directory ~/emacs into which I unzipped the Tramp distribution. I compiled it in place and did not bother installing it system-wide, being the only user of my system.

Then I added the following to my .emacs file:

`;; Load most recent version of Tramp for proxy support (add-to-list 'load-path "~/emacs/tramp/lisp/") (require 'tramp) (add-to-list 'Info-default-directory-list "~/emacs/tramp/info/")`

With this in place, suppose you want to edit as root the files on aHost. The best is to add the following to your .emacs:

`;; Setting for working with remote host (add-to-list 'tramp-default-proxies-alist '("aHost.*" "root" "/ssh:yourusername@%h:"))`

Now editing remote files on aHost is easy, just open the following:

`/sudo:aHost:/path/to/aFile`

And that's about it.
