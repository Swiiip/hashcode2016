class Warehouse:
    
    def __init__(self,location, inventory):
        self.inventory = inventory
        self.location = location
        
    
    def take(self,objectType,n):
        if objectType in self.inventory:
            if n< self.inventory[objectType]:
                self.inventory[objectType] -= n
                return n
            else:
                taken = self.inventory[objectType]
                del  self.inventory[objectType]
                return taken
        else:
            return 0
            
    def put(self,objectType,n):
        if objectType in self.inventory:
            self.inventory[objectType] += n
        else:
            self.inventory[objectType] = n
            
    def __str__(self):
        s = "Warehouse located at "+str(self.location)+".\n"
        s += "Products availables : "
        for p in self.inventory:
            s += "["+str(p)+","+str(self.inventory[p])+"], "
        return s        
    
            
if __name__== "__main__":
    w = Warehouse((2,5), {0:5,2:6, 4:7})
    print(w)
    print(w.take(0,2))
    print(w)
    print(w.take(2,3))
    print(w)
    print(w.take(0,4))
    print(w.put(1,3))
    print(w)
    w.put(0,2)
    print(w)
        
    
    
        
