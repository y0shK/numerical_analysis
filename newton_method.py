import numpy as np

def compute_poly(x): # x_i = [x_3, x_2, x_1, x_0, ...], where x_3 is coef of x**3

    """
    total = 0
    expo = len(x_i)
    for i in x_i:
        total += x_i * x_0 ** (expo-i) 
    """

    #p1 = x**4 - x**2 + x - 1
    #d1 = 4*x**3 - 2*x + 1

    p1 = 1/x
    d1 = (-1) * (1/(x**2))

    return p1, d1

def newtons_method(x_0, itercount):
    p_v, d_v = compute_poly(x_0)

    try:
        newtonval = x_0 - p_v / d_v
    except ZeroDivisionError:
        newtonval = 10000000000000 # FIXME put a better solution

    return newtonval

def iter_newton(x_0, itercount):
    
    for i in range(itercount):

        newt = newtons_method(x_0, itercount)   
        x_0 = newt

        # print(i, newt)

    return newt
    

#print(compute_poly(0))
#print(iter_newton(0, 2))
print(iter_newton(1, 50))
