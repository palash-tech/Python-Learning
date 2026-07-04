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
    for i in range(1,n):
        return n*(n-1)
n=int(input("Enter a number:"))
print(factorial(n))

