from __future__ import division
import parser
from Drone import Drone
from Warehouse import Warehouse
from Order import Order

class Simulation(object):

    def __init__(self, paramDict, solver):
        self.cols = params['y']
        self.rows = params['x']
        self.nbTurns = params['turns']
        self.weights = params['weights']
        self.warehouses = []
        for place, invent_dict in params['warehouses']:
            self.warehouses.append(Warehouse(place, invent_dict))
        self.orders = []
        for place, invent_dict in params['orders']:
            self.orders.append(Order(place, invent_dict))
        self.drones = []
        for e in params['nb_drones']:
            self.drones.append(Drone(payload, init_pos, self.weights))

        self.score = 0.0
        self.solver = solver

    def __str__(self):
        s = ''
        for e in self.__dict__:
            s += e + '\n'
            s += str(self.__dict__[e]) + '\n'
        return s

    def step(self):
        print "caca"
        
    def run(self, commands):
        isGiven = [false]*len(commands)
        
        unloadDrones = []
        otherDrones = []
        
        for i in range(sim.turns):
            for d in range(self.drones):
                drone = self.drones[d]
                               
                #on check si le drone a bien une commande courrante
                if not drone.busy:
                    # on trouve la prochaine commande du drone
                    for k in range(len(commands)):
                        command = command[k]
                        if not isGiven[k] and command[0] == d:
                            drone.command(shapeCommand(command))
                            isGiven[k] = True
                            
                if drone.getOrderType() == 'U':
                    unloadDrones.append(drone)
                else:
                    otherDrones.append(drone)
                    
            #on fait avancer/executer chaque drone
            for drone in unloadDrones: # en commançant par ceux qui dechargent
                drone.step()
            for drone in otherDrones:
                drone.step()
    
    def shapeCommand(self, command): # take a comand in the standard format (int and char only) and transfor object index into reference
        symbol = command[1]
        result = [symbol]
        if symbol == "U" or symbol == "L":
            result.append(self.warehouses[command[2]])
            result += command[3:]
        elif symbol == "D":
            result.append(self.orders[command[2]])
            result += command[3:]
        elif symbol == "W":
            result.append(command[2])
                    
        return result                       
        

if __name__ == "__main__":
    input_file = 'data/busy_day.in'
    params = parser.parse(input_file)
    sim = Simulation(params)
    print(sim)

