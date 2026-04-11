---
title: "Saikoro game engine in Lisp"
date: 2011-05-20
categories: 
  - "programming"
tags: 
  - "game"
  - "lisp"
  - "saikoro"
---

Here at Neurobat we consecrate one day per sprint as a \*Lab Day\*, i.e. a day when, not unlike what Google does, we are free to work on whatever we want.

Today was Lab Day and I took the opportunity to brush up my Lisp skills by writing a game, inspiring myself heavily from Conrad Burski's wonderful book [Land of Lisp](http://www.amazon.com/gp/product/1593272812/ref=as_li_ss_tl?ie=UTF8&tag=compandsmarbu-20&linkCode=as2&camp=217145&creative=399349&creativeASIN=1593272812)![](images/ir), which will teach you the necessary Lisp skills for the most important programming gig ever, that is, writing games.

I wrote a game engine for the [Saikoro](http://boardgamegeek.com/boardgame/27813/saikoro) boardgame, a game simple enough to be amenable to the kind of AI described in the book. Without doing any major kind of optimization, the computer will play a perfect game on a 4 x 4 board by computing exhaustively a tree of all possible games from a starting position.

Here is what a typical game session looks like:

```
$ sbcl --load saikoro.lisp
; snip some noise
Current player: A
| A[ 0] 3[ 1] 3[ 2] 2[ 3] |
| 1[ 4] 4[ 5] 2[ 6] 2[ 7] |
| 3[ 8] 4[ 9] 4[10] 2[11] |
| 1[12] 3[13] 4[14] B[15] |
Choose your move: 
1. 0 -> 4 
2. 0 -> 10 
3. 0 -> 1 
4. 0 -> 5 
2
Current player: B
| 0[ 0] 3[ 1] 3[ 2] 2[ 3] |
| 1[ 4] 4[ 5] 2[ 6] 2[ 7] |
| 3[ 8] 4[ 9] A[10] 2[11] |
| 1[12] 3[13] 4[14] B[15] |
Current player: A
| 0[ 0] 3[ 1] 3[ 2] 2[ 3] |
| 1[ 4] B[ 5] 2[ 6] 2[ 7] |
| 3[ 8] 4[ 9] A[10] 2[11] |
| 1[12] 3[13] 4[14] 0[15] |
Choose your move: 
1. 10 -> 1 
2. 10 -> 7 
2
Current player: B
| 0[ 0] 3[ 1] 3[ 2] 2[ 3] |
| 1[ 4] B[ 5] 2[ 6] A[ 7] |
| 3[ 8] 4[ 9] 0[10] 2[11] |
| 1[12] 3[13] 4[14] 0[15] |
Current player: A
| 0[ 0] 3[ 1] 3[ 2] 2[ 3] |
| B[ 4] 0[ 5] 2[ 6] A[ 7] |
| 3[ 8] 4[ 9] 0[10] 2[11] |
| 1[12] 3[13] 4[14] 0[15] |
Choose your move: 
1. 7 -> 1 
1
Current player: B
| 0[ 0] A[ 1] 3[ 2] 2[ 3] |
| B[ 4] 0[ 5] 2[ 6] 0[ 7] |
| 3[ 8] 4[ 9] 0[10] 2[11] |
| 1[12] 3[13] 4[14] 0[15] |
Current player: A
| 0[ 0] A[ 1] 3[ 2] 2[ 3] |
| 0[ 4] 0[ 5] 2[ 6] 0[ 7] |
| 3[ 8] 4[ 9] 0[10] 2[11] |
| 1[12] B[13] 4[14] 0[15] |
Choose your move: 
1. 1 -> 6 
2. 1 -> 3 
3. 1 -> 2 
3
Current player: B
| 0[ 0] 0[ 1] A[ 2] 2[ 3] |
| 0[ 4] 0[ 5] 2[ 6] 0[ 7] |
| 3[ 8] 4[ 9] 0[10] 2[11] |
| 1[12] B[13] 4[14] 0[15] |
Current player: A
| 0[ 0] 0[ 1] A[ 2] 2[ 3] |
| 0[ 4] 0[ 5] 2[ 6] 0[ 7] |
| 3[ 8] 4[ 9] 0[10] 2[11] |
| B[12] 0[13] 4[14] 0[15] |
B wins!
* (quit)
```

As you can see the UI is very rudimentary for the moment but I wanted to concentrate on getting the AI right first. Next I plan to optimize the AI, and make it work with a non-exhaustive game tree so it would work on larger boards.

If you're interested in trying it out, feel free to [clone my repository](https://github.com/dlindelof/saikoro).
