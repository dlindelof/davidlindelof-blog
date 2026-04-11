---
title: "IPMVP"
draft: true
---

I'm having mixed feelings about IPMVP, the International Performance, Measurement and Verification Protocol.

It's this widely used protocol that's supposed to unify the way people establish the efficacy of energy conservation measures in buildings. When you install, say, better windows in a building with higher insulation, you just cannot do this on one building and have another identical building untouched (a so-called control building). Every building is unique. So when you install an ECM, you must have a method to determine whether it worked or not.

Now frankly I'm not even sure why we need a standard protocol for this. Time-series analysts have been doing intervention analysis for a very long time, but apparently no one has bothered asking them for their advice. So anyway, here we are with the IPMVP.

I've read through the entire IPMVP Core Concepts document. In some places it is brilliantly clear and leaves little room for interpretation:

> Each project **must** be individually designed to suit the objectives and desired accuracy of energy- or water-saving efforts.
> 
> Adjustments **must** account for the differences in conditions between the baseline and reporting periods.
> 
> Valid mathematical techniques **must** be used to derive the adjustment method for each M&V plan.

But elsewhere I've found the standard to be uncomfortably vague:

> Where multiple versions of the same ECM installation are included within the measurement boundary, statistically valid samples **may** be used as valid measurements of the total parameter.
> 
> Engineering calculations or mathematical modelling **may** be used to assess the significance of the errors in estimating any parameter in the reported savings.
> 
> Several meters **may** be used to measure the flow of one energy type into a facility.
> 
> A model may be as simple as an ordered list of twelve measured monthly energy quantities without any adjustments.
> 
> Some variables may be measured for short intervals (day, week or month) or extracted from existing operating logs.
> 
> Techniques may be as simple as a constant value (no adjustment) or as complex as a several multiple parameter non-linear equations each correlating energy with one or more independent variables.
