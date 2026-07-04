add=lambda a,b:a+b
print(add(20,30))

square=lambda x:x*x
print(square(5))

largest_value=lambda a,b,c:a if a>b and a>c else b if b>c else c
print(largest_value(10,25,15))