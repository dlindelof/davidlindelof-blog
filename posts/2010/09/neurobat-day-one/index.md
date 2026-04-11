---
title: "Neurobat, day one"
date: 2010-09-14
categories: 
  - "announcements"
---

Yesterday marked my first day as Chief Technology Officer at [Neurobat AG](http://www.neurobat.net/), a young company formed in Switzerland to industrialize and market advanced building control algorithms, such as the ones commonly researched and developed at my former laboratory, the [Solar Energy and Building Physics Laboratory at EPFL](http://lesowww.epfl.ch/).

This also marks the end of almost three years spent building enterprise integration systems in Java for a certain coffeeshop. I'm now moving back to my original topics of interest, namely the intelligent control and simulation of buildings. Indeed, without disclosing too much, the very first project I will be working on is the implementation of certain ideas formulated during the Neurobat research project carried out aeons ago at LESO-PB. Except this time the systems won't be running in the quiet and safe environment of an experimental building whose occupants have a history of forgiveness towards enthusiastic graduate students and their ideas---including myself. No, this time we mean business, that is, embedded systems that must be build rock-solid and run unattended for years, or possibly decades.

One issue that's come up more than once was whether we should keep MATLAB as our lingua franca for prototyping and trying out new ideas and concepts before porting them to languages more, shall we say, closer to the machine. Or should we just dump it (including its non-negligible licencing costs, especially for an non-academic organization) and work directly as close to the metal as we dare?

Personally, without wanting to sound overly smug or anything, I think that someone asking this question has obviously never tried multiplying two matrices in C. The implementation contributed by [James Trevelyan to the Numerical Recipes in C website](http://www.nr.com/contrib/) runs to about 33 lines:

void dmmult( double \*\*a, int a\_rows, int a\_cols, double \*\*b, int b\_rows, int b\_cols, double \*\*y) /\* multiply two matrices a, b, result in y. y must not be same as a or b \*/ { int i, j, k; double sum; if ( a\_cols != b\_rows ) { fprintf(stderr,"a\_cols b\_rows (%d,%d): dmmult\\n", a\_cols, b\_rows); exit(1); } #ifdef V\_CHECK if ( !valid\_dmatrix\_b( a ) ) nrerror("Invalid 1st matrix: dmmult\\n"); if ( !valid\_dmatrix\_b( b ) ) nrerror("Invalid 2nd matrix: dmmult\\n"); if ( !valid\_dmatrix\_b( y ) ) nrerror("Invalid result matrix: dmmult\\n"); #endif /\* getchar(); dmdump( stdout, "Matrix a", a, a\_rows, a\_cols, "%8.2lf"); dmdump( stdout, "Matrix b", b, b\_rows, b\_cols, "%8.2lf"); getchar(); \*/ for ( i=1; i<=a\_rows; i++ ) for ( j=1; j<=b\_cols; j++ ) { sum = 0.0; for ( k=1; k<=a\_cols; k++ ) sum += a\[i\]\[k\]\*b\[k\]\[j\]; y\[i\]\[j\] = sum; } }

Give me instead MATLAB's

y = a \* b

anytime. Now of course I realize the comparison is completely unfair. The C version includes error checking, comments, etc. But still, C is, after all, originally a systems programming language, while MATLAB-the-language is a DSL for doing precisely this sort of stuff. I never wanted to prove that C sucked at doing linear algebra---I just wanted to show that most trivial operations in MATLAB would have to be---by us---re-implemented in C before we can even begin using them. And I don't think we have that sort of time. Not outside of academia.
