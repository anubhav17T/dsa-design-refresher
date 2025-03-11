def multiply(num1: str, num2: str) -> str:
    if int(num1) == 0 or int(num2) == 0:
        return "0"
    return str(int(num1) * int(num2))


print(multiply(num1="3", num2="5"))