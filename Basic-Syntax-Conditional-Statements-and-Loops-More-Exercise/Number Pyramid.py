n = int(input())
counter = 1

for row in range(1,n+1):
    for col in range(1, row+1):
        if counter > n:
            break
        print(f"{counter}", end=" ")
        counter += 1
    print("")