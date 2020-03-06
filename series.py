#This is the code for series.py and all
#the general principle is using recursion for the function
#first is the fib(n) function where the first terms are placed as the stop points in the recursion
def fib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
assert fib(3) == 1
assert fib(7) == 8
#same thing for the lucas(n) function
def lucas(n):
    if n <= 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
assert lucas(1) == 2
assert lucas(2) == 1
assert lucas(5) == 7
def series(n,a,b):
    if (a == 0 and b == 0):
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    else:
        if n <= 1:
            return a
        elif n == 2:
            return b
        else:
            return  series(n-1,a,b) +   series(n-2,a,b)
assert series(3,2,1) == 3
