num = int(input())

for current_number in range(1111, 10000):
    num_to_str = str(current_number)
    is_special_num = True
    for index, digit in enumerate(num_to_str):
        if int(digit) == 0 or num % int(digit) != 0:
            is_special_num = False
            break
    if is_special_num:
         print(f"{current_number}", end=" ")