import Animal
from random import randint


class Turtle(Animal.Animal):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'T', 2, 1, x, y)

    def action(self, ch):
        random = randint(0, 3)
        if random == 2:
            super().action(ch)

    def if_reflected_attack(self, other):
        if other.get_power() < 5 and type(self) != type(other):
            #kommentarz o odbiciu
            log = "Turtle reflected attack:" + str(type(other)) + " !" + '\n'
            self.world.add_log(log)
            return True
        else:
            return False

    def reproduction(self, x, y):
        return Turtle(self.world, self.world.get_turn(), x, y)
