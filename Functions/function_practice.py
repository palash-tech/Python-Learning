def greet(name):
    print("Hello",name)
name=input("Enter name:")
greet(name)

def add(a,b):
    
    sum=a+b
    return sum
a=int(input("Enter a number"))
b=int(input("Enter another number"))
print(add(a,b))

def largest(c,d):
   
    if c>d:
        return "c is largest number"
    else:
 
       return "d is largest number"
c=int(input("Enter a number"))
d=int(input("Enter another number"))
print(largest(c,d))

def is_even(n):
    if n%2==0:
        return "number is even"
n=int(input("Enter a number"))
print(is_even(n))