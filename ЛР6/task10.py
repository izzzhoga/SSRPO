from math import pi, pow

print("--------- Задание 10 ---------")

class Geometric:
    def calculateArea(self):
        print("Calculating area")

class Square(Geometric):
    def __init__(self, a):
        self.side = a
    def _perimeter(self):
        print("Perimeter of Square {}: {}\n".format(self.side, self.side * 4))
    def calculateArea(self):
        print("Area of Square {}: {}\n".format(self.side, pow(self.side, 2)))

class Circle(Geometric):
    def __init__(self, a):
        self.__radius = a
    def calculateArea(self):
        print("Площадь окружности равна: ", pi * pow(self.__radius, 2))

area1 = Circle(5)
area1.calculateArea()

print("Check subclass: ", issubclass(Circle, Geometric))
print("Check instance area1->Circle: ", isinstance(area1, Circle))
print("Check instance area1->Geometric: ", isinstance(area1, Geometric))
print("Check instance area1->dict: ", isinstance(area1, dict))
print("Geometric.__bases__: ", Geometric.__bases__)
print("Square.__bases__: ", Circle.__bases__)


# Дополните  код  программы  lab_06_03.py.
# Создайте  класс Circle, унаследованный от класса  Geometric, для которого определите атрибут radius.
# Сделайте атрибут radius  приватным (с использованием двойного  подчеркивания). 
# Переопределите  унаследованный  метод calculateArea(), рассчитав площадь окружности
# (значение числа Пи доступно в библиотеке math).