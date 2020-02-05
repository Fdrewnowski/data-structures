import Animal


class Fox(Animal.Animal):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'F', 3, 7, x, y)

    def action(self, ch):
        super().action(ch)
        o = self.world.find_organism_by_location(self.x, self.y)
        if o is not None and o.get_power() > self.power:
            self.recover_position()

    def reproduction(self, x, y):
        return Fox(self.world, self.world.get_turn(), x, y)