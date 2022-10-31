import time

print("--------- Индивидуальное задание 1 ---------")

# Товар
class Merchandise:
    def __init__(self, category, type):
        self.__category = category
        self.__type = type
    def setCategory(self, newCategory):
        self.__category = newCategory
    def setType(self, newType):
        self.__type = newType

# Продукт
class Product(Merchandise):
    def __init__(self, category, type, name):
        super().__init__(category, type)
        self.name = name
    def setName(self, newName):
        self.name = newName

# Молочный продукт
class MilkProduct(Merchandise):
    def __init__(self, category, type, name, price):
        super().__init__(category, type)
        self.name = name
        self.price = price
    def setName(self, newName):
        self.name = newName
    def setPrice(self, newPrice):
        self.price = newPrice

# Игрушка
class Toy(Product):
    def __init__(self, category, type, name, material, color, price):
        super().__init__(category, type, name)
        self.material = material
        self.color = color
        self.price = price
    def setMaterial(self, newMaterial):
        self.material = newMaterial
    def setColor(self, newColor):
        self.color = newColor
    def setPrice(self, newPrice):
        self.price = newPrice

# Покупка
class Purchase:
    listPurchase = []
    cost = 0
    def addItemToPurchase(name):
        Purchase.listPurchase.append(name)
    def printPurchase():
        if len(Purchase.listPurchase) != 0:
            print("Корзина: ")
            for i in Purchase.listPurchase:
                Purchase.cost += i.price
                print("\t{}\n\tКатегория: {}\n\tТип: {}\n\tЦена: {}\n\n\tСтоимость покупок: {}\n\n".format(i.name, i._Merchandise__category, i._Merchandise__type, i.price, Purchase.cost))

        else:
            print("Ваша корзина пуста!\n")

dino = Toy("Игрушка", "Развивающая", "Динозаврик", "Пластик", "Желтый", 125)
sportCar = Toy("Игрушка", "Развивающая", "Молния МакКуин", "Пластик", "Красный", 630)
milk = MilkProduct("Кисломолочный продукт", "Молоко", "Белое Озеро", 57)
cheese = MilkProduct("Кисломолочный продукт", "Сыр", "Отрадное", 320)
Purchase.printPurchase()
Purchase.addItemToPurchase(dino)
Purchase.printPurchase()
Purchase.addItemToPurchase(cheese)
Purchase.printPurchase()


# Предметная область: Товары в магазине. Классы: игрушка, продукт, товар, молочный продукт, покупка