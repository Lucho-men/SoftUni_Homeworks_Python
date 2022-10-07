import sys
n = int(input())
num = 0
sum = 0
max_num = -sys.maxsize

for i in range(1, n+1):
    num = int(input())
    if max_num < num:
        max_num = num
    sum += num

if sum - 2 * max_num == 0:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(2 * max_num - sum)}")
