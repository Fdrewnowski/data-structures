import Animal


class Sheep(Animal.Animal):

    def __init__(self, world, age, sign, x, y, power):
        super().__init__(world, age, sign, power, 4, x, y)

    def reproduction(self, x, y):
        return Sheep(self.world, self.world.get_turn(), 'S', x, y, 4)
