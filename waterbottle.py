# there are numBottle water bottles that are initially full of water. you can exchange numExchange empty
# water bottles from the market with one full water bottle
# the operation of drinking a full water bottle turns it into an empty bottle
# Given the two integers numBottle and numExchange , return the mximum number of water bottles you can drink.

numBottle=int(input("Enter the number of intially fulled water bottles:"))
numExchange=int(input("Enter how many number of bottles we return to getone fulled water bottle:"))
consumed=0
while(numBottle>=numExchange):
    consumed+=numExchange
    numBottle-=numExchange
    numBottle+=1
print(consumed+numBottle)
