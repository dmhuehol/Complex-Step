import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym

import helper_math as hm
import helper_diff_schemes as hds

import time

xDat = np.linspace(-math.pi/4,math.pi/2,1000)
yDat = hm.moler_f(xDat)
poi = math.pi/4
flagPoint = hm.moler_f(poi)

# Evaluate true derivative
xSym = sym.Symbol('x')
molerFun = np.divide(sym.exp(xSym),((sym.cos(xSym)) ** 3 + (sym.sin(xSym)) ** 3))
molerFunDiff = hds.sym_diff(poi, xSym, molerFun)
print("Exact value of derivative at point of interest (evaluated symbolically) is: " + str(molerFunDiff))

spcr = '          '
cntrdErr = np.empty(16)
cntrdErr[:] = np.nan
cmplxstpErr = np.empty(16)
cmplxstpErr[:] = np.nan
# print('power        h (step size)              complex step                centered difference')
t = time.time()
# for cInd, c in enumerate(reversed(np.arange(-16,0,dtype=np.float64))):
hStep = 10 ** -10
cntrd = hds.centered_diff(poi, hStep, hm.moler_f)
    # cmplxstp = hds.complex_step_diff(poi, hStep, hm.moler_f)
    # print('-' + str(f"{int(abs(c)):02d}") + spcr + str("{:.15f}".format(hStep)) + spcr + str("{:.16f}".format(cmplxstp)) + spcr + str("{:.16f}".format(cntrd)))
    # cntrdErr[cInd] = abs(cntrd - molerFunDiff)
    # cmplxstpErr[cInd] = abs(cmplxstp - molerFunDiff)
elapsed = time.time() - t

t2 = time.time()
# for cInd, c in enumerate(reversed(np.arange(-16,0,dtype=np.float64))):
hStep = 10 ** -10
    # cntrd = hds.centered_diff(poi, hStep, hm.moler_f)
cmplxstp = hds.complex_step_diff(poi, hStep, hm.moler_f)
    # print('-' + str(f"{int(abs(c)):02d}") + spcr + str("{:.15f}".format(hStep)) + spcr + str("{:.16f}".format(cmplxstp)) + spcr + str("{:.16f}".format(cntrd)))
    # cntrdErr[cInd] = abs(cntrd - molerFunDiff)
    # cmplxstpErr[cInd] = abs(cmplxstp - molerFunDiff)
elapsed2 = time.time() - t2

print('Time for centered difference: ' + str(elapsed))

print('Time for complex step: ' + str(elapsed2))
