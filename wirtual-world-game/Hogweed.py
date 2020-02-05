import Plant
import Animal
import CyberSheep


class Hogweed(Plant.Plant):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'h', 10, 0, x, y)

    def reproduction(self, x, y):
        return Hogweed(self.world, self.world.get_turn(), x, y)

    def if_reflected_attack(self, other):
        if isinstance(other, Animal.Animal) and not isinstance(other, CyberSheep.CyberSheep):
            # komentarz
            log = "Oh noo, dies:" + str(type(other)) + '\n'
            self.world.add_log(log)
            self.world.delete_organism(other)
            self.world.delete_organism(self)
            return True
        elif isinstance(other, CyberSheep.CyberSheep):
            log = "CyberSheep eats Hogweed" + '\n'
            self.world.add_log(log)
            self.world.delete_organism(self)
            return True
        return False

    def action(self, ch):
        if self.world.get_height() > self. y + 1:
            o = self.world.find_organism_by_location(self. x, self.y + 1)
            if o is not None and isinstance(o, Animal.Animal) and not isinstance(o, CyberSheep.CyberSheep):
                #kommentarz
                log = "Oh no, dies:" + str(type(o)) + '\n'
                self.world.add_log(log)
                self.world.delete_organism(o)
        if 0 < self. y - 1:
            o = self.world.find_organism_by_location(self. x, self.y - 1)
            if o is not None and isinstance(o, Animal.Animal) and not isinstance(o, CyberSheep.CyberSheep):
                #kommentarz
                log = "Oh no, dies:" + str(type(o)) + '\n'
                self.world.add_log(log)
                self.world.delete_organism(o)
        if self.world.get_width() > self. x + 1:
            o = self.world.find_organism_by_location(self. x + 1, self.y)
            if o is not None and isinstance(o, Animal.Animal) and not isinstance(o, CyberSheep.CyberSheep):
                #kommentarz
                log = "Oh no, dies:" + str(type(o)) + '\n'
                self.world.add_log(log)
                self.world.delete_organism(o)
        if 0 < self. x - 1:
            o = self.world.find_organism_by_location(self. x - 1, self.y)
            if o is not None and isinstance(o, Animal.Animal) and not isinstance(o, CyberSheep.CyberSheep):
                #kommentarz
                log = "Oh no, dies:" + str(type(o)) + '\n'
                self.world.add_log(log)
                self.world.delete_organism(o)
        super().action(ch)
