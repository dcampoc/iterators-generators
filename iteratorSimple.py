# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:04:32 2019

@author: damian.campo
"""

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for item in flash:
    print(item)

# Create an iterator for flash: superspeed
superspeed = iter(flash)

# Print each item from the iterator
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
