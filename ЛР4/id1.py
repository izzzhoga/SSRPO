from random import randint

print("--------- Индивидуальное задание 1 ---------")
N = int(input("Введите размер массива: "))
l = [(randint(0, 100)) for i in range(N)]
print("Сгенерированный массив: " + str(l))

l2 = []
while l:
    minimum = l[0]
    for x in l: 
        if x < minimum:
            minimum = x
    l2.append(minimum)
    l.remove(minimum)

print (l2)

res = 0
maximum = 0
count = False
while l2:
    for x in l2: 
        if x > maximum:
            maximum = x
            count = False
        elif x == maximum:
            count = True
            res = maximum
    l2.remove(x)

print(res)

'''Напишите программу, которая сортирует массив, 
а затем находит максимальное из чисел, встречающихся 
в массиве несколько раз. Не использовать встроенные функции.'''