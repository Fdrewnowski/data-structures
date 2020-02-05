import Organism
from random import randint
from abc import abstractmethod


class Plant(Organism.Organism):

    def __init__(self, world, age, sign, power, initiative, x, y):
        super().__init__(world, age, sign, power, initiative, x, y)

    def multiply(self, x, y):
        random = randint(0, 3)
        if random == 0 and self.x < self.world.get_width() - 1 and self.world.find_organism_by_location(x + 1, y) is None:
            self.world.add_organism(self.reproduction(x + 1, y))
        elif random == 1 and self.x > 0 and self.world.find_organism_by_location(x - 1, y) is None:
            self.world.add_organism(self.reproduction(x - 1, y))
        elif random == 3 and self.y < self.world.get_height() - 1 and self.world.find_organism_by_location(x, y + 1) is None:
            self.world.add_organism(self.reproduction(x, y + 1))
        elif random == 2 and self.y > 0 and self.world.find_organism_by_location(x, y - 1) is None:
            self.world.add_organism(self.reproduction(x, y - 1))

    def action(self, ch):
        random = randint(0, 8)
        if random == 1:
            self.multiply(self.x, self.y)

    def if_reflected_attack(self, other):
        return False

    def collision(self, other):
        return True

    @abstractmethod
    def reproduction(self, x, y):
        pass
