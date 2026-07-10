import math
def area_circle(r):
    print(math.pi*r*r)
def area_rectangle(w,h):
    print(w*h)
def is_even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
area_circle(9)
area_rectangle(2,5)
is_even(6)
print(factorial(7))