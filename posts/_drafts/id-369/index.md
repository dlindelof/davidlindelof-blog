---
title: "A cluster building algorithm"
draft: true
---

Recently I came across some piece of stunningly crafted MATLAB code that was used to generate the system matrices for a typical office room. It was basically a gigantic function, almost 1000 lines long, that began by initializing the system matrices with zeros:

`A = zeros(30, 30); B = zeros(30, 13);`

There are 30 floating thermal nodes in this model (hence the 30 rows of A and B, and the 30 columns of A), 6 heat sources and 7 fixed thermal nodes (hence the 13 columns of B).

The function then proceed by filling in each section of _A_ and _B_, beginning with the indoor air in the upper left corner, proceeding through each of the four walls, ceiling, floor, window, window frame, and ending in the lower right corner with the heating equipment. At the very end of all this, the function makes sure that the diagonal elements of _A_ satisfy the basic energy conservation equations.

Michael Feathers, in his book Working Effectively with Legacy Code, has a name for this style of programming. I think he called it a "Bulleted Method", e.g. a method that, instead of doing one thing and doing it well, tries to do a series of things one at a time.

I think this style of programming is quite common in the scientific world (from which I come, incidentally, so I'm allowed to say bad things about them/us). We scientists and engineers tend, when we program, to think more in terms of scripts rather than trying to write clean, modular code. The person who wrote this code was either under tremendous time pressure to get things done or was oblivious to the possibility that someone, somewhere might want to someday change the model. Well here I am.

After staring and the model for many evenings I realized something that, I think, is common in building energy models: most buildings can be modeled as a cluster of weakly coupled sub-clusters. For instance, you will model a typical wall as a series of layers coupled to each others, but only the outermost layers will be coupled to other building elements---the innermost layer to the indoor air, and the outermost layer (if it is an exterior wall) to the outdoor air and to incident radiation. This is also why, in thermal building simulation, you often deal with sparse matrices.

\[ graphviz name=Wall \] main -> parse -> execute; main -> init; main -> cleanup; execute -> make\_string; execute -> printf init -> make\_string; main -> printf; execute -> compare; \[/graphviz\]

Now the legacy code I was working with had several functions that would compute partial coupling matrices for different building elements---walls, windows, etc. I thought it could be an interesting thing if the entire building's system matrices could be built up incrementally from the individual partial matrices.

So let me first introduce some notation:

Let _T_ be the vector of free-floating node temperatures in the model, i.e. the nodes whose temperature are left free to evolve. Let _S_ be the vector of heat sources relevant to that cluster of nodes. If we're dealing with the nodes describing the layers of an outward-facing wall, for instance, the sources would include the incident solar radiation. Let also _U_ be the vector of nodes external to our cluster, but whose thermal coupling is known in advance. With our wall example, there would be at least two such external nodes: one for the indoor air (coupled to the innermost wall layer) and one for the outdoor air (coupled to the outermost wall layer).

Then the evolution of this cluster is given by the following:

CdTdt=A×T+B×S+D×U

where:
