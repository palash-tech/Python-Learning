num=int(input("Eneter a number:"))
original=num

sum=0
while num>0:
    digit=num%10
   
    num=num//10
    cube=digit**3
    sum=sum+cube
if original==sum:
    print("Number is amrstronge")
else:
    print("Number is not")