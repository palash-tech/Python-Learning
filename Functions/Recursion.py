"""print("Print number from 1 to n")
def print_num(n):
    if n==0:
        return
    print_num(n-1)
    print(n)
    
n=int(input("Enter a number:"))
print_num(n)

print("Factorial recursion")

def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a * fact(a-1)
a=int(input("Enter a nummber:"))
print(fact(a))"""

print("Fibonacci serier")
def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("Enter number:"))
for i in range(n):
    print(fibo(i),end=" ")

