---
title: "How to test for floating point exceptions with CppUTest"
date: 2015-11-25
---

> Some programmers, when confronted with a problem, think "I know, I'll use floating point arithmetic." Now they have 1.999999999997 problems. // Tom Scott

Floating point arithmetic is notoriously hard to get right. I consider writing a bug-free, optimally performant numeric library to be approximately as hard as writing a compiler. Fortunately, most programmers don't need to deal with it, unless your work involves anything to do with science or engineering.

There's one subject though where I think you need to be a bit more careful. This is about understanding when and why your program will catch floating point exceptions (FPE). Let's consider a couple of examples.

Consider first this program `FPE.java`:

```
public class FPE {
  public static void main(String[] args) { 
    int i = 0; 
    System.out.println("1 / 0 = " + (1 / i));
  }
}
```

Compiling it and running it yields:

```
$ javac FPE.java
$ java FPE
Exception in thread "main" java.lang.ArithmeticException: / by zero at FPE.main(FPE.java:4)
```

In Java, dividing an integer by zero yields an `ArithmeticException`. Fair enough. What about floating points?

```
public class FPE2 { 
  public static void main(String[] args) { 
    double i = 0; 
    System.out.println("1 / 0 = " + (1 / i));
  }
}
```

Now this yields something different:

```
$ javac FPE2.java
$ java FPE2
1 / 0 = Infinity
```

I'm not sure I like having such a wildly different behavior. But consider now the same programs in C:

```
#include <stdio.h>

int main() {
  int i = 0;
  printf("1 / 0 = %d\n", 1 / i);
}
```

This is the result (under OSX):

```
$ gcc -o FPE FPE.c
$ ./FPE
Floating point exception: 8
```

Not exactly the most helpful error message ever, but at least the program crashes. Now the same thing with doubles:

```
#include <stdio.h>

int main() { 
  double i = 0.;
  printf("1 / 0 = %g\n", 1 / i);
}
```

And here's the result:

```
$ gcc -o FPE2 FPE2.c
$ ./FPE2 
1 / 0 = inf
```

So Java and C behave similarly: dividing an integer by zero crashes the program, but dividing a double by zero does not. I find it rather unsettling that `1 / 0` should result in a completely different program than `1 / 0.`. I realise now that I had assumed _all_ divisions by zero would be caught at runtime and cause the program to fail. This is, however, simply not true.

Our code at Neurobat includes a fair amount of numeric algorithms, which are decently covered by our unit tests. However, there remained the small possibility that the code could execute "illegal" floating point operations and silently fail.

There is no portable way to force a program to crash when a floating point exception is raised. You need to make sure that floating point exceptions cause a `SIGFPE` signal to be sent to your program. Only google can help you here, but for OSX [here is how you do it](http://stackoverflow.com/questions/247053/enabling-floating-point-interrupts-on-mac-os-x-intel).

What you can do in a portable way is to test if a floating point exception was raised, and I _highly recommend that you check for most floating-point exceptions in your unit tests_. I say "most", because you probably don't need to test for `FE_INEXACT`. See the manpage for `fenv` for details.

Here is how we do it in the [CppUTest framework](http://cpputest.github.io/). You need to test for exceptions before and after running your unit tests. We use plain assertions because CppUTest doesn't like that we use its assertions outside of a test run.

```
#include "CppUTest/CommandLineTestRunner.h"

#include <cassert>
#include <fenv.h>

void assert_no_fpe_raised(void) {
  assert(0 == fetestexcept(FE_INVALID) && "Invalid floating-point exception raised during tests.");
  assert(0 == fetestexcept(FE_DIVBYZERO) && "Division by zero raised during tests.");
  assert(0 == fetestexcept(FE_OVERFLOW) && "Overflow raised during tests.");
  assert(0 == fetestexcept(FE_UNDERFLOW) && "Underflow raised during tests.");
#ifdef FE_DENORMALOPERAND
  assert(0 == fetestexcept(FE_DENORMALOPERAND) && "Denormal operand raised during tests.");
#endif
  assert(0 == fetestexcept(FE_ALL_EXCEPT & ~FE_INEXACT) && "Floating-point exceptions (other than inexact) raised during tests.");
}

int main(int argc, char** argv) {
  int result;
  assert(0 == fetestexcept(FE_ALL_EXCEPT) && "Floating-point exceptions active before tests begin.");
  result = RUN_ALL_TESTS(argc, argv);
  assert_no_fpe_raised();
  return result;
}
```

So did we ever catch any bug with this? Indeed we did. We use an off-the-shelf optimisation algorithm that minimises an objective function in an $N$-dimensional space. At each iteration, the algorithm needs to compute the middle between two points where the objective function is to be evaluated. It does this by taking the mean of the points' coordinates, in the naive way: $x' = \\frac{x1 + x2}{2}$. What we found was, that if $x1$ or $x2$ is large enough, their sum could overflow. What's worse, the program would not terminate or fail in any visible way, but just return rubbish.

Bottom line is that if your program does any kind of floating point computation, consider having your unit test framework check for floating point exceptions. It probably won't do it by default.
