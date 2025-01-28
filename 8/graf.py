import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

point_forkn = float(input('Точка x0 для построения касательной и нормали на промежутке от 1 до 5: '))
start = float(input('промежуток для касательного расслоения [x0,x1] x0 на промежутке от 1 до 5: '))
end = float(input('x1: '))

x = np.arange(1,5,0.01)
xk = np.arange(1,5,0.25)
def f(x):
    y = (2*x-3)**2 * np.sin(x**2 +2)
    return y

def maximum(x, m = 0):
    max_ind = -1
    for ind, i in enumerate(x):
        current_value = f(i)
        if current_value > m:
            m = current_value
            max_ind = ind
    return m, x[max_ind]
def minimum(x, m = np.inf):
    min_ind = -1
    for ind, i in enumerate(x):
        current_value = f(i)
        if current_value < m:
            m = current_value
            min_ind = ind
    return m, x[min_ind]


def df(x):
    dy = 4*np.sin(x**2 +2) * (2*x -3) +2*x * (4*x**2-12*x +9)* np.cos(x**2 +2)
    return dy
def ddf(x):
    ddy = 8*x*np.cos(x**2 + 2)*(2*x -3)+8*np.sin(x**2+2)+(24*x**2-48*x+18)*np.cos(x**2+2)-4*x**2 * np.sin(x**2 +2)*(4*x**2 - 12*x+9)
    return ddy
def kf(x,x0):
    yk = f(x0) + df(x0) *(x-x0)
    return yk
def nf(x,x0):
    yn = f(x0) - 1/df(x0)*(x-x0)
    return yn

def forin(z):
    return np.sqrt(1+(4*np.sin(z**2 +2) * (2*z -3) +2*z * (4*x**2-12*z +9)* np.cos(z**2 +2))**2)

maxi = maximum(x)
mini = minimum(x)



common = plt.subplot(2,3,1)
plt.plot(x,f(x),x,kf(x,point_forkn),x,nf(x,point_forkn))
plt.plot([maxi[1]],[maxi[0]],'o',color = '#000')
plt.plot([mini[1]],[mini[0]],'o',color = '#000')
dcommon = plt.subplot(2,3,2)
plt.plot(x,f(x))
ddcommon = plt.subplot(2,3,3)
plt.plot(x,ddf(x))
pl_rass = plt.subplot(2,1,2)
for i in xk:
    for x0 in xk:
        if start <= x0 <= end:
            plt.plot(xk,kf(xk,x0),'--r')
plt.plot(x,f(x))

plt.gcf().set_facecolor('#808080')
common.grid()
dcommon.grid()
ddcommon.grid()
pl_rass.grid()

plt.show()
