"""
Run python autograder.py 
"""

def average(priceList):
    "Return the average price of a set of fruit"
    "*** YOUR CODE HERE ***"
    priceList=list(set(priceList))
    sum=0
    for x in priceList:
    	sum += x
    return round(sum/len(priceList),2)
