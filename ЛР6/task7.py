print("--------- Задание 7 ---------")

class Worker:
    'doc class Worker'
    count = 0
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        Worker.count += 1
    def display(self):
        print("Worker:")
        print("{} {}".format(self.name,self.surname))

class Animal:
    id = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.id += 1
    def display(self):
        print("Animal id: {}".format(Animal.id))
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))

a1 = Animal("Lion", "3")
print("Animal.id: {}".format(Animal.id))
a1.display()
a2 = Animal("Dog", "12")
print("Animal.id: {}".format(Animal.id))
a1.display()
a3 = Animal("Bird", "2")
print("Animal.id: {}".format(Animal.id))
a1.display()


# Удостоверьтесь  в  работоспособности  программы,  запустив её.
# Ознакомьтесь  с  выведенной  информацией.