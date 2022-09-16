def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

# print(square_digits(1685))

def printer_error(s):
    err_count = 0
    count = len(s)
    good_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m"]
    for i in s:
        if i not in good_list:
            err_count += 1
    print(str(err_count) + "/" + str(count))
    return 

inp = input()
printer_error(inp)