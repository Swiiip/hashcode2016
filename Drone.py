'''
Created on 11 fevr. 2016

@author: capitaine slip
'''
import Warehouse
import numpy as np
class Drone(object):
    '''
    classdocs
    '''


    def __init__(self, location, payloadWeight, weights):
        '''
        Constructor
        '''
        self.pos = location
        self.payload = {}
        self.payloadWeight = payloadWeight
        self.currentPayloadWeight = 0
        self.busy = False
        self.commandType = 'W'
        self.command = []
        self.weights = weights
        self.timeleft = 0
        
    def goto(self, location):
        distance = np.sqrt((self.pos[0]-location[0])*(self.pos[0]-location[0]) + (self.pos[1]-location[1])*(self.pos[1]-location[1]))
        self.pos = location
        return np.floor(distance)
    
    def gotoWH(self,warehouse):
        return self.goto(warehouse.location)
    
    def load(self,objet,n,warehouse):
        weight = self.weights[objet]
        if weight*n + self.currentPayloadWeight <= self.payloadWeight:
            self.currentPayloadWeight += weight*n
            if objet in self.payload :
                self.payload[objet] += n
            else:
                self.payload[objet] = n
            warehouse.take(objet,n)
        else:
            raise ValueError
        
        return 1
    
    def takeCommand(self,commandType,param):    
        self.command = param
        self.commandType = commandType
        if commandType == 'D':
            self.timeleft = self.goto(param[0]) + 1
            self.busy = True
        if commandType == 'W':
            self.timeleft = param[0]
            self.busy = True 
        if commandType == 'L' or commandType == 'U':
            self.timeleft = self.gotoWH(param[0])
            self.busy =True
        
        return 0
    
    def step(self):
        if self.timeleft>1:
            self.timeleft -=1
        else:
            self.timeleft = 0
            out = self.execute()
            if out <> False:
                return out
            
            
            
    def execute(self):
        self.busy =True
        if self.commandType == 'D':
            return self.deliver(self.command[2],self.command[3])
        if self.commandType == 'L':
            self.load(self.command[2],self.command[3],self.command[1])
            return False
        if self.commandType == 'U':
            self.unload(self.command[2],self.command[3],self.command[1])
            return False
    
    def unload(self, objet,n, warehouse):
        unloaded = 0
        weight = self.weights[objet]
        if objet not in self.payload:
            return unloaded
        if self.payload[objet] >= n:
            self.currentPayloadWeight -= n*weight
            self.payload[objet] -= n
            warehouse.put(objet,n)
            unloaded = n
        else:
            self.currentPayloadWeight -= self.payload[objet]*weight
            unloaded = self.payload[objet]
            warehouse.put(objet,self.payload[objet])
            self.payload[objet] = 0
        return unloaded
    
    
    def deliver(self,objet,n):
        weight = self.weights[objet]
        delivered = False
        if objet not in self.payload:
            return delivered
        if self.payload[objet] >= n:
            self.currentPayloadWeight -= n*weight
            self.payload[objet] -= n
            delivered = n
        else:
            self.currentPayloadWeight -= self.payload[objet]
            delivered = self.payload[objet]
            self.payload[objet] = 0
            
        return self.command([1].deliver(objet,n))
    
    def __str__(self):
        return "Drone , maxPayload : " + str(self.payloadWeight) +"\n"
        + "payload [" + str(self.payload) + "]\n"
        + "current weight " + str(self.currentPayloadWeight)
        
if __name__ == "__main__":
    D = Drone((10,10),30,[1,1,1,1])
    W = Warehouse.Warehouse((2,5), {0:5,2:6,4:7})
    print D
    print D.goto((24,34))
    print D.gotoWH(W)
    print D.load(0, 4, W)
    print D.unload(0, 1, W)
    print D.deliver(0,1)
    D.takeCommand('W', [4])
    print D.busy
    D.step()
    D.step()
    D.step()
    D.step()
    print D.busy
    print "BONGEOURRE"
        