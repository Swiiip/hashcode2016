class Order:
    
    def __init__(self,location, purchase):
        self.location = location
        self.purchase = purchase
        self.totalWeight = self.getTotalWeight()
   
    def deliver(self, objectType, n):
        if objectType in self.purchase:
            if n<self.purchase[objectType]:
                self.purchase[objectType] -=n
            else:
                del self.purchase[objectType]
        return not bool(self.purchase)
        
    def getTotalWeight(self):
        total = 0
        for i in self.purchase:
            total += self.purchase[i]
        return total

if __name__ == "__main__":
    test = Order((3,2), {1:10, 2:20})
    print test.totalWeight

