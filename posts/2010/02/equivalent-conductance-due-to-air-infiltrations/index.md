---
title: "Equivalent conductance due to air infiltrations"
date: 2010-02-22
categories: 
  - "energy"
tags: 
  - "air-infiltration"
  - "thermal-conductance"
---

Here is how you compute the thermal coupling between a room's indoor temperature and the outdoor temperature due to infiltrations.

The equation governing the exchange of heat is as follows:

Cair × dT/dt = g × Δ T

where Cair is the indoor air thermal mass \[J/K\], T is the indoor air temperature \[K\], g is the equivalent conductance \[W/K\] and Δ T is the temperature difference between indoors and outdoors.

What we need to compute is how much heat is exchanged per unit of time when air seeps into the indoor room. The air that infiltrates will draw (or more rarely, yield) heat from the indoor air until it reaches thermal equilibrium with T. So we obtain:

V' × ρ × Cp air × Δ T = J

where V' is the infiltration rate \[m3 / s\], ρ is the air density (about 1.2 kg/m3), Cp air is the air thermal capacity (about 1008 J/kgK) and J is the rate of heat exchange in W.

Now we immediately recognize that actually, J / Δ T = g. But we can also simplify further by noting that air infiltration rates are more commonly given in room volumes renewed by some unit of time (commonly the hour). Note first that:

Cair = Vair × ρ × Cp air

and therefore:

V' × Cair / Vair = g

or more simply, if Nren is the room volume renewal rate per hour:

Nren / 3600 × Cair = g

And therefore the main equation becomes simply:

dT/dt = Nren / 3600 × Δ T

I find this to be an amazingly simple equation, especially as it applies to other situations similar to air infiltrations. For example, you can use it to compute the exchange of heat among the elements of a heater through which hot water circulates.
