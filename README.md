# Freight Consolidation Problem

A company has to transport goods/skids on a truck/trailer from a single source A to a single destination B on a fixed route C, and would like to minimize the number of trips.

This problem is foramalized as a knapsack problem. Two solution techniques used are:

- Brute-force algorithm by enumrating all possible ways of dividing all skids for separate trips and selecting the allocation with the least number of trips without any trip exceeding the weight limits.

- Greedy heuristic by adding the largest skid to the current trip until no longer able to add any before beginning a new trip.
