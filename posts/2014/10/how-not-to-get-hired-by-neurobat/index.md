---
title: "How not to get hired by Neurobat"
date: 2014-10-16
---

When I recruit software engineers I always ask them to first take a short online programming test. Following a [recommendation from Jeff Atwood](http://blog.codinghorror.com/how-to-hire-a-programmer/), we use [Codility](https://codility.com) as an online programming testing tool.

The goal of this test is _not_ to assess whether you are a good programmer. I believe there's more to software engineering than merely being able to code a simple algorithm under time pressure. The goal is to filter out self-professed programmers who, in fact, can't program. And [according to Jeff Atwood again](http://blog.codinghorror.com/why-cant-programmers-program/), these people are uncomfortably numerous.

During our current recruitment round we got an angry email from a candidate who performed less than stellarly:

> Thank you for your e-mail, outlining that you don't wish to proceed further with my application.
> 
> I fully understand your position, though I feel that your online testing system is flawed. I have been programming C and C++ on and off for 25 years, so I guess if I don't know it, then nobody does.
> 
> It's simply not realistic to test people under such artificial conditions against the clock, relatively unprepared and in a strange development environment.
> 
> Nevertheless, I'm glad to have experienced the test, and it has helped resolve my focus on exactly the type of jobs that I don't wish to pursue, and the types of people I don't wish to work with.

This is from a candidate who, according to his resume, is an "experienced IT professional" with 10+ years of experience in C/C++, Javascript, Perl, SQL, and many others. Let's have a look at the programming test and his solution.

The test consists in two problems, rated "Easy" and "Medium" respectively by the Codility platform. The candidates have one hour to carry out the test. They can take the test only once, but whenever they want. They are given the opportunity to practice first.

Here is the gist of the first, "Easy" problem:

> Write a function `int solution(string &S);` that, given a non-empty string S consisting of N characters, returns 1 if S is an anagram of some palindrome and returns 0 otherwise.

For example, `"dooernedeevrvn"` is an anagram of the palindrome `"neveroddoreven"`. A minute of reflexion should be enough to realise that a string is an anagram of a palindrome if and only if not more than one letter occurs an odd number of times.

Here is Mr. If-I-don't-know-it-nobody-does's solution in toto:

// you can use includes, for example:
// #include 
#include 
#include 

using namespace std;

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(string &S) {
    // --- string size ---
    int N = S.size();
    char \*str;
    bool even;
    vector cnt(N,0);
    
    // --- even no of letters? ---
    if (N % 2)
       even = false;
    else
       even = true;
       
    // --- for faster access ---
    str = (char \*)S.c\_str();

    
    // --- count each letter occurence ---
    
    // --- for each letter and check letter count of all others ---
    for (int i=0;i
        // --- exists at least once ---
        cnt\[i\]++;

        // --- check all other positions ---
        for (int j=0;j

Never mind that this solution has O(n2) time complexity and O(n) space complexity (the test asked for O(n) and O(1) respectively), it is also wrong. It returns 0 for "zzz". But perhaps the use of C-style `char*` "for faster access" will compensate for the algorithmic complexity.

Let's have a look at another solution proposed by a self-titled senior programmer:

```
// you can use includes, for example:
// #include 

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;
#define NUM_ALPH 30
#define a_ASCII_OFFSET 97

int solution(string &S) {
    // write your code in C++11
    //std::map letters_to_counts;
    //std::map::iterator it;
    //int len = S.size;
    
    //string alph = "abcdefghijklmnopqrstuvwxyz";
    
    int count[NUM_ALPH]={};  // set to 0
    for(int i==0; i< len; i++)
    {
        char ch= S[i];
        int index= (int)ch;  // cast to int 
        count[index-a_ASCII_OFFSET]^=1;  //toggles bit, unmatched will have 1,
    }
    int sum_unmatched=0;
    for(int i=0; i < NUM_ALPH; i++)
    {
        sum_unmatched+=count[i];
        
    }
    if(sum_unmatched<=1)return 1;
    return 0;
}
// did not have time to polish but the solution logic should work

```

This one doesn't even compile, but fortunately the "logic should work". I'm sure it will, being written as it is in C, and with helpful comments too ("cast to int", really?)

I have several more examples like this one, all coming from candidates who applied to a job ad where I made the mistake to ask for a Senior Software Engineer.

Compare this with a contribution from one who applies to a non-senior position:

```
#include 
#include 

map createDictionary(string & S) {
    map result;
    for (char ch : S) {
        ++ result[ch];
    }
    return result;
}

int solution(string & S) {
    map dictionary = createDictionary(S);
    int numEvens = count_if(dictionary.begin(), dictionary.end(), 
        [] (const pair & p) { return p.second % 2 == 1; });
        
    return numEvens < 2? 1: 0;
}

```

Not only is this code correct, it also reads well and demonstrates knowledge of the recent additions to the C++ language. And this comes from a relatively younger candidate, who came as far as the in-person interview.

Again, software engineering is about much more than merely programming skills. This test is only the first filter; when the candidates are invited for the interview I ask them to explain their reasoning and their code to a non-programmer, to see how their communication skills stack up. Only then will we consider making them an offer.
