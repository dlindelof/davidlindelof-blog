---
title: "Evaluating energy conservation measures: lessons learned"
draft: true
---

Suppose you invest in making your home more energy-efficient. You carefully record your energy consumption both before and after the intervention. You find that the energy bill is higher after the intervention than before. Now what?

Evaluating the performance of energy conservation measures is hard. The energy demand of a building depends on many variables, most of which are beyond our control such as the weather.

I work for Neurobat AG, a small Swiss company specialised in advanced control algorithms for efficient space heating in buildings. Since the company's inception we have carried out several field tests to evaluate the performance of our systems.

We've recently been asked to provide a short summary of our experience in evaluating the performance of energy conservation measures. Here is the gist of what I wrote.

## The 2013--2014 field tests

During the 2013--2014 winter we measured the _energy signature_ of 10 single-family houses, both with our controller and with the existing one. The test is written up in an _Energy & Buildings_ paper (see below), where the experiment is described in detail.

The heating energy consumption of each building was continuously measured throughout the winter, together with other temperatures including the indoor and outdoor temperatures. Plotting the daily heating energy consumption against the mean daily outdoor temperature yields the energy signature of the building. By regularly alternating between the Neurobat controller and the standard controller, we obtained two energy signatures for each building. Comparing the slopes of these signatures yields an estimate of the energy savings achieved with the Neurobat controller.

A statistical analysis showed that when taken in isolation, no building showed statistically significant energy savings. But when taken all together, an average energy savings of 28% was obtained, albeit with a large variance from building to building.

### Lessons learned

- A single season is enough for comparing a heating control system against another provided that enough data is collected for each.
- The \`\`official'' IPMVP protocol would have taken too long and been too costly to implement.
- The two control systems should alternate regularly (but not more frequently than every 2 weeks).
- When economically feasible, a heat counter should be used on each building so that daily energy consumption can be measured.
- A good cooperation with the house tenants is essential for the success of the experiment.

## The "Aargau heizt schlau" project

In collaboration with the Aargau canton and the Fachhochschule Nordwestschweiz, we are currently evaluating the performance of our controller on 60+ single family houses in that canton.

For a project of this size it is not feasible to equip each building with its own heat counter, nor to regularly alternate between the new controller and the old one. Another solution had to be found.

We have designated some (less than 10) buildings as "index buildings", i.e. buildings deemed to be representative of the others. These index buildings are equipped with a heat counter and with a primary energy counter (e.g. gas meter, electricity meter or oil consumption meter). The energy signature of these index sites can thus be accurately established.

The overall performance of our system will then be assessed by comparing with the historic energy bills of the other buildings. The analysis is currently on-going, but the exploratory data analysis suggests that \`\`traditional'' analysis techniques (based on degree-days with a standard, one-size-fits-all base temperature) will not work. This calls for more advanced statistical techniques.

### Lessons learned

- Continuously monitoring the energy performance of building with cheap embedded PCs such as the Raspberry Pi is perfectly workable but requires constant monitoring to detect faults.
- Comparing the energy performance of a building after an intervention with its historic consumption data is probably doable but requires a skilled data analyst.
- "Official" methods for evaluating the performance of energy conservation measures should be treated with care; anecdotal evidence suggests that in many cases, these methods simply do not work.

## Publications

The 2013--2014 field tests, including the energy signature of each building, have been documented by Lindelöf, D. et al. in _"Field tests of an adaptive, model-predictive heating controller for residential buildings."_ _Energy and Buildings_ 99 (2015): 292-302.

The energy savings on a commercial building controlled remotely by an online optimisation server have been documented by Lindelöf, D. et al. in _"Architecture and field test of a RESTful web service for the optimization of space heating in a commercial office"_, CISBAT 2015, EPFL, Lausanne, September 9-11th, 2015.

A method for estimating the energy performance of a building (including its base temperature for degree-days) is the object of a paper submitted to _Energy and Building_ and currently under review.
