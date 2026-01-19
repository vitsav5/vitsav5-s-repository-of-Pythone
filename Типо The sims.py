class Home:
    def __init__(self, name):
        self.name = name

    def sleep(self, sim):
        print(f'{sim.name}, спит в доме {self.name}')
        sim.energy += 20

    def relax(self, sim):
        print(f'{sim.name}, релаксит в доме {self.name}')
        sim.energy += 10

class Job:
    def __init__(self, title, salary, salarygay):
        self.title = title
        self.salary = salary
        self.salarygay = salarygay

    def work(self, sim):
        print(f'{sim.name} работает как {self.title}')
        sim.money += self.salary
        sim.energy -= 15

    def Gey_mer(self, sim):
        print(f'{sim.name} работает как {self.title}')
        sim.money += self.salarygay
        sim.energy -= 5

class Sim:
    def __init__(self, name, home, job, supermarcket):
        self.name = name
        self.energy = 50
        self.money = 100
        self.home = home
        self.job = job
        self.supermarcket = supermarcket

    def eat(self):
        print(f'{self.name} ест еду)')
        self.energy += 10
        self.money -= 5

    def show_status(self):
        print('-------')
        print(f'Имя: {self.name}')
        print(f'Энергия: {self.energy}')
        print(f'Деньги: {self.money}')

    def proverka(self):
        if self.energy < 0:
            print('Сим устал!!!')
        if self.money < 0:
            print('Сим без денег!!!')

class Supermarcket:
    def __init__(self, needsf, needsth):
        self.needsf = needsf
        self.needsth = needsth

    def food(self, sim):
        print(f'{sim.name} купил еды')
        sim.money -= self.needsf

    def things(self, sim):
        print(f'{sim.name} купил вещи')
        sim.money -= self.needsth

home = Home('Дом')
job = Job('чел', 50, 30)
supermarcket = Supermarcket(10, 15)
sim = Sim('боб', home, job, supermarcket)

sim.show_status()
sim.job.work(sim)
sim.job.Gey_mer(sim)
sim.supermarcket.food(sim)
sim.supermarcket.things(sim)
sim.home.sleep(sim)
sim.home.relax(sim)
sim.eat()
sim.show_status()
sim.proverka()