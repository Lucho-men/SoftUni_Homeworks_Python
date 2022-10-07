
num1 = int(input())
num2 = int(input())

operator = input()
even_or_odd = ""
result = 0.0

if operator == "+":
    if (num1 + num2) % 2 == 0:
        print(f"{num1} {operator} {num2} = {(num1 + num2)} - even")
    else:
        print(f"{num1} {operator} {num2} = {(num1 + num2)} - odd")

elif operator == "-":
    if (num1 - num2) % 2 == 0:
        print(f"{num1} {operator} {num2} = {(num1 - num2)} - even")
    else:
        print(f"{num1} {operator} {num2} = {(num1 - num2)} - odd")

elif operator == "*":
    if (num1 * num2) % 2 == 0:
        print(f"{num1} {operator} {num2} = {(num1 * num2)} - even")
    else:
        print(f"{num1} {operator} {num2} = {(num1 * num2)} - odd")

elif operator == "/":
    if num2 != 0:
        print(f"{num1} {operator} {num2} = {(num1 / num2):0.2f}")
    else:
        print(f"Cannot divide {num1} by zero")

elif operator == "%":
    if num2 != 0:
        print(f"{num1} {operator} {num2} = {(num1 % num2)}")
    else:
        print(f"Cannot divide {num1} by zero")


