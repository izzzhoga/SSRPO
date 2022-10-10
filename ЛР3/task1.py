def minusLocal(a, b):
    return a - b

def minusGlobal():
    global globalNum1, globalNum2
    return globalNum1 - globalNum2

try:
    globalNum1 = int(input("Введите первое число: "))
    globalNum2 = int(input("Введите второе число: "))
    res1 = minusLocal(globalNum1, globalNum2)
    res2 = minusGlobal()
    print("Результат вычитания функции с параметрами: " + str(res1))
    print("Результат вычитания функции с глобальными переменными: " + str(res2))
except ValueError:
    print("Ошибка ввода! Будьте внимательнее!")
