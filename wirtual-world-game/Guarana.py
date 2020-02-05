import Plant


class Guarana(Plant.Plant):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'g', 0, 0, x, y)

    def reproduction(self, x, y):
        return Guarana(self.world, self.world.get_turn(), x, y)

    def if_reflected_attack(self, other):
        tmp = other.get_power()
        tmp += 3
        other.set_power(tmp)
        #komentarz
        log = "Organism gets +3 power:" + str(type(other)) + '\n'
        self.world.add_log(log)
        self.world.delete_organism(self)
        return True
