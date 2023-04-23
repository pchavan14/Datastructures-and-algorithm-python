#take the ratios (fractional) and then calculate

class Item:
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsack(items,capacity):
    items = sorted(items , key= lambda x : x.ratio , reverse= True)
    usedCapacity = 0
    totalValue = 0

    for i in items:
        print(i.weight , i.value , i.ratio)
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            print(unusedWeight)
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value

        if usedCapacity == capacity:
            break

    print(totalValue)




item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)

cList = [item1 , item2 , item3]

knapsack(cList, 50)