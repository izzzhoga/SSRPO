def outputNum(a):
    for i in range(a, 0, -1):
        if (a % i == 0): print(i, end = " ")

try:
    num = int(input("Введите число для обработки: "))
    print("Делители числа: ", end = "")
    outputNum(num)
except ValueError:
    print("Ошибка ввода! Будьте внимательнее!")
