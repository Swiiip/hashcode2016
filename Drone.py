'''
Created on 11 févr. 2016

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
    
    def __print__(self):
        print "Drone id " + self.id + " , maxPayload : " + self.payloadWeight
        print "payload" + self.payload
        print "current weight " + self.currentPayloadWeight
        