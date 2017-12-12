#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:26:45 2017

@author: avinashrani
Project Euler Problem-1
"""
total = 0
for n in range (1000):
    if n%3 == 0 or n%5==0:
        total += n
        
print(total)
        

