#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:31:18 2020

@author: ornwipa
"""

from knapsack_demo_partition import get_partitions
from knapsack_demo_load_data import load_skids

def bruteforce_transport(skids, limit=10):
    """
    Finds the allocation of skids that minimizes the number of trips or trailers
    via brute force.  The algorithm should follow the following method:

    1. Enumerate all possible ways that skids can be divided for separate trips.
    2. Select the allocation that minimizes the number of trips without making 
        any trip that does not obey the weight limitation.

    Parameters:
    skids - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the fixed-size trailer (one int)
    
    Returns:
    A list of lists, with each inner list containing the names of skids transported 
    on a particular trailer and the overall list containing all the trailers
    """
    
    skids_list = list(skids.copy()) # not mutate the given dictionary of skids

    min_no_trip = len(skids_list) # set max number of trips = number of skids
    
    for skids_divided in get_partitions(skids_list):
        
        feasible = True
        for trip in skids_divided:
            if sum(skids[skid] for skid in trip) > limit:
                feasible = False
                break
            
        if feasible and len(skids_divided) < min_no_trip:
            min_no_trip = len(skids_divided)
            out = skids_divided
            break
        
    return out

# Uncomment the following code and run this file to test the function.
# print(bruteforce_transport(load_skids("demo_data.txt"), 12))