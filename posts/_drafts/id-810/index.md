---
title: "The most effective energy-saving measure you can make"
draft: true
---

When it comes to analysing the cost/benefit ratio of different energy efficiency measures, I'd like to submit that the most effective measure you can possibly make is to sell your house.

From the Neurobat R&D headquartes we monitor the energy use of several test buildings in Switzerland and abroad, most of which are single-family homes. With this data we have a pretty good idea about the energy demands of typical Swiss dwellings. Here is, for example, the daily heating energy for a house in Fey (VD), as a function of the average daily outdoor temperature:

As expected from basic building physics, the relationship is nicely linear. What is not so nice, however, is the daily energy use at the reference outdoor temperature of 8.5 degrees. According to this model, the Fey house uses $94\\pm4\\text{kWh}$ each day at that temperature. This translates to about 1.41 MJ/m$^2$ per day, or 514.65 MJ/m$^2$ per year.

It is difficult if not impossible for the layman to determine whether this number is reasonable. But fortunately, in Switzerland we have some fairly stringent building construction codes, many of which being codified in the SIA series of norms.

SIA 380/1 is _the_ norm that mandates how much heating energy a building is allowed to use in Switzerland. All new building designs must conform to it, as must all significant refurbishment projects. According to its most recent revision (2009), newly built single-family homes are allowed the following amount:

$$65 + 65\\times \\frac{A\_\\text{th}}{A\_\\text{E}} \\text{MJ/m^2/year},$$

where $A\_\\text{th}$ is the so-called "surface énergétique de référence", i.e. roughly speaking the living surface, and $A\_\\text{E}$ is the so-called "surface de l'enveloppe propre", i.e. roughly speaking the envelope surface. This energy budget is valid for an average outdoor temperature of 8.5 degrees C and an indoor temperature of 20 degrees C.

The Fey house is 240 m2 in surface; its envelope surface is unknown, but can be estimated at about 400 m2. Its yearly energy budget would therefore be $65 + 65\\times 400/240 = 48.15 \\text{MJ/m^2/year}$, or about 31.7 kWh per day. Its mean indoor temperature is not quite 20 degrees, however; it's currently closer to 23 degrees. The SIA norm allows for an extra 4% energy for a mean outdoor temperature lower than 1 degree; I believe that the same correction applies when the indoor temperature is higher by one degree, since the flow of energy from indoor to outdoor depends linearly on the temperature difference between indoor and outdoor. One should therefore multiply the daily energy budget by $1.04^3$, or about 1.12, yielding 35.8 kWh/d.

Even with this correction, the Fey house uses almost **three times more energy** than what a newly built house of the same size would. I've also checked informally these figures with an independent energy consultant and he's confirmed that these figures are about **twice** what was considered normal for a building built in 1998.

Is this situation specific to our Fey site? Unfortunately not.
