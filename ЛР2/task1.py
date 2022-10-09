try:
    plusCount, minusCount = 0, 0
    num = int(input("Вводите положительные и отрицательные целые числа (для завершения ввода введите 0): "))
    while (num != 0):
        if (num > 0):
            plusCount += 1
        else:
            minusCount += 1
        num = int(input())
    print("Количество положительных чисел: {0}. Количество отрицательных чисел: {1}.".format(plusCount, minusCount))
except ValueError:
    print("Ошибка ввода! Будьте внимательнее!")
