---
title: "What to do when you need a templated virtual function"
draft: true
---

I had a class responsible for making local climate forecasts. It provided estimates for the outdoor temperature on an hourly basis. The first version of the API looked like this:

class Model { std::vector forecast(); }

This class soon bacame part of a wider model-predictive control framework, so to unit-test its clients I soon needed to mock it out. This resulted in the following solution:

Model ^ | AdaptiveModel MockModel

class Model { virtual forecast = 0; }

But something was bugging me. I didn't like the idea of using an STL container as part of the interface. Not all clients of this class could be assumed to have STL available. And perhaps the caller might want the forecast in another kind of container, or even a plain C-style array. And finally, this interface almost always implied copying a whole vector.

Indeed, most STL functions avoid specifying the kind of container they work with and rely instead heavily on templare functions, whose template arguments are frequently iterators. So the forecast function could be refactored to look like this:

template virtual forecast(OutputIterator it);

this is nice, because the caller would now have the maximum choice:

std::vector result; forecast(back\_inserter(result));

It's lovely and exactly what I was aiming for. It's also wrong. The C++ language forbids virtual template functions.

Before we discuss the solution, let's remind ourselves why we need a template in the first place. We do because there is no such class as an "OutputIterator" superclass from which all output iterators derive. If there were, we might be able to use that superclass in the function's signature. So you might be tempted to construct such a superclass, using perhaps Boost's any::range. But I think there's a bettwe way.

We cannot have a virtual template function; but when you think of it, perhaps the "virtualness" of forecast can be separated from its "templatedness". After all, there are two clear responsibilities here: computing the forecast (virtual) and returning it to the caller (template). With that in mind:

class Model { template forecast { for ... } private: doForecast(); }
