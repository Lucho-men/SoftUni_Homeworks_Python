beginning_num = int(input())
ending_num = int(input())
magic_num = int(input())
magic_num_found = False
counter = 0

for i in range(beginning_num, ending_num + 1):
    for j in range(beginning_num, ending_num +1):
        counter += 1
        if i + j == magic_num:
            magic_num_found = True
            break
    if magic_num_found == True:
     break

if magic_num_found == False:
    print(f"{counter} combinations - neither equals {magic_num}")
else:
    print(f"Combination N:{counter} ({i} + {j} = {magic_num})")