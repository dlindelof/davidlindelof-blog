---
title: "My go-to software libraries for API design"
draft: true
---

API design is possibly the hardest aspect of software engineering. Everything else, including architecture, can in principle change and evolve over time, be refactored, etc. Even database schemas can be made to evolve, if the business needs demand it. But an API is an entirely different matter. A carelessly designed API is something that will live with you for ages to come and plague you.

I've never claimed being particularly skilled at this craft, so what I do when I need to design an API is turn to my masters for inspiration. And there are a few exceptionally well-designed and well-documented libraries out there, to which I usually turn when I need inspiration.

## The Numerical Algorithms Group

Albeit not open-source, this is an amazingly well-designed and documented library for numerical work. It is all the more remarkable as it is entirely implemented in C or Fortran, and thus manages to do without the usual niceties such as exceptions, default arguments, function overloading etc that usually help in making an API easy to use.

Consider for example one of the many functions available for optimising an objective function. This one minimises a function in N-dimensional space by the _Nelder-Mead_ algorithm (sometimes also called the _simplex_ algorithm):

```
void nag_opt_simplex_easy (Integer n, double x[], double *f, double tolf, double tolx,
                           void (*funct)(Integer n, const double xc[], double *fc, Nag_Comm *comm),
                           void (*monit)(double fmin, double fmax, const double sim[], Integer n, Integer ncall, double serror, double vratio, Nag_Comm *comm),
                           Integer maxcal, Nag_Comm *comm, NagError *fail)
```

You don't really need to read the documentation to figure out what most of these arguments represent. `n` is clearly the dimensiona What makes the NAG library easy to use is a certain consistency in the way their functions are designed. Most of them return `void`, and take a `NagError*` argument as the last argument to communicate success or failure. `NagError` is a structure with the following fields:

```
int code;
Nag_Boolean print;
char message[NAG_ERROR_BUF_LEN];
Integer errnum;
void (*handler)(char*,int,char*);
```

And this is all you, as a user of the library, need to know in order to check if the function call succeeded or not.

## sqlite

## lpsolve

## libcurl
