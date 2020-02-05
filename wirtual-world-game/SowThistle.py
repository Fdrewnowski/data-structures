import Plant


class SowThistle(Plant.Plant):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 's', 0, 0, x, y)

    def reproduction(self, x, y):
        return SowThistle(self.world, self.world.get_turn(), x, y)

    def multiply(self, x, y):
        super().multiply(x, y)
        super().multiply(x, y)
        super().multiply(x, y)
