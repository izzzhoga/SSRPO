print("--------- Задание 1 ---------")
res = 1
file_read = open("input.txt", "r")
file_write = open("output.txt", "w")
string = file_read.read().split(" ")
for i in string:
    res *= int(i)
file_write.write(str(res))
file_read.close()
file_write.close()

# Считать из файла input.txt 10 чисел (числа записаны через пробел). 
# Затем записать их произведение в файл output.txt.