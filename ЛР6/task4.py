print("--------- Задание 4 ---------")
import time

class Ticket:
    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print("Delete  ticket: ", self.createDate)

    def display(self):
        print("Ticket:")
        print("  createDate: ", self.createDate)
        print("  owner: ", self.owner)
        print("  deadline: ", time.asctime(self.deadline))

# создание объект класса
ticket1 = Ticket(time.strftime("%d %b %Y %H:%M:%S", time.localtime()), "Ivan Ivanov", time.strptime("17.12.2017", "%d.%m.%Y"))

# вызов метода
ticket1.display()

# получение значения атрибута
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1,"owner"))

# проверка наличия атрибута
print("hasattr: ", hasattr(ticket1,"owner")) 
setattr(ticket1, "owner", "Alexei  Petrov")  # установка значения атрибута
print("Owner(setattr): ", ticket1.owner)

delattr(ticket1, "owner")  # удаление  значения атрибута
print("delattr: ", ticket1.owner) if hasattr(ticket1,"owner") else print("Нет такого атрибута!")

del ticket1 # удаление объекта
# print(ticket1)


# Дополните  код  программы  lab_06_01.py.
# Получите  текущее время  сервера  (или  компьютера) и
# выведите  его  на  экран  в  аналогичном формате: 9 Mar 2017 14:53:55.