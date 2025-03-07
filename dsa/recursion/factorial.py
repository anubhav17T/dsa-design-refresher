def factorial(num):
    if num == 0 or num == 1:
        return num
    print("I am calculating factorial for F{}".format(num))
    result = num * factorial(num - 1)
    print("Value is {}".format(result))
    return result


result = factorial(num=10)
