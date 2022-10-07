import sys

divisor = int(input())
boundary = int(input())
maximum = 0
for i in range(boundary,1,-1):
    if i % divisor == 0:
        maximum = i
        break
print(maximum)
