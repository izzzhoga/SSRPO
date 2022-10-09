try:
    N = int(input("Введите число: "))
    print("Автоморфные числа до {0}: ".format(N))
    for i in range(N + 1):
        num = i
        if num * num % (10 ** len(str(num))) == num :
            print(i)
except ValueError:
    print("Введите число!")
    