print("Square function")
def square(n):
    return n**2
n=int(input("Enter a number:"))
print(square(n))

print("cube function")
def cube(d):
   return d**3
d=int(input("Enter a number:"))
print(cube(d))

print("maximum function")
def maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a,b,c=map(int,input("Enter numbers:").split())
print(maximum(a,b,c))

print("factorial function")
def factorial(n):
    if n==0 or n==1:
        return 1
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("Enter a number:"))
print(factorial(n))

print("Exponential function")
def power(b,e):
    return b**e
base=int(input("Enter base value:"))
exponent=int(input("Enter exponent value:"))
print(power(base,exponent))