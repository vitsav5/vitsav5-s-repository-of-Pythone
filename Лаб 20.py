'''
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} издаёт какой-то звук."
my_cat = Cat('Мурчик')
print(my_cat.speak())
my_cat.name = 'Барсик'
print(my_cat.name)
'''

'''
class Zombie:
    def __init__(self, name):
        self.name = name
        self.health = 50
    def growl(self):
        return f'{self.name} рычит: УУУУ!'

z1 = Zombie('Кровавый')
print(z1.name)
print(z1.health)
print(z1.growl())
'''

''''''
print('=== БИТВА ГЕРОЕВ ===')
# Герой
class Character:
    def __init__(self, name, healthe = 100, max_health = None, damage = 20):
        self.name = name
        self.healthe = healthe
        self.max_healthe = max()
        self.damage = damage

    def status(self):
        percent = (self.healthe / self.max_healthe) * 100
        return f'{self.name}: {self.healthe} / {self.max_healthe} HP ({percent:.0f}%0 | Урон: {self.damage}'

    def attack(self, damage):
        return f'{self.name} бьёт {target.name} на {self.damage}'

    def take_damage(self, damage):
        self.healthe -= damage
        if self.healthe < 0:
            self.healthe = 0
        return f'{self.name} получил {damage} урона! Осталось {self.healthe} HP'

    def is_alive(self):
        return self.healthe > 0

# ВРАГ
class Enemy:
    def __init__(self, name, healthe = 60, damage = 15):
        self.name = name
        self.healthe = healthe
        self.damage = damage
        self.max_healthe = healthe

    def status(self):
        percent = (self.healthe / self.max_healthe) * 100
        return f'{self.name}: {self.healthe} / {self.max_healthe} HP ({percent:.0f}%0 | Урон: {self.damage}'

    def attack(self, damage):
        return f'{self.name} бьёт {target.name} на {self.damage}'

    def take_damage(self, damage):
        self.healthe -= damage
        if self.healthe < 0:
            self.healthe = 0
        return f'{self.name} получил {damage} урона! Осталось {self.healthe} HP'

    def is_alive(self):
        return self.healthe > 0

    