# Differencing schemes
import numpy as np
import sympy as sym

import helper_math as hm


def centered_diff(xDat,hStep,fHandle):
    cDiff = (fHandle(xDat+hStep) - fHandle(xDat-hStep))/(2*hStep)

    return cDiff

def complex_step_diff(xDat,hStep,fHandle):
    csDiff = np.imag(fHandle(xDat+1j*hStep)/hStep)

    return csDiff

def sym_diff(xDat,soi,fHandle):
    #symbol of interest
    symDiff = sym.diff(fHandle,soi)
    symEvalDiff = symDiff.subs(soi,xDat)

    return symEvalDiff
