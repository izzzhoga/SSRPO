print("Вычисление цифр Армстронга из диапазона от 100 до 9999:")
for i in range(100,1000):
    summ = 0
    for ind in range(0, 3):
        i = str(i)
        summ += int(i[ind]) ** 3
        i = int(i)
    if summ == i:
        print(i)
