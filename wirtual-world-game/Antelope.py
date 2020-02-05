import Animal
from random import randint


class Antelope(Animal.Animal):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'A', 4, 4, x, y)

    def reproduction(self, x, y):
        return Antelope(self.world, self.world.get_turn(), x, y)

    def collision(self, other):
        random = randint(0, 1)
        if random == 1 and type(self) != type(other) and isinstance(other, Animal.Animal):
            #komentarz
            if self.go_to_free_position():
                log = "Antelope reflected Attack" + '\n'
                self.world.add_log(log)
                return True
            else:
                return super().collision(other)
        else:
            return super().collision(other)

    def if_reflected_attack(self, other):
        random = randint(0, 1)
        if random == 1 and type(self) != type(other):
            return self.go_to_free_position()
        else:
            return False

    def action(self, ch):
        super().action(ch)
        super().action(ch)

    def go_to_free_position(self):
        if self.world.get_height() > self.y + 1 and self.world.find_organism_by_location(self.x, self.y + 1) is not None:
            self.y += 1
            log = "Antelope reflected Attack" + '\n'
            self.world.add_log(log)
            return True
        elif self.y - 1 >= 0 and self.world.find_organism_by_location(self.x, self.y - 1) is not None:
            self.y -= 1
            log = "Antelope reflected Attack" + '\n'
            self.world.add_log(log)
            return True
        elif self.world.get_width() > self.x + 1 and self.world.find_organism_by_location(self.x + 1, self.y) is not None:
            self.x += 1
            log = "Antelope reflected Attack" + '\n'
            self.world.add_log(log)
            return True
        elif self.x - 1 >= 0 and self.world.find_organism_by_location(self.x - 1, self.y) is not None:
            self.x -= 1
            log = "Antelope reflected Attack" + '\n'
            self.world.add_log(log)
            return True
        else:
            return False
