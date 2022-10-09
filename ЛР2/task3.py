try:
    print("Введите 10 чисел: ")
    minValue = 1001
    for i in range(10):
        num = int(input())
        if (num % 2 == 0 and num % 3 != 0 and num < minValue):
            minValue = num
    if (minValue == 1001):
        print("Нет введенного числа, которое подходит под условия!")
    else:
        print("Минимальное значение среди введенных чисел: " + str(minValue))
except ValueError:
    print("Введите числа!")
