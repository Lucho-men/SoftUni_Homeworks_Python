n = int(input())
solutions = 0
# x1 + x2 + x3 = n - брой решения = ?

for i in range(0, n+1):
    for j in range(0, n+1):
        for k in range(0, n+1):
            if i + j + k == n:
                solutions += 1

print(solutions)