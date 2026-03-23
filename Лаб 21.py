'''
class Sim:
    def __init__(self, name, energy = 50):
        self.name = name
        self.energy = energy

class Bed:
    def use_for_sleep(self, sim):
        sim.energy = 100

my_sim = Sim(name = 'Bob')
my_bed = Bed()
my_bed.use_for_sleep(my_sim)
print(f'aertg {my_sim.name} fgafa {my_sim.energy}')
'''
