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
            self.drones.append(Drone(payload, init_pos))

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


if __name__ == "__main__":
    input_file = 'data/busy_day.in'
    params = parser.parse(input_file)
    sim = Simulation(params)
    print(sim)
    for i in range(sim.turns):
        sim.step();
