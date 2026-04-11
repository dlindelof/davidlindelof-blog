---
title: "Ubuntu fonts problem after reboot"
date: 2009-04-23
tags: 
  - "dpkg"
  - "ubuntu"
  - "x-org-server"
---

My screen fonts under [Ubuntu](http://www.ubuntu.com/ "Ubuntu") are occasionally completely screwed up. They show up in blue with overstrikes:

[![ubuntu-font](images/ubtuntu-font.png "ubuntu-font")](http://www.visnet.ch/smartbuildings/wp-content/uploads/2009/04/ubtuntu-font.png) I think this happens when I reboot my machine without a second monitor being attached to it, which it usually has. I suppose [X.org](http://www.x.org/ "X.Org Server") gets confused when it cannot find a monitor that used to be there.

To solve this problem you must reconfigure X.org. Just enter the following and log out and in again to your X session:

`sudo dpkg-reconfigure xorg`
