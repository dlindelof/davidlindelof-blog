---
title: "Building physics without equations"
categories: 
  - "general"
draft: true
---

Is it possible to run a computer simulation of building physics without equations?

Most building physicist I know would probably say no, at least not realistically. A buildinf will always be abstraccted by a set of thermal nodes, each with its thermal capaxity, each linked to heat sink/source, and connected to each others by equivalent conductances.

You then solve this model by writing out the differential equations---one per node---and stepping through the simulation one delta t at a time.

0 1 0 0 0 1 1 0 0
