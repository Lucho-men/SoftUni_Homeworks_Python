import sys
min = sys.maxsize
max = -sys.maxsize
n = int(input())
for i in range(0, n):
    num = int(input())
    if num < min:
        min = num
    if num > max:
        max = num

print(f"Max number: {max}")
print(f"Min number: {min}")


