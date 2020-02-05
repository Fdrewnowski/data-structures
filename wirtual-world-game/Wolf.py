import Animal


class Wolf(Animal.Animal):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'W', 9, 5, x, y)

    def reproduction(self, x, y):
        return Wolf(self.world, self.world.get_turn(), x, y)
