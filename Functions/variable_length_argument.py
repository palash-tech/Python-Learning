def sum(*numbers):
    total=0
    for i in numbers:
        total=total+i
    return total
print(sum(30,40))
print(sum(10,40,55,6))
print(sum(30,60,200))