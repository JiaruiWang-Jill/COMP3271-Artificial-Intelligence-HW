"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import shop

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """    
    least=float("inf")
   

    for x in fruitShops:
      price=x.getPriceOfOrder(orderList)
      if price<least:
        least=price
        shop1=x
    "*** YOUR CODE HERE ***"
    return shop1
    
def shopArbitrage(orderList, fruitShops):
    """
    input: 
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    output:
        maximum profit in amount
    """
    difference=0
    for name,order in orderList:
      costlist1=[x.fruitPrices[name] for x in fruitShops]
      difference += (max(costlist1)-min(costlist1))*order
    return difference

def shopMinimum(orderList, fruitShops):
    """
    input: 
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    output:
        Minimun cost of buying the fruits in orderList
    """
    mini=0
    for name,order in orderList:
      costlist1=[x.fruitPrices[name] for x in fruitShops]
      mini += min(costlist1)*order
    return mini

if __name__ == '__main__':
  "This code runs when you invoke the script from the command line"
  orders = [('apples',1.0), ('oranges',3.0)]
  dir1 = {'apples': 2.0, 'oranges':1.0}
  shop1 =  shop.FruitShop('shop1',dir1)
  dir2 = {'apples': 1.0, 'oranges': 5.0}
  shop2 = shop.FruitShop('shop2',dir2)
  shops = [shop1, shop2]
  print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
  orders = [('apples',3.0)]
  print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
  
#second test
  dir1 = {'apples': 2.0, 'oranges':1.0}
  shop1 =  shop.FruitShop('shop1',dir1)
  dir2 = {'apples': 1.0, 'oranges': 5.0}
  shop2 = shop.FruitShop('shop2',dir2)
  dir3 = {'apples': 1.5, 'oranges': 2.0}
  shop3 = shop.FruitShop('shop3',dir3)
  shops = [shop1, shop2, shop3]
  order = [('apples',10.0), ('oranges',3.0)]
  print(shopArbitrage(order,shops))