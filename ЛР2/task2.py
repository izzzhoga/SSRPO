num1, num2 = 1, 1
print("Числа Фибоначчи: {0} {1}".format(num1, num2), end=' ')
for i in range(2, 8):
    num1, num2 = num2, num1 + num2
    print(num2, end=' ')
