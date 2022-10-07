start_num = int(input())
end_num = int(input())
sum_odd = 0
sum_even = 0

for i in range(start_num, end_num + 1):

    for j in range(1, len(str(i))+1):

        if j % 2 != 0:
            sum_odd += int((str(i))[j-1])
        else:
            sum_even += int((str(i))[j-1])

    if sum_odd == sum_even:
         print(i, end=" ")

    sum_odd = 0
    sum_even = 0