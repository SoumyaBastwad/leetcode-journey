# the Fibonacci sequence:such that each number is the sum of the two preceding ones, starting from 0 and 1.
def fib(n):
    a=0
    b=1
    if n<=0:
        print("invalid number")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input("enter a integer:"))
fib(n)



