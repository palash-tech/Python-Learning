print("Greet function")
def greet(name):
    print("Hello",name)
name=input("Enter name:")
greet(name)

print("Sum of two number ")
def add(a,b):
    
    sum=a+b
    return sum
a=int(input("Enter a number"))
b=int(input("Enter another number"))
print(add(a,b))

print("Largest number ")
def largest(c,d):
   
    if c>d:
        return c
    else:
 
       return d
c=int(input("Enter a number"))
d=int(input("Enter another number"))
print(largest(c,d))

print("Even odd funtion ")
def is_even(n):
    if n%2==0:
        return "number is even"
    else:
        return "number is odd"
n=int(input("Enter a number"))
print(is_even(n))