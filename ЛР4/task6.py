import copy

print("--------- Задание 6 ---------")
word = input("Введите слово для проверки палиндрома: ")
l = list(word)
l2 = copy.deepcopy(l)
l2.reverse()
if(l == l2):
    print("Слово ЯВЛЯЕТСЯ палиндромом!")
else:
    print("Слово НЕ ЯВЛЯЕТСЯ палиндромом!")

# Проверить, является ли заданное слово палиндромом.