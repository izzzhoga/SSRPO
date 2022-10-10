from math import pow


def outputNum(a, b):
    print("Результат: " + str(int(pow(a, b))))

try:
    num = int(input("Введите число: "))
    pw = int(input("Введите степень: "))
    outputNum(num, pw)
except ValueError:
    print("Ошибка ввода! Будьте внимательнее!")
