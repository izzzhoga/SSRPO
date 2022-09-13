def counter(a, b, c):
    return a*b*c

try:
    hour = int(input("Введите количетво отработанных часов: "))
    price = int(input("Введите часовую ставку: "))
    k = 1
    if hour < 40:
        print("Зарплата равна:", counter(hour, price, k))
    else:
        k = 1.5
        print("Зарплата равна:", int(counter(hour, price, k)))
except ValueError:
    print("Введите числа!")