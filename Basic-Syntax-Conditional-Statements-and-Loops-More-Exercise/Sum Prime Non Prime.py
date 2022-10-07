entry = input()
sum_prime = 0
sum_non_prime = 0

while entry != "stop":
    current_num = int(entry)
    count = 0
    if current_num < 0:
        print("Number is negative.")
    elif current_num == 0:
        sum_non_prime += 0
    elif current_num == 1:
        sum_non_prime += 1
    else:
        num_is_prime = True
        for i in range(2,current_num):
            if current_num % i == 0:
                num_is_prime = False
                break
        if num_is_prime == True:
            sum_prime += current_num
        else:
            sum_non_prime += current_num
    entry = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")