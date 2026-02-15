import numpy as np 

def fx(x):
    y = x**3 - np.sin(x)

    return y

def fdx(x):
    ydx = 3*(x**2) - np.cos(x)

    return ydx 

def root(x_0):

    """
    Root is a function that finds the root of equation x^3 - sin(x).

    input parameters:
    x_0 = initial guess for the root

    returns:
    x = actual root of the function
    count = after how many iterations we reached to the root

    
    """

    x= x_0 
    count = 0

    print(f"The value of x for {count} iteration is {x}")
    while abs(fx(x))>0.0000000001:
        print("=================")
        y = fx(x)
        ydx = fdx(x)
        x = x -y/ydx
        print(f"The value of x for {count} iteration is {x}")
        count+=1

    print(f"The root is {x}")

    return x,count
        