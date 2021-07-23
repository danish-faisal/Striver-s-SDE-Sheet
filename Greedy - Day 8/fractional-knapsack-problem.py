# https://www.geeksforgeeks.org/fractional-knapsack-problem/

# Item Value DataClass
class ItemValue:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
        self.cost=self.value/self.weight


class FractionalKnapSack:

    @staticmethod
    def getMaxValue(weights,values,capacity):
        # array to store combined-value of given weight-value pairs
        sacks=[]

        for i in range(len(weights)):
            sacks.append(ItemValue(weights[i],values[i]))
        
        # sort the sacks-array in descending order of costs(value of 1 weight of each item)
        sacks.sort(key=lambda x:x.cost,reverse=True)

        # to keep track of total weight and total value added to the KnapSack
        addedWeight = totalVal = 0

        for i in sacks:
            # if the whole weight of the item with greater cost-value can be added,add it 
            if addedWeight+i.weight<=capacity:
                addedWeight+=i.weight
                totalVal+=i.value
            # will reach here only when capacity is at its end, and only a fraction of remaining items can be added
            # add a fraction of the item with next highest cost to fill the capacity
            else:
                remaining=capacity-addedWeight
                totalVal+=i.cost * remaining
                break
        
        return totalVal


# Driver Code
if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50
 
    # Function call
    maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)