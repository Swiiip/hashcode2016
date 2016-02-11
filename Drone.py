'''
Created on 11 fevr. 2016

@author: capitaine slip
'''
import Warehouse
import numpy as np
from IPython.config.application import catch_config_error
class Drone(object):
    '''
    classdocs
    '''


    def __init__(self, location, payloadWeight):
        '''
        Constructor
        '''
        self.pos = location
        self.payload = {}
        self.payloadWeight = payloadWeight
        self.currentPayloadWeight = 0
        
    def goto(self, location):
        distance = np.sqrt((self.pos[0]-location[0])*(self.pos[0]-location[0]) + (self.pos[1]-location[1])*(self.pos[1]-location[1]))
        self.pos = location
        return np.floor(distance)
    
    def gotoWH(self,warehouse):
        return self.goto(warehouse.location)
    
    def load(self,objet,n,weight,warehouse):
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
    
    def unload(self, objet,weight,n, warehouse):
        unloaded = 0
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
    
    def deliver(self,objet,weight,n):
        delivered = 0
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
            
        return delivered
    
    def __str__(self):
        return "Drone , maxPayload : " + str(self.payloadWeight) +"\n"
        + "payload [" + str(self.payload) + "]\n"
        + "current weight " + str(self.currentPayloadWeight)
        
if __name__ == "__main__":
    D = Drone((10,10),30)
    W = Warehouse.Warehouse((2,5), {0:5,2:6,4:7})
    print D
    print D.goto((24,34))
    print D.gotoWH(W)
    print D.load(0, 4, 1, W)
    print D.unload(0, 1, 2, W)
    print D.deliver(0,1,1)
    print "BONGEOURRE"
        