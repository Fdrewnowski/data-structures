import Wolf
import Grass
import Human
import Turtle
import Antelope
import SowThistle
import Fox
import Hogweed
import Guarana
import Sheep
import DeadlyNightshade
import CyberSheep

class World(object):

    height = 0
    width = 0
    turn = 1
    list_of_organisms = []
    new_organisms = []
    gui1 = None
    log =""

    def __init__(self, gui):
        self.gui1 = gui
        self.height = 15
        self.width = 15
        self.turn = 0
        org1 = Guarana.Guarana(self, self.get_turn(), 11, 11)
        self.list_of_organisms.append(org1)
        org2 = CyberSheep.CyberSheep(self, self.get_turn(), 4, 1)
        self.list_of_organisms.append(org2)
        org3 = Antelope.Antelope(self, self.get_turn(), 0, 8)
        self.list_of_organisms.append(org3)
        org4 = Hogweed.Hogweed(self, self.get_turn(), 0, 0)
        self.list_of_organisms.append(org4)
        org5 = Hogweed.Hogweed(self, self.get_turn(), 10, 3)
        self.list_of_organisms.append(org5)
        org6 = Sheep.Sheep(self, self.get_turn(), 'S', 7, 8, 4)
        self.list_of_organisms.append(org6)
        org7 = SowThistle.SowThistle(self, self.get_turn(), 13, 13)
        self.list_of_organisms.append(org7)
        org8 = DeadlyNightshade.DeadlyNightshade(self, self.get_turn(), 10, 0)
        self.list_of_organisms.append(org8)
        org9 = Fox.Fox(self, self.get_turn(), 6, 6)
        self.list_of_organisms.append(org9)
        org10 = Grass.Grass(self, self.get_turn(), 0, 13)
        self.list_of_organisms.append(org10)
        org11 = Wolf.Wolf(self, self.get_turn(), 5, 7)
        self.list_of_organisms.append(org11)
        org12 = Human.Human(self, self.get_turn(), 13, 2)
        self.list_of_organisms.append(org12)
        org13 = Grass.Grass(self, self.get_turn(), 0, 14)
        self.list_of_organisms.append(org13)
        org14 = Turtle.Turtle(self, self.get_turn(), 9, 9)
        self.list_of_organisms.append(org14)
        org15 = Sheep.Sheep(self, self.get_turn(), 'S', 8, 8, 4)
        self.list_of_organisms.append(org15)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_turn(self):
        return self.turn

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_log(self, log):
        self.log = log

    def add_log(self, log):
        self.log += log

    def add_organism(self, organism):
        if organism is not None:
            self.new_organisms.append(organism)
                #__add__(organism)

    def delete_organism(self, organism):
        for i in range(len(self.list_of_organisms) - 1):
            if self.list_of_organisms[i] == organism:
                self.list_of_organisms.remove(organism)
        for j in range(len(self.new_organisms) - 1):
            if self.new_organisms[j] == organism:
                self.new_organisms.remove(organism)



    def swap(self, listO, i):
        temp = listO[i]
        listO[i] = listO[i+1]
        listO[i+1] = temp

    def bubble_sort(self, listO, n):
       for j in range(0, n-1):
           for i in range(0, n-1):
               if listO[i].get_initiative() < listO[i+1].get_initiative():
                    self.swap(listO, i)
               elif listO[i].get_initiative() == listO[i+1].get_initiative() and listO[i].get_age() < listO[i+1].get_age():
                    self.swap(listO, i)
       return listO

    def action(self, ch):
        print("next")
        self.list_of_organisms = self.bubble_sort(self.list_of_organisms, len(self.list_of_organisms))
        self.turn += 1
        for i in range(0, len(self.list_of_organisms)):
            if i < len(self.list_of_organisms) and self.list_of_organisms[i] is not None:
                self.list_of_organisms[i].action(ch)
                print(str(type(self.list_of_organisms[i])))
                for j in range(0, len(self.list_of_organisms)):
                    if j < len(self.list_of_organisms) and i < len(self.list_of_organisms) and\
                            self.list_of_organisms[i] is not None and\
                            self.list_of_organisms[i].get_x() == self.list_of_organisms[j].get_x() and\
                            self.list_of_organisms[i].get_y() == self.list_of_organisms[j].get_y() and\
                            self.list_of_organisms[i] != self.list_of_organisms[j]:

                        if self.list_of_organisms[i].collision(self.list_of_organisms[j]):
                            break
        self.draw()

    def find_organism_by_location(self, x, y):
        tmp = None
        for i in range(0, len(self.list_of_organisms)):
            ox = self.list_of_organisms[i].get_x()
            oy = self.list_of_organisms[i].get_y()
            if ox == x and oy == y:
                tmp = self.list_of_organisms[i]
        for i in range(0, len(self.new_organisms)):
            if self.new_organisms[i].get_x() == x and self.new_organisms[i].get_x() == x:
                tmp = self.new_organisms[i]
        return tmp

    def draw(self):
        self.list_of_organisms += self.new_organisms
        self.new_organisms.clear()
        for i in range(len(self.list_of_organisms)):
            self.gui1.set_image(self.list_of_organisms[i])

    def save(self):
        file = open("save&load/saved.txt", "w")
        for i in range(len(self.list_of_organisms)):
            o = self.list_of_organisms[i]
            file.write('%d' % o.get_x())
            file.write(";")
            file.write('%d' % o.get_y())
            file.write(";")
            file.write(o.get_sign())
            file.write(";")
            file.write('%d' % o.get_power())
            file.write(";")
            file.write('%d' % o.get_age())
            if isinstance(o, Human.Human):
                file.write(";")
                file.write('%d' % o.get_super_power())
            file.write("\n")
        file.close()

    def load(self):
        self.new_organisms.clear()
        self.list_of_organisms.clear()
        line = ""
        list = []
        with open('save&load/saved.txt') as f:
            for line in f:
                list = line.split(";")
                if list[2] == 'H':
                    o = Human.Human(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_super_power(int(list[5]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'A':
                    o = Antelope.Antelope(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'd':
                    o = DeadlyNightshade.DeadlyNightshade(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'F':
                    o = Fox.Fox(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'G':
                    o = Grass.Grass(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'g':
                    o = Guarana.Guarana(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'h':
                    o = Hogweed.Hogweed(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'S':
                    o = Sheep.Sheep(self, int(list[4]), 'S', int(list[0]), int(list[1]), 4)
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 's':
                    o = SowThistle.SowThistle(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'W':
                    o = Wolf.Wolf(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'T':
                    o = Turtle.Turtle(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)
                elif list[2] == 'C':
                    o = CyberSheep.CyberSheep(self, int(list[4]), int(list[0]), int(list[1]))
                    o.set_power(int(list[3]))
                    self.add_organism(o)

    def get_human(self):
        for i in range(len(self.list_of_organisms)):
            if isinstance(self.list_of_organisms[i], Human.Human):
                return self.list_of_organisms[i]
        return None

    def get_hogweed(self):
        list_of_hogs =[]
        for i in range(len(self.list_of_organisms)):
            if isinstance(self.list_of_organisms[i], Hogweed.Hogweed):
                list_of_hogs.append(self.list_of_organisms[i])
        return list_of_hogs


