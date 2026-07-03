def add(a,b):
    sum=a+b
    print(sum)
def sub(a,b):
    subs=a-b
    print(subs)
def multiplication(a,b):
    mult=a*b
    print(mult)
def division(a,b):
    div=a/b
    print(div)
x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number:"))
print("Enter 1 for Addition")
print("Enter 2 for substraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
num=int(input("Enter a number:"))
if num==1:
    add(x,y)
elif num==2:
    sub(x,y)
elif num==3:
    multiplication(x,y)
else:
    division(x,y)

