print("--------- Задание 8 ---------")

class Animal:
    count = 0
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        Animal.count += 1
    def display(self):
        print("Animal id: {}".format(self.id))
        print("Name: {}".format(self.name))
        print("Age: {}\n".format(self.age))

a1 = Animal(12, "Lion", "3")
print("Animal.count: {}".format(Animal.count))
a1.display()
a2 = Animal(34, "Dog", "12")
print("Animal.count: {}".format(Animal.count))
a1.display()
a3 = Animal(45, "Bird", "2")
print("Animal.count: {}".format(Animal.count))
a1.display()


# Модифицируйте  код  программы  lab_06_02.py.
# Измените название  атрибута  id  на  count.
# Модифицируйте  программу  так,  чтобы, определив  атрибут  id,
# он  являлся  уникальным  для  каждого  объекта, изменяясь на единицу с
# увеличением количества объектов класса.