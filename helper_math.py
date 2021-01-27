# Helper math functions for complex differentiation
import math
import numpy as np

def moler_f(xDat):
    # Moler function from https://blogs.mathworks.com/cleve/2013/10/14/complex-step-differentiation/
    # Link active as of 1/19/2021
    yDat = np.divide(np.exp(xDat),((np.cos(xDat)) ** 3 + (np.sin(xDat)) ** 3))

    return yDat
