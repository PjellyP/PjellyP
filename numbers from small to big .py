x = int(input("Enter the number: "))
k = int(input("Enter the number: "))
y = int(input("Enter the number: "))
if x>k>y :
    print(y,k,x)
elif k>x>y :
    print(y,x,k)
if y>k>x :
    print(x,k,y)
elif x>y>k :
    print(k,y,x)
if k>y>x :
    print(x,y,k)
if y>x>k :
    print(k,x,y)