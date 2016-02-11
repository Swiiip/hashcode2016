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


if __name__ == "__main__":
    input_file = 'data/busy_day.in'
    params = parser.parse(input_file)
    sim = Simulation(params)
    print(sim)
    for i in range(sim.turns):
        sim.step();
