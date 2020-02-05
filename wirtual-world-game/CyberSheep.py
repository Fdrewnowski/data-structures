import Sheep
import Animal
import math


class CyberSheep(Sheep.Sheep):

    def __init__(self, world, age, x, y):
        super().__init__(world, age, 'C', x, y, 11)

    def reproduction(self, x, y):
        return CyberSheep(self.world, self.world.get_turn(), x, y)

    def action(self, ch):
        list_of_hogweed = self.world.get_hogweed()
        list_of_distances = []
        list_of_x =[]
        list_of_y =[]
        smallest = 100000
        index = 0
        if len(list_of_hogweed)>0:
            for i in range(len(list_of_hogweed)):
                list_of_x.append(abs(list_of_hogweed[i].get_x()-self.get_x()) + 1)
                list_of_y.append(abs(list_of_hogweed[i].get_y()-self.get_y()) + 1)
                c = math.sqrt(list_of_x[i]**2 + list_of_y[i]**2)
                list_of_distances.append(c)
            for i in range(len(list_of_distances)):
                if list_of_distances[i] < smallest:
                    smallest = list_of_distances[i]
                    nearHog = list_of_hogweed[i]
                    index = i
            if list_of_x[index] >= list_of_y[index]:
                if self.get_x()-list_of_hogweed[index].get_x() > 0:
                    self.x -= 1
                elif self.get_x()-list_of_hogweed[index].get_x() < 0:
                    self.x += 1
                else:
                    print("Warning")
                    self.recover_position()
            elif list_of_x[index] < list_of_y[index]:
                 if self.get_y() - list_of_hogweed[index].get_y() > 0:
                    self.y -= 1
                 elif self.get_y() - list_of_hogweed[index].get_y() < 0:
                    self.y += 1
                 else:
                    print("Warning")
                    self.recover_position()
        else:
            ch = 4
            super().action(ch)
