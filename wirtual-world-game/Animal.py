import Organism
from random import randint
from abc import abstractmethod


class Animal(Organism.Organism):

    def __init__(self, world, age, sign, power, initiative, x, y):
        super().__init__(world, age, sign, power, initiative, x, y)

    def multiply(self, x, y):
        if self.x < self.world.get_width() - 1 and self.world.find_organism_by_location(x + 1, y) is None:
            #komunikat
            log = "Multiplication:" + str(type(self)) + '\n'
            self.world.add_log(log)
            self.world.add_organism(self.reproduction(x + 1, y))
        elif self.x > 0 and self.world.find_organism_by_location(x - 1, y) is None:
            #komunikat
            log = "Multiplication:" + str(type(self)) + '\n'
            self.world.add_log(log)
            self.world.add_organism(self.reproduction(x - 1, y))
        elif self.y < self.world.get_height() - 1 and self.world.find_organism_by_location(x, y + 1) is None:
            #komunikat
            log = "Multiplication:" + str(type(self)) + '\n'
            self.world.add_log(log)
            self.world.add_organism(self.reproduction(x, y + 1))
        elif self.y > 0 and self.world.find_organism_by_location(x, y - 1) is None:
            #komunikat
            log = "Multiplication:" + str(type(self)) + '\n'
            self.world.add_log(log)
            self.world.add_organism(self.reproduction(x, y - 1))

    def action(self, ch):
        random = randint(0, 3)
        self.set_last_move(random)
        if random == 0 and self.y < self.world.get_height() - 1:
            self.y += 1
        elif random == 1 and self.y > 0:
            self.y -= 1
        elif random == 2 and self.x < self.world.get_width() - 1:
            self.x += 1
        elif random == 3 and self.x > 0:
            self.x -= 1

    def if_reflected_attack(self, other):
        return False

    def collision(self, other):
        if other.if_reflected_attack(self):
            return True
        if type(other) == type(self): # or type
            self.recover_position()
            self.multiply(self.x, self.y)
            return True
        elif self.power > other.get_power():
            # comment
            log = "Fight:" + str(type(self)) + "&" + str(type(other))+'\n'
            log += "Wins:" + str(type(self))+'\n'
            self.world.add_log(log)
            self.world.delete_organism(other)
            return True
        elif self.power < other.get_power():
            # comment
            log = "Fight:" + str(type(self)) + "&" + str(type(other)) + '\n'
            log += "Wins:" + str(type(other)) + '\n'
            self.world.add_log(log)
            self.world.delete_organism(self)
            return True
        elif self.power == other.get_power() and self.initiative >= other.get_initiative():
            # comment
            log = "Fight:" + str(type(self)) + "&" + str(type(other)) + '\n'
            log += "Wins:" + str(type(self)) + '\n'
            self.world.add_log(log)

            self.world.delete_organism(other)
            return True
        elif self.power == other.get_power() and self.initiative < other.get_initiative():
            # comment
            log = "Fight:" + str(type(self)) + "&" + str(type(other)) + '\n'
            log += "Wins:" + str(type(other)) + '\n'
            self.world.add_log(log)
            self.world.delete_organism(self)
            return True

    @abstractmethod
    def reproduction(self, x, y):
        pass
