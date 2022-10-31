print("--------- Индивидуальное задание 1 ---------")
file_read = open("text.txt", "r", encoding="utf8")

while True:
    string = file_read.readline().split()
    length = 0
    res = []
    if string != []:
        # print(string)
        for i in string:
            if len(i) > length: length = len(i); res = []
            if len(i) == length: length = len(i); res.append(i)
        print(' '.join(res))
    if not string: break

file_read.close()


# Пусть дан файл с текстом.
# Для каждой строки распечатайте слово наибольшей длины.
# Если их несколько, то распечатайте все.