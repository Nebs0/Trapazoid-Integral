#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:33:51 2023

@author: nebiyousamuel
"""

def trap(f, a, b, n):
    """
    Calculate the trapezoid integral of a function f from a to b using n trapezoids.
    
    Parameters:
        f: The function to be integrated.
        a: The lower limit of the integral.
        b: The upper limit of the integral.
        n: The number of trapezoids used for approximation.
        
    Returns:
        The approximated integral value.
    """
    # Step 1: Calculate the width of each sub-interval
    delta_x = (b - a) / n
    
    # Step 2: Calculate the function values at end-points of sub-intervals
    x_values = [a + i * delta_x for i in range(n + 1)]
    y_values = [f(x) for x in x_values]
    
    # Step 3: Calculate the area of each trapezoid and sum them up
    integral = 0.5 * delta_x * (y_values[0] + y_values[-1])
    integral += sum(delta_x * y for y in y_values[1:-1])
    
    return integral

# Example usage:
# Define the function to be integrated, for example, f(x) = x^2
def f(x):
    return x**2

# Define the interval [a, b]
a = 0
b = 2

# Define the number of trapezoids
n = 1000

# Calculate the integral using trap function
result = trap(f, a, b, n)
print("Approximated integral:", result)
