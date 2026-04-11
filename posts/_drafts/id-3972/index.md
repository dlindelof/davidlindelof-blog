---
title: "Representing N-dimensional grids"
draft: true
---

Many programming problems deal with a two-dimensional grid. A programming interview I recently took, for example, had a sparse rectangle NxM grid of non-negative integers, the 0 cells representing water and sets of positive integers representing islands: ...

 The problem consisted in finding the most valuable island, where the value of an island is the sum of all its cells.  It is tempting and natural to use a two-dimensional array to represent this map:

 int\[\]\[\] map;

 That makes it easy to compute, say, the total value of a cell and its neighbors: 

int valueOfCellAndNeighbors(int row, int col) { ...} 

This function will feature one pair of if statements per map dimension. If we want to generalise this to an arbitrary number of dimensions, we'll either have to resort to template programming or think of something more clever. 

I generally use a one-dimensional array to represent a two-dimensional map. Let's see if that approach helps us here by trying it on a few small dimensions. 

N=0: single cell, no neighbors are possible

 N=1: a cell array. Each cell can have at most two neighbors. If i is the index into the array, then the neighbors are found by

(I > 0 ? I-1: Na) and (I < N-1?...)

 N=2: a two-dimensional map. A cellar row I and column j is stored at position I + NCOL \* j. Each ell cn have at most 4 neighbors, fond by GENERALIZED CODE AS ABOVE
