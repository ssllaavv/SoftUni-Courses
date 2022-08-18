def calculator(op, num1, num2):
    if op == "multiply" or op == "*":
        return num1 * num2
    elif op == "divide" or op == "/":
        return num1 // num2
    elif op == "add" or op == "+":
        return num1 + num2
    elif op == "subtract" or op == "-":
        return num1 - num2


operator = input()
firs_num = int(input())
second_num = int(input())

print(calculator(operator, firs_num, second_num))

