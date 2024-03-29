# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:50:19 2019

@author: damian.campo
"""

mutants = ['charles xavier',
 'bobby drake',
 'kurt wagner',
 'max eisenhardt',
 'kitty pryde']

aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']

powers = ['telepathy',
 'thermokinesis',
 'teleportation',
 'magnetokinesis',
 'intangibility']


# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants,aliases,powers))

# Print the list of tuples (visualization purposes)
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants,aliases,powers)

# Print the zip object (object that will be unpacked by using a 'for')
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1,value2,value3 in mutant_zip:
    print(value1, value2, value3)
    

##### SECOND EXERSIZE #########
    
print('Second exersize'.upper)

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2, they are tuples
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(list(result1) == mutants)
print(list(result2) == powers)