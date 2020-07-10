#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:52:05 2020

@author: ornwipa
"""

def load_skids(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain data
    in the form of comma-separated skid name, weight pair, and return a dictionary
    containing skid names as keys and corresponding weights as values.

    Parameters:  filename - the name of the data file as a string

    Returns:  a dictionary of skid name (string), weight (int) pairs
    """

    skid_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        skid_dict[line_data[0]] = int(line_data[1])
        
    return skid_dict