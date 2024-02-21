# secant_method
# x_(n+1) = x_n - (f(x_n)(x_n - x_(n-1)))/(f(x_n) - f(x_(n-1))

import numpy as np

def fn_x2(x):
    return np.exp(x) + x - 7

def fn_x3(x):
    return np.exp(x) + np.sin(x) - 4

def secant(fn_arg, x_n, x_nminus):
    div_term = (fn_arg(x_n) * (x_n - x_nminus))/(fn_arg(x_n) - fn_arg(x_nminus))
    x_nplus = x_n - div_term
    return x_nplus

#print(fn_x(2))
print("part b")

bx_2 = secant(fn_x2, 2,1)
print(bx_2)

bx_3 = secant(fn_x2, bx_2, 2)
print(bx_3)

print("\npart c")

cx_2 = secant(fn_x3, 2,1)
print(cx_2)

cx_3 = secant(fn_x3, cx_2, 2)
print(cx_3)
