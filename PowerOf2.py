# ispowerof2 
# in that input taken as integer n and if that n is a power of 2 it's showing true
#  if n is not a power of 2 it's showing False
n=int(input("Enter the n value a integer:"))
if n<=0:
     print(False)        # n is negative or o 
while n%2==0:
    n=n//2
print(n==1)             # if n is power of 2