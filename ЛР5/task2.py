print("--------- Задание 2 ---------")
file_read = open("input_children.txt", "r", encoding="utf8")
file_write = open("output_children.txt", "w", encoding="utf8")
minimum = 1000
maximum = 0
minList = []
maxList = []

while True:
    string = file_read.readline().split()
    if string != []:
        if int(string[2]) > maximum: maxList = string; maximum = int(string[2])
        if int(string[2]) < minimum: minList = string; minimum = int(string[2])
        print(maxList, minList)
    if not string: break
file_write.writelines(' '.join(maxList) + "\n")
file_write.writelines(' '.join(minList))

file_read.close()
file_write.close()

# В файл записаны сведения о детях детского сада:
# Иванов Иван 5 лет
# Необходимо записать в текстовый файл самого старшего и самого младшего.
