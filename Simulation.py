class Simulation:

    grid = (0, 0);
    nbrRounds = 10;
    drones = {};
    orders = {};
    warehouses = {};

    def __init__(self, runningMethod):
        print "init";

    def step(self):
        print("Caca");
        
if __name__ == "__main__":

    sim = Simulation("default");

    for i in range(sim.nbrRounds):
        sim.step();

