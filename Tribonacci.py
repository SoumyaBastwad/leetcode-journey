n=int(input("enter a integer:"))
t=[0,1,1]
if n<0:
    print("invalid number")
elif n<3:
    print(t[n])
else:
    for i in range(3,n+1):
        t[0],t[1],t[2]=t[1],t[2],sum(t)
    print(t[2])
    

     
    