print("BASIC CALCULATOR")

num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))
op = input("Choose operator (+, -, *, /): ")

if op == "+":
    result = num1 + num2
    print(f"Answer: {num1} + {num2} = {result}")

elif op == "*":
    result = num1 * num2
    print(f"Answer: {num1} * {num2} = {result}")

elif op == "-":
    result = num1 - num2
    print(f"Answer: {num1} - {num2} = {result}")

elif op == "/":
    result = num1 / num2
    print(f"Answer: {num1} / {num2} = {result}")

else:
    print(f"Invalid operator: {op}")