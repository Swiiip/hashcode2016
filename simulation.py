class Simulation:


    def __init__(self, paramDict, commandList):
        for e in paramDict:
            setattr(self, e, paramDict[e])

    def step(self):
        print "caca"
        
        
if __name__ == "__main__":

    sim = Simulation({"test" : "test2"})

    for i in range(sim.nbrRounds):
        sim.step();

