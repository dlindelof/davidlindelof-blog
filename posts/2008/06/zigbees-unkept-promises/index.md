---
title: "ZigBee's unkept promises"
date: 2008-06-03
categories: 
  - "home-automation"
---

The Guardian carries an [interesting story](http://www.guardian.co.uk/technology/2008/may/01/wifi.zigbee) about yet another alternative to ZigBee: Ultra-low Power Bluetooth.

ZigBee has been touted since 2003 as a low-power, low-bandwidth wireless protocol ideally suited to home automation applications. But as the article makes clear, "we aren't all drawing our curtains and turning on the lights with the touch of a button". It is not clear why ZigBee hasn't yet established itself in the market. A high barrier to entry might explain part of it. But according to the article, possibly the biggest obstacle to ZigBee adoption is its mesh topology, requiring all nodes to continuously listen to incoming data to pass on to the other nodes. Bluetooth, on the other hand, has a simpler star-shaped network but much more limited in range and number of devices.

From my earlier life working on a ZigBee-based home automation product I can testify how we often had power problems with our ZigBee devices. The alternative was to have them all dormant, periodically waking up and transmitting their (own) data. But then we are back to a star-shaped network, and we are unable to actively query a node for its current status.

There's no easy way out of this dilemma. As the article has it, "you can't do low power and mesh at the same time."
