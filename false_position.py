import numpy as np

def fn_x1(x):
    return x**3 - 2*x - 2

def fn_x2(x):
    return np.exp(x) + x - 7

def fn_x3(x):
    return np.exp(x) + np.sin(x) - 4

"""
for i in range(1, 3):
    print('fn_x - iteration' + str(i))
    print(fn_x1(i))
    print(fn_x2(i))
    print(fn_x3(i))
"""

def fp(fn_x, a, b):
    top = a * fn_x(b) - b * fn_x(a)
    bottom = fn_x(b) - fn_x(a)

    if bottom != 0:
        return top/bottom
    else:
        return 10*10 # heuristic for unbounded int - more than we need/expect

def call_fp(fn_x, a, b, iter_counter=1):
    # returns a_(n+1), b_(n+1)
    c_1 = fp(fn_x, a, b)
    
    if fn_x(c_1) * fn_x(a) < 0:
        b = c_1
    else:
        a = c_1

    print('c value of iter ' + str(iter_counter) + ': ' + str(c_1))

    return [a, b]

"""
print("\neval 2a. c val")
c_2a = fp(fn_x1, 1, 2)
print(c_2a)

print(fn_x1(c_2a))

c2_a2 = fp(fn_x1, 1.6, 2)
print(c2_a2)
print(fn_x1(c2_a2))
"""

a2, b2 = call_fp(fn_x2, 1, 2)
print(a2, b2)
a3, b3 = call_fp(fn_x2, a2, b2, iter_counter=2)

print("\n")

a2_2, b2_2 = call_fp(fn_x3, 1, 2)
print(a2_2, b2_2)
a3_2, b3_2 = call_fp(fn_x3, a2_2, b2_2, iter_counter=2)
