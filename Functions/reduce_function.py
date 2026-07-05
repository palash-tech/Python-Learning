from functools import reduce
print("Sum of all numbers")
l1=[2,4,6,8]
new_l1=reduce(lambda x,y:x+y,l1)
print(new_l1)

print("product of all numbers")
def product(x,y):
    return x*y
l2=[2,3,4]
new_l2=reduce(product,l2)
print(new_l2)

print("Find the Maximum number")
l3=[10,45,30,80,25]
new_l3=reduce(lambda x,y:x if x>y else y,l3)
print(new_l3)