def eval_poly(coef_list, x):
    expo = len(coef_list) - 1
    total = 0
    for i in range(len(coef_list)-1):
        total += coef_list[i] * (x ** (expo-i))
        print(total)

    # get rid of x^0 term
    total += coef_list[-1]

    print("\nTotal end")
    return total

print(eval_poly([1, 1, 1, 0], 1)) # passes test case - x**3 + x**2 + x at x=1 is 3

# expect -1, receives -1
print(eval_poly([5, -8, 0, 4, -1], 0)) 

# expects 8, gets 8
print(eval_poly([5, -8, 0, 4, -1], -1))

print(eval_poly([20, -24, 0, 4], -1))
