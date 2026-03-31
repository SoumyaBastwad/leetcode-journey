# the tribonacci number: such that each number is the sum of the three preceding ones, starting from 0 ,1 and 1. 
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
    

     
    
