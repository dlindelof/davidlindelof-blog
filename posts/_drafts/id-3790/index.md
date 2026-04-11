---
title: "The nice thing about degree-days is that there are so many of them"
draft: true
---

[Degree-days](https://en.wikipedia.org/wiki/Degree_day) are a measure of how cold a given range of dates has been. Ideally, the heating demand of a building during that period should be proportional to the degree-days of that period.

Under steady-state conditions, the heating demand of a building will be proportional to $$\\int(\\theta\_b - \\theta)^+\\mathrm{d}t$$ where $\\theta\_b$ is the building's _base temperature_ (sometimes also called the _balance temperature_), and $(.)^+$ stands for the _positive part_ function, such that $x^+ = x$ if $x > 0$ and $x^+ = 0$ otherwise.

Standards bodies have adopted this definition to define how the energy efficiency of a building is to be measured, and tables of degree-days are available for most parts of the world. The only problem is, for which base temperature?

The original ASHRAE standard recommended a base temperature of 18.3 C (or 65 F), which the ASHRAE Handbook states:

> ... represents average conditions in typical buildings in the past.

But in Europe, things get more complicated. In the UK, the recommended base temperature is apparently 15.5 C, because according to [the Carbon Trust](http://www.carbontrust.com/resources/guides/energy-efficiency/degree-days/) because:

> ... at this temperature most UK buildings do not need supplementary heating.

In Switzerland, the SIA (Société Suisse des Ingénieurs et des Architectes) published the SIA 381/3 norm, defining something also called _degrés-jours_ (or degree-days) but defined very differently. First, _heating days_ are defined as those days during which the average outdoor temperature drops below the base temperature. Second, the degree-days are calculated as above, but _only for the heating days_ and using a •base temperature 8 degrees higher than the one used to define a heating day\*.

For example, a day with an average outdoor temperature of 10 C will yield 8.3 DD (ASHRAE) but 10 DD (SIA). A day with an average outdoor temperature of 13 C will yield 5.3 DD (ASHRAE) but 0 DD (SIA).

Since 2015 the SIA has now abandoned that definition, but many cantons continue publishing _official_ degree-days using the old definition, usually using 12 C as a base temperature.

The new SIA 380:2015 norm has instead adopted the ISO 15927-6:2007 European norm, which essentially uses the ASHRAE definition but recommends a base temperature of 12 C. These have been renamed _Accumulated Temperature Differences (ATD)_. It is however very hard to obtain official values, unless you are willing to do some manual programming.

I have checked what values are published by different cantons and here is what I've found:

- Geneva: [degree-days base 18/12](http://ge.ch/energie/media/energie/files/fichiers/documents/degres_jour_global_2015_decembre.pdf)
- Vaud: [weekly degree-hours](http://www.vd.ch/themes/environnement/energie/chauffage/suivi-de-consommation/degres-heures-saison-2015-2016/), doesn't say what basis is used
- Neuchâtel: [daily degree-days](http://www.ne.ch/autorites/DDTE/SENE/energie/Pages/Degres-jours.aspx), looks like 20/12 basis
- Valais: [monthly degree-days](https://www.vs.ch/web/sefh/donnees-meteorologiques), says they come straight from Meteosuisse and looks like 20/12
