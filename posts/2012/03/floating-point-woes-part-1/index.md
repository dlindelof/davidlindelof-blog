---
title: "Floating-point woes, part 1"
date: 2012-03-12
categories: 
  - "programming"
---

You may have several decades of programming experience, certain classes of problems seem to repeatedly cause endless confusion. Floating-point computation is one such class.

I've been doing a fair amount of numerical analysis these past few months, implementing [floating-point](http://en.wikipedia.org/wiki/Floating_point "Floating point") calculations on embedded platforms. In the process I've stumbled across a few programming gotchas which I'd like to document in a (hopefully short) series of posts. I think that some of them are highly non-trivial, and that no amount of prior lecturing and/or reading (such as Goldberg's excellent \_[What Every Computer Scientist Should Know About Floating-Point](http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)\_ paper), there are still some issues that might surprise any programmer. I begin with a relatively simple and well-known example drawn from the programming class I teach.

(All the code examples in this series are available from git@github.com:dlindelof/fpwoes.git)

Termination criteria for a square-root calculating routine --------------------------------------------------------------------

Consider this program for calculating square roots by [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method "Newton's method"):

"sqrt1.c": #include #include #define EPS 0.000001 static float fabsf(float x) { return x < 0 ? -x : x; } static int sqrt\_good\_enough(float x, float guess) { return fabsf(guess\*guess - x) < EPS; } static float sqrt\_improve(float guess, float x) { return (guess + x/guess)/2; } static float sqrt\_iter(float x, float guess) { if (sqrt\_good\_enough(x, guess)) return guess; else return sqrt\_iter(x, sqrt\_improve(guess, x)); } float sqrt(float x) { return sqrt\_iter(x, 1.0f); } int main(int argc, char\*\* argv) { float x = atof(argv\[1\]); printf("The square root of %.2f is %.2f\\n", x, sqrt(x)); return 0; } This program works well enough with arguments smaller than about 700. Above that value, one gets segmentation faults:

$ ./sqrt1 600 The square root of 600.00 is 24.49 $ ./sqrt1 1000 Segmentation fault

Debugging the progam under \`gdb\` shows that a stack overflow happened:

$ gdb ./sqrt1 Reading symbols from /home/dlindelof/Dropbox/Projects/fpwoes/sqrt1...done. (gdb) run 1000 Starting program: /home/dlindelof/Dropbox/Projects/fpwoes/sqrt1 1000 Program received signal SIGSEGV, Segmentation fault. fabsf (x=Cannot access memory at address 0x7fffff7feff4 ) at sqrt1.c:6 6 static float fabsf(float x) { (gdb) bt #0 fabsf (x=Cannot access memory at address 0x7fffff7feff4 ) at sqrt1.c:6 #1 0x00000000004005aa in sqrt\_good\_enough (x=1000, guess=31.622776) at sqrt1.c:11 #2 0x0000000000400610 in sqrt\_iter (x=1000, guess=31.622776) at sqrt1.c:19 #3 0x000000000040063a in sqrt\_iter (x=1000, guess=31.622776) at sqrt1.c:22 #4 0x000000000040063a in sqrt\_iter (x=1000, guess=31.622776) at sqrt1.c:22 #5 0x000000000040063a in sqrt\_iter (x=1000, guess=31.622776) at sqrt1.c:22 #6 0x000000000040063a in sqrt\_iter (x=1000, guess=31.622776) at sqrt1.c:22 #7 0x000000000040063a in sqrt\_iter (x=1000, guess=31.622776) at sqrt1.c:22 #8 0x000000000040063a in sqrt\_iter (x=1000, guess=31.622776) at sqrt1.c:22 #9 0x000000000040063a in sqrt\_iter (x=1000, guess=31.622776) at sqrt1.c:22 #10 0x000000000040063a in sqrt\_iter (x=1000, guess=31.622776) at sqrt1.c:22

What's happening should be quite clear here. The best estimate for the square root of 1000 in single precision is 31.622776, whose square is 999.999939, differing from 1000 by about 6.1e-5, i.e. way more than the specified tolerance of 1e-6. But it is the best approximation that can be represented in single precision. In hex, it is \`0x41fcfb72\`. One least-significant bit (LSB) less, or \`0x41fcfb71\`, represents 31.6227741 whose square is 999.999817, off by 18.3e-5. One LSB more is \`0x41fcfb73\` or 31.6227779, whose square is 1000.00006, off by 6.1e-5, i.e. the same difference as for 31.622776. 31.622776 is therefore the best approximation to the square root of 1000 with single-point precision.

To have the program terminate instead of entering an infinite loop we need to rethink the termination criteria. Obviously we cannot use an absolute difference between the square of our guess and the argument, for as we have just seen, for large values it might not be possible to get an answer whose square is close enough to the argument.

We could imagine using a \_relative\_ difference instead:

static int sqrt\_good\_enough(float x, float guess) { return fabsf(guess\*guess - x) / x < EPS; } This gives us a second program \`sqrt2.c\`, which works much better:

$ ./sqrt2 1000 The square root of 1000.00 is 31.62 $ ./sqrt2 5 The square root of 5.00 is 2.24 $ ./sqrt2 2 The square root of 2.00 is 1.41 $ ./sqrt2 1 The square root of 1.00 is 1.00 $ ./sqrt2 100000 The square root of 100000.00 is 316.23 $ ./sqrt2 10000000 The square root of 10000000.00 is 3162.28 $ ./sqrt2 1000000000 The square root of 1000000000.00 is 31622.78 $ ./sqrt2 0.5 The square root of 0.50 is 0.71 $ ./sqrt2 0.1 The square root of 0.10 is 0.32 $ ./sqrt2 0.01 The square root of 0.01 is 0.10 $ ./sqrt2 0.05 The square root of 0.05 is 0.22 Interestingly, Kernighan and Plauger (in their clasic \_The Elements of Programming Style\_) deal with a very similar problem in the first chapter, but introduce a slightly different termination criteria. Translated into C from the original Fortran, this would give:

static int sqrt\_good\_enough(float x, float guess) { return fabsf(x/guess - guess) < EPS \* guess; }

I asked the good folks on www.stackoverflow.com why one termination criteria might be better than another. I've accepted the answer that explained that the termination criteria should match the update definition. In other words, you want the termination criteria to be equivalent to saying \`|guess\[n+1\] - guess\[n\]| < guess\[n\] \* EPS\`. Given that \`guess\[n+1\] = (guess\[n\] + x/guess\[n\])/2\`, one obtains a termination criteria that reads \`|x/guess\[n\] - guess\[n\]| < guess\[n\] \* EPS\` --- which is exactly the termination criteria preferred by K&P.

Note furthermore that this criteria correctly handles the case when \`y == 0.0\`. However, the program will still eventually produce nonsense on an input of \`0.0\`. Quoth the debugger:

#1 0x0000000000400636 in sqrt\_iter (x=0, guess=0) at sqrt3.c:22 #2 0x0000000000400646 in sqrt\_iter (x=0, guess=1.40129846e-45) at sqrt3.c:22 #3 0x0000000000400646 in sqrt\_iter (x=0, guess=2.80259693e-45) at sqrt3.c:22 #4 0x0000000000400646 in sqrt\_iter (x=0, guess=5.60519386e-45) at sqrt3.c:22 #5 0x0000000000400646 in sqrt\_iter (x=0, guess=1.12103877e-44) at sqrt3.c:22 #6 0x0000000000400646 in sqrt\_iter (x=0, guess=2.24207754e-44) at sqrt3.c:22 #7 0x0000000000400646 in sqrt\_iter (x=0, guess=4.48415509e-44) at sqrt3.c:22 #8 0x0000000000400646 in sqrt\_iter (x=0, guess=8.96831017e-44) at sqrt3.c:22 #9 0x0000000000400646 in sqrt\_iter (x=0, guess=1.79366203e-43) at sqrt3.c:22 #10 0x0000000000400646 in sqrt\_iter (x=0, guess=3.58732407e-43) at sqrt3.c:22 #11 0x0000000000400646 in sqrt\_iter (x=0, guess=7.17464814e-43) at sqrt3.c:22 #12 0x0000000000400646 in sqrt\_iter (x=0, guess=1.43492963e-42) at sqrt3.c:22 #13 0x0000000000400646 in sqrt\_iter (x=0, guess=2.86985925e-42) at sqrt3.c:22 #14 0x0000000000400646 in sqrt\_iter (x=0, guess=5.73971851e-42) at sqrt3.c:22 #15 0x0000000000400646 in sqrt\_iter (x=0, guess=1.1479437e-41) at sqrt3.c:22 #16 0x0000000000400646 in sqrt\_iter (x=0, guess=2.2958874e-41) at sqrt3.c:22 #17 0x0000000000400646 in sqrt\_iter (x=0, guess=4.59177481e-41) at sqrt3.c:22

The termination criteria will eventually involve a \`0.0/0.0\` operation. There is no way out of this other than to explicitly handle that special case. The final program thus reads:

\`sqrt3.c\` #include #include #define EPS 0.000001 static float fabsf(float x) { return x < 0 ? -x : x; } static int sqrt\_good\_enough(float x, float guess) { return fabsf(x/guess - guess) < EPS \* guess; } static float sqrt\_improve(float guess, float x) { return (guess + x/guess)/2; } static float sqrt\_iter(float x, float guess) { if (sqrt\_good\_enough(x, guess)) return guess; else return sqrt\_iter(x, sqrt\_improve(guess, x)); } float sqrt(float x) { if (x == 0.0) return 0.0; else return sqrt\_iter(x, 1.0f); } int main(int argc, char\*\* argv) { float x = atof(argv\[1\]); printf("The square root of %.2f is %.2f\\n", x, sqrt(x)); return 0; }

What's the most obscure bug involving floating-point operations you've ever been involved in? I'd love to hear from it in the comments below.
