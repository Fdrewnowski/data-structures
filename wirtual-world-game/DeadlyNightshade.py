import Plant
import Animal


class DeadlyNightshade(Plant.Plant):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'd', 99, 0, x, y)

    def reproduction(self, x, y):
        return DeadlyNightshade(self.world, self.world.get_turn(), x, y)

    def if_reflected_attack(self, other):
        if isinstance(other, Animal.Animal):
            # komentarz
            log = "It was poisonous, dies:" + str(type(other)) + " !" + '\n'
            self.world.add_log(log)
            self.world.delete_organism(other)
            self.world.delete_organism(self)
            return True

        return False
