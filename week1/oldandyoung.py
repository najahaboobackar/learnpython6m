x=int(input("enter the age"))
y=int(input("enter the age"))
z=int(input("enter the age"))
if x>y and x>z:
    print("the age of x is greater",x)
    if y<z:
        print("younger is y",y)
    else:
        print("younger is",z)
elif y>x and y>z:
    print("the age of y",y)
    if x<z:
        print("the younger is",x)
    else:
        print("the younger",z)
else:
    print("the greater age is",z)
    if y<x:
        print("the younger is",y)
    else:
        print("the younger",x)
