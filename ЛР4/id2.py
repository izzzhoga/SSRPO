from random import randint

def printMatrix (matrix): 
   for row in matrix: 
      for x in row: 
          print ( "{:4d}".format(x), end = "" ) 
      print ()

print("--------- Индивидуальное задание 2 ---------")
N1 = int(input("Введите количество строк: "))
N2 = int(input("Введите количество столбцов: "))
l = [[0 for j in range(N2)] for i in range(N1)]
coorX = 0
coorY = 0
maximum = 0
for i in range(N1):
    for j in range(N2):
        l[i][j] = randint(0, 100)
        if maximum < l[i][j]: 
            maximum = l[i][j]
            coorX = i + 1
            coorY = j + 1

print("Сгенерированный массив: ")
printMatrix(l)

print("Максимальный элемент равен: {0}. Строка: {1}. Столбец: {2}".format(maximum, coorX, coorY))
