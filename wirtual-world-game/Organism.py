import World
from abc import ABCMeta, abstractmethod


class Organism(object):
    """ wtf


    Attributes:
        age:
        world:
        sign:
        power:
        initiative:
        x:
        y:
        last_move:

    """
    age = 0
    world = World
    sign = '*'
    power = 0
    initiative = 0
    x = 0
    y = 0
    last_move = 4

    __metaclass__ = ABCMeta

    def __init__(self, world, age, sign, power, initiative, x, y):
        self.age = age
        self.world = world
        self.sign = sign
        self.power = power
        self.initiative = initiative
        self.x = x
        self.y = y

    def get_age(self):
        return self.age

    def get_sign(self):
        return self.sign

    def get_initiative(self):
        return self.initiative

    def get_power(self):
        return self.power

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_last_move(self):
        return self.last_move

    def recover_position(self):
        if self.last_move == 0 and self.y > 0:
                self.y -= 1
        elif self.last_move == 1 and self.y < self.world.get_height() - 1:
                self.y += 1
        elif self.last_move == 3 and self.x < self.world.get_width() - 1:
                self.x += 1
        elif self.last_move == 2 and self.x > 0:
                self.x -= 1

    def same_location(self, organism):
        if self != organism and self.get_x() == organism.get_x() and self.get_y:
            return 1
        return 0

    def set_age(self, age):
        self.age = age

    def set_initiative(self, initiative):
        self.initiative = initiative

    def set_last_move(self, last_move):
        self.last_move = last_move

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_power(self, pow):
        self.power = pow

    def set_sign(self, sign):
        self.sign = sign

    @abstractmethod
    def collision(self, other):
        pass

    @abstractmethod
    def multiply(self, x, y):
        pass

    @abstractmethod
    def reproduction(self, x, y):
        pass

    @abstractmethod
    def action(self, ch):
        pass

    @abstractmethod
    def if_reflected_attack(self, other):
        pass
