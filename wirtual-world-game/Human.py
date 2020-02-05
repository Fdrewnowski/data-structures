import Animal


class Human(Animal.Animal):

    superPower = 0

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'H', 5, 4, x, y)
        self.superPower = 0

    def reproduction(self, x, y):
        return Human(self.world, self.world.get_turn(), x, y)

    def get_super_power(self):
        return self.superPower

    def set_super_power(self, super_power):
        self.superPower = super_power

    def action(self, ch):
        if self.superPower > 5:
            #komentarz
            log = "Superpower activated!" + '\n'
            self.world.add_log(log)
            if self.world.get_height() > self.y + 1:
                o = self.world.find_organism_by_location(self.x, self.y + 1)
                if o is not None:
                    # kommentarz
                    log = "Human burned:" + str(type(o)) + " !" + '\n'
                    self.world.add_log(log)
                    self.world.delete_organism(o)
            if 0 < self.y - 1:
                o = self.world.find_organism_by_location(self.x, self.y - 1)
                if o is not None:
                    # kommentarz
                    log = "Human burned:" + str(type(o)) + " !" + '\n'
                    self.world.add_log(log)
                    self.world.delete_organism(o)
            if self.world.get_width() > self.x + 1:
                o = self.world.find_organism_by_location(self.x + 1, self.y)
                if o is not None:
                    # kommentarz
                    log = "Human burned:" + str(type(o)) + " !" + '\n'
                    self.world.add_log(log)
                    self.world.delete_organism(o)
            if 0 < self.x - 1:
                o = self.world.find_organism_by_location(self.x - 1, self.y)
                if o is not None:
                    # kommentarz
                    log = "Human burned:" + str(type(o)) + " !" + '\n'
                    self.world.add_log(log)
                    self.world.delete_organism(o)

        self.superPower -= 1
        if self.superPower < 0:
            self.superPower = 0

        if ch == 0 and self.y < self.world.get_height() - 1:
            self.y += 1
        elif ch == 1 and self.y > 0:
            self.y -= 1
        elif ch == 2 and self.x < self.world.get_width() - 1:
            self.x += 1
        elif ch == 3 and self.x > 0:
            self.x -= 1
