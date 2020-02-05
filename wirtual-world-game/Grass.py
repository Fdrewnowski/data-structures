import Plant


class Grass(Plant.Plant):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'G', 0, 0, x, y)

    def reproduction(self, x, y):
        return Grass(self.world, self.world.get_turn(), x, y)
