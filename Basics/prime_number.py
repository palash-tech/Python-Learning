num=int(input("Enter a number:"))
prime=True
if num<2:
    print("number is not prime")
else:
    for i in range(2,num):
        if num%i==0:
             prime=False
             break
if prime==False:
    print("Number is not prime")
else:
    print("number is prime")