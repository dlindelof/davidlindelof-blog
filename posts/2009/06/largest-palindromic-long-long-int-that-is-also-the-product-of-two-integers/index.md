---
title: "Largest palindromic long long int that is also the product of two integers"
date: 2009-06-02
categories: 
  - "programming"
tags: 
  - "palindrome"
  - "project-euler"
---

Just to practice my C skills I've begun doing the [Project Euler](http://projecteuler.net/ "Project Euler") exercises in that language.

[Project 4](http://projecteuler.net/index.php?section=problems&id=4) asks what is the largest [palindromic number](http://en.wikipedia.org/wiki/Palindromic_number "Palindromic number") that can be expressed as the product of two 3-digit numbers. The answer is 906609 = 993 x 913.

Just for fun I modified my program to compute the largest integer that could be represented in C on my machine as the product of two integers. After about 3.5 hours, the glorious answer came back:

999900665566009999 = 999980347 x 999920317

And for the record, here is my program:

```
\#include 
\#include 

\#define MIN 100000000LL
\#define MAX 1000000000LL

typedef unsigned long long bigint;

int is_palindrome(char* str) {
  char* n = str + strlen(str) - 1;
  while (n > str) if (*str++ != *n--) return 0;
  return 1;
}

int main() {
  bigint product;
  bigint a,b;
  bigint largest = 0;
  char product_str[30];
  for (a = MAX-1; a > MIN; a--) {
    if (a\*a < largest) break;
    for (b = a; b > MIN; b--) {
      product = a*b;
      if (product < largest) break;
      sprintf(product_str, "%llu", product);
      if (is_palindrome(product_str)) {
        largest = product;
        printf("%llu x %llu = %llu\n", a, b, product);
        break;
      }
    }
  }
  return 0;
}

```
