import numpy as np
from scipy.optimize import minimize

K=6
L=5
def rosen(x):
    #"""The Rosenbrock function"""
    #return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
    """The Romeo function"""
    return sum (((K*L*e**(-K*x-x0))/(1+e**(-K*x-x0))**2)**2 - x**2)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xatol': 1e-8, 'disp': True})

print(res.x)

