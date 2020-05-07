def cal(k,y,z):
    for i in reversed(range(k+1)):
        if i==1:
            return z-round(y)
        dtc=z/(2*i-1)
        y=y-dtc




x=int(input())
y=int(input())
z=int(input())
k=int(x/z)
print(cal(k,y,z))
