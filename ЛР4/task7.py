def func(num):
    count = 0
    res = False
    for j in range(2, (num // 2 + 1)):
        if (num % j == 0):
            count += 1
    if (count <= 0):
        res = True
        return res
    else:
        res = False
        return res

print("--------- Задание 7 ---------")
l = input("Введите массив чисел через пробел для обработки: ").split(" ")
l2 = []
for i in l:
    result = func(int(i))
    if(result):
        l2.append(i)
print("Список простых чисел из введенного массива: ", end = ""); print(l2)

# Найдите в массиве все простые числа и скопируйте их в новый массив.