def outputNum(a):
    count = 0
    while (a != 0):
        count += 1
        a //= 10
    return count

try:
    num = int(input("Введите число для обработки: "))
    print("Количество цифр числа равно: " + str(outputNum(num)))
except ValueError:
    print("Ошибка ввода! Будьте внимательнее!")
