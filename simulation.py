from __future__ import division
import parser


class Simulation(object):

    def __init__(self, paramDict, solver):
        for e in paramDict:
            setattr(self, e, paramDict[e])
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
        
    def run(commands):
        currentCommand = {} #dictionary : key = drone, value = commande en cours
        currentState = {} # dictionary: key = drone, value = etat du drone
        isGiven = [false]*len(commands)
        
        for i in range(sim.turns):
            for d in range(len(self.drones)):
                drone = self.drones[d]
                
                #on check si le drone a bien une commande courrante
                if not (drone in currentCommand):
                    # on trouve la prochaine commande du drone
                    for k in range(len(commands)):
                        if not isGiven[k] and command[k].drone == d:
                            currentCommand[drone] = command[k]
                
                #on fait avancer la commande courrante
                    
                
        
    def step():
        miss


if __name__ == "__main__":
    input_file = 'data/busy_day.in'
    params = parser.parse(input_file)
    sim = Simulation(params)
    print(sim)

