import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym

import helper_math as hm
import helper_diff_schemes as hds

xDat = np.linspace(-math.pi/4,math.pi/2,1000)
yDat = hm.moler_f(xDat)
poi = math.pi/4
flagPoint = hm.moler_f(poi)

plt.figure()
plt.plot(xDat,yDat, color='#F86B92',linewidth=3)
plt.plot(poi, flagPoint,'o',color='#84C5BB',markersize=10)
plt.title("y = exp(x)/((cos(x)^3 + (sin(x))^3)")
plt.xlim(-math.pi/4, math.pi/2)
plt.xticks([-math.pi/4,0,math.pi/4,math.pi/2])
plt.ylim(0,6)
plt.show()

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
print('power        h (step size)              complex step                centered difference')
for cInd, c in enumerate(reversed(np.arange(-16,0,dtype=np.float64))):
    hStep = 10 ** c
    cntrd = hds.centered_diff(poi, hStep, hm.moler_f)
    cmplxstp = hds.complex_step_diff(poi, hStep, hm.moler_f)
    print('-' + str(f"{int(abs(c)):02d}") + spcr + str("{:.15f}".format(hStep)) + spcr + str("{:.16f}".format(cmplxstp)) + spcr + str("{:.16f}".format(cntrd)))
    cntrdErr[cInd] = abs(cntrd - molerFunDiff)
    cmplxstpErr[cInd] = abs(cmplxstp - molerFunDiff)


# Error plot
plt.figure()
xH = 10 ** np.arange(-16,0,dtype=np.float64)
plt.plot(xH,cntrdErr, color='#FFA83A',linewidth=3,label='Centered')
plt.plot(xH,cmplxstpErr, color='#EA0504',linewidth=3,label='Complex step')
plt.title("Error for different differencing methods")
plt.ylim(10 ** -14, 10 ** 0)
plt.yscale("log")
plt.xscale("log")
plt.legend()
# plt.show()
