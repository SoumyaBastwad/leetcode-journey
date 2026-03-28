#palindrome number
#A palindrome number is a number that reads the same forward and backward.
x=input("enter a integer number")
rev=""
for i in x:
    rev=i+rev
if rev==x:
    print("the given number is palindrome")
else:
    print("the given number is not a palindrome")
