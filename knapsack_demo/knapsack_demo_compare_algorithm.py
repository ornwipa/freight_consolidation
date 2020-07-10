#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:17:00 2020

@author: ornwipa
"""

import time
from knapsack_demo_load_data import load_skids
from knapsack_demo_bruteforce import bruteforce_transport
from knapsack_demo_greedy import greedy_transport

def compare_transport_algorithms():
    """
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.
    """

    skids = load_skids("demo_data.txt")
    limit = 10
    
    print("Greedy heuristics")
    start = time.time()
    print("Number of trips: " + str(len(greedy_transport(skids, limit))) )
    end = time.time()
    print("Computing time: " + str(end - start) + " seconds")
    
    print("Brute force")
    start = time.time()
    print("Number of trips: " + str(len(bruteforce_transport(skids, limit))) )
    end = time.time()
    print("Computing time: " + str(end - start) + " seconds")

# Uncomment the following code and run this file to test the function.
# compare_transport_algorithms()