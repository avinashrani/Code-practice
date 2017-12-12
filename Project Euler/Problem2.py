#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:36:46 2017

@author: avinashrani
Project Euler Problem 2
"""

total = 0
fib1 = 1
fib2 = 2

while fib1<4000000 or fib2<4000000:    
    if fib1%2 == 0:
        total += fib1
    
    if fib2%2 == 0:
        total += fib2
    
    temp = fib1 + fib2
    temp2 = temp + fib2
    
    fib1 = temp
    fib2 = temp2

print (total)

        
    
    

