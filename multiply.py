# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/31/2022
#
# Write a recursive function named
# multiply that takes two positive integers as parameters and returns the product of those two numbers (the result
# from multiplying them together). Your program should not use multiplication - it should find the result by using
# addition.

def multiply(multiplicand, multiplier):
    """Gives multiplication value by using addition method."""
    # Multiplier is different from one.
    if multiplier == 1:
        # If multiplier is one, the result will be the multiplicand itself.
        return multiplicand
    # performs multiplication by addition.
    return multiply(multiplicand, multiplier-1) + multiplicand
