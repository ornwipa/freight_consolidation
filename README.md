# Freight Consolidation Problem

A company has to transport goods/skids on a truck/trailer from a single source to a single destination on a fixed pre-determined route, and would like to minimize the number of trips.

This problem is formalized as a knapsack problem. Two solution techniques used are:

- Brute-force algorithm by enumrating all possible ways of dividing the skids into groups for separate trips and selecting the allocation with the least number of trips without any trip exceeding the weight limits.

- Greedy heuristic by adding the largest skid to the current trip until no longer able to add more any skid before beginning a new trip.

The next problem to be solved is how to arrange the skids to fit in the 3D container of standard size.
