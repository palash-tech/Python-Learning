print("Find even numbers using filter function")
l=[2,3,4,6,5,8]
newl=filter(lambda x:x%2==0,l)
print(list(newl))

print("Find odd numbers using filter function")
def odd(x):
    if x%2!=0:
        return x
l1=[3,2,5,7,6]
new_l1=filter(odd,l1)
print(list(new_l1))

print("Find numbers less than 50 using filter function")
l2=[23,40,30,55,60,45]
new_l2=filter(lambda x:x<50,l2)
print(list(new_l2))

print("Names longer than 5 characters")
l3=["Palash","Rahul","Aman","Piyush","Shubham"]
new_l3=filter(lambda x:len(x)>5,l3)
print(list(new_l3))