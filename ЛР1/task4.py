def num_check(a):
    count = 0
    while a > 0:
        a //= 10
        count += 1
    return count

try:
    num = int(input("Введите число для проверки: "))
    result = num_check(num)
    if result == 4:
        print("Число четырёхзначное!")
    else:
        print("Число не четырёхзначное! Попробуйте ещё...")
except ValueError:
    print("Введите числа!")