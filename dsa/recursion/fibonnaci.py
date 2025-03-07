def fib(num: int) -> int:
    if num == 1 or num == 0:
        return num
    a, b = 0, 1
    for _ in range(2, num + 1):  # have taken 0 and first number manually
        a, b = b, a + b

    return b


fib(num=20)



def fibr(num:int)->int:
    if num==1 or num==0:
        return num
    else:
        return fib(num-1)+fib(num-2)

fibr(num=20)