def outputNum(a):
    while (a > 0):
        print(a % 10)
        a //= 10

try:
    num = int(input("Введите число для обработки: "))
    outputNum(num)
except ValueError:
    print("Ошибка ввода! Будьте внимательнее!")
