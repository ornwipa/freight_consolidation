#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:17:26 2020

@author: ornwipa
"""
            
def partitions(set_):
    """ This function is adapted from codereview.stackexchange.com. """
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    """ This helper function fetches all of the available partitions. """
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

# Uncomment the following code and run this file for visualization.
# for item in (get_partitions(['a','b','c','d'])):
#    print(item)