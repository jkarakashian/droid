#!/usr/bin/env python
 
import string
import random
 
"""Generates a random droid name!"""
 
def rand_number():
    return random.choice(string.digits)
 
 
def rand_letter():
    return random.choice(string.ascii_uppercase)
 
 
def rand_char():
   if random.randint(1,2) % 2:
       return rand_number()
   return rand_letter()
 
 
formats = ['x-xxx', 'xx-xx', 'xxx-x']
format = random.choice(formats)
name = ''.join([rand_char() if c == 'x' else c for c in format])
print name
