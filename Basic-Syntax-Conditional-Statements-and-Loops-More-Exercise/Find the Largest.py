import sys
# Gets an inter input and gives the largest number that can be formed from it's digits
number = [](int(input()))
list_of_numbers = list()
final_list_of_numbers = list
highest_number = -(sys.maxsize)
for i in range (0,len(number)):
    for j in range (i, len(number)):
        if highest_number < int(list_of_numbers[i]):
            highest_number = list_of_numbers[i]
            final_list_of_numbers[i] = highest_number
            highest_number = -(sys.maxsize)
print(int(final_list_of_numbers.join))

