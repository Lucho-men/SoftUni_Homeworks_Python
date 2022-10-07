n = int(input())
num = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

for i in range(1, n + 1):
    num = int(input())
    if num < 200:
        num1 += 1
    elif 200 <= num <= 399:
        num2 += 1
    elif 400 <= num <= 599:
        num3 += 1
    elif 600 <= num <= 799:
        num4 += 1
    else:
        num5 += 1

print(f"{((num1 / n) * 100):0.2f}%")
print(f"{((num2 / n) * 100):0.2f}%")
print(f"{((num3 / n) * 100):0.2f}%")
print(f"{((num4 / n) * 100):0.2f}%")
print(f"{((num5 / n) * 100):0.2f}%")