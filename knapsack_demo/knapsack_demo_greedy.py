#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:57:50 2020

@author: ornwipa
"""

from knapsack_demo_partition import get_partitions
from knapsack_demo_load_data import load_skids

def greedy_transport(skids, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of skids that attempts to
    minimize the number of trips needed to transport all the skids. 
    The greedy heuristic should follow the following method:

    1. As long as the trip can fit another skid, add the largest skid that fits
    2. Once the trip is full, begin a new trip to transport the remaining skids

    Parameters:
    skids - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the fixed-size trailer (one int)
    
    Returns:
    A list of lists, with each inner list containing the names of skids transported 
    on a particular trailer and the overall list containing all the trailers
    """
    
    trips = []
    skids_left = skids.copy() # not mutate the given dictionary of skids
    
    while len(skids_left) != 0:
        trip = []
        capacity_left = limit
        try:
            smallest = min(skids_left.values())
        except ValueError:
            smallest = 0
        
        while capacity_left >= smallest and len(skids_left) != 0:
            weight_sorted = sorted(skids_left.values(), reverse=True) # largest
            
            for w in weight_sorted: # search for next weight allowed on the trip
                if w <= capacity_left:
                    next_weight = w
                    break
            
            for skid in skids_left.keys(): # search for corresponding skid
                if skids_left[skid] == next_weight:
                    next_skid = skid
                    break
                    
            if next_skid in trip:
                break
            else:
                trip.append(next_skid)    
                capacity_left -= skids_left[next_skid]         
                del(skids_left[next_skid])            
            
        trips.append(trip)
    return trips

# Uncomment the following code and run this file to test the function.
# print(greedy_transport(load_skids("demo_data.txt"), 12))