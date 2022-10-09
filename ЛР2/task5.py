from random import randint

print("Вычисление среднего арифметического (для завершения работы введите 0): ")
summ = 0
count = 0
while (True):
    num = randint(0, 100)
    print(num)
    if (num == 0): break
    summ += num
    count += 1
print("Среднее арифметическое равно: {0}".format(int(summ/count)))
