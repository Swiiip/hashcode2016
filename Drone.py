'''
Created on 11 fevr. 2016

@author: capitaine slip
'''
import numpy as np
class Drone(object):
    '''
    classdocs
    '''


    def __init__(self, droneID, posX, posY, payloadWeight):
        '''
        Constructor
        '''
        self.id = droneID
        self.pos = np.array((posX,posY))
        self.payload = []
        self.payloadWeight = payloadWeight
        self.currentPayloadWeight = 0
        
    def goto(self, posX ,posY):
        newPos = np.array((posX,posY))
        distance = np.linalg.norm(self.pos - newPos)
        Drone.pos = newPos
        return np.floor(distance)
    
    def load(self,objet,number,weight,warehouse):
        
        if weight + self.currentPayloadWeight <= self.payloadWeight:
            self.currentPayloadWeight
            self.payload.append(objet)
            warehouse.take(objet,number)
        else:
            raise ValueError
        
        return 1
    
    def unload(self, objet,weight, warehouse):
        if objet in self.payload:
            self.currentPayloadWeight -= weight
            self.payload.remove(objet)
            warehouse.put(objet)
        else:
            raise ValueError
        return 1
    
    def deliver(self, objet,weight):
        if objet in self.payload:
            self.currentPayloadWeight -= weight
            self.payload.remove(objet)
        else:
            raise ValueError
    
    def __str__(self):
        return "Drone id " + str(self.id) + " , maxPayload : " + str(self.payloadWeight) +"\n"
        + "payload [" + str(self.payload) + "]\n"
        + "current weight " + str(self.currentPayloadWeight)
        
if __name__ == "__main__":
    D = Drone(0,10,20,30)
    print D
    print D.goto(24,34)
    print "BONGEOURRE"
        