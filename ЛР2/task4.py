from itertools import count


try:
    print("Вычисление среднего арифметического (для завершения работы введите 0): ")
    summ = 0
    count = 0
    while (True):
        num = int(input())
        if (num == 0): break
        summ += num
        count += 1
    print("Среднее арифметическое равно: {0}".format(int(summ/count)))
except ValueError:
    print("Введите числа!")
except ZeroDivisionError:
    print("Введите хотя бы одно число!")
