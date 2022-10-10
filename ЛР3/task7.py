def outputNum(a):
    fact = 1
    for i in range(2, a + 1):
        fact *= i
    return fact

try:
    num = int(input("Введите число для нахождения факториала: "))
    print("Факториал равен: " + str(outputNum(num)))
except ValueError:
    print("Ошибка ввода! Будьте внимательнее!")
