try:
    x, y = map(int, input("Введите два числа через пробел и нажмите Enter: ").split())
    print("{0}+{1}=?".format(y, x))
    print("{0} | {1} | {2}".format(y, x, x+y))
    print("Z({0})=F({1})".format(x, y))
    print("x={0}; y={1};".format(x, y))
    print("Ответ: ({0};{1})".format(x, y))
except ValueError:
    print("Введите два числа через пробел!")