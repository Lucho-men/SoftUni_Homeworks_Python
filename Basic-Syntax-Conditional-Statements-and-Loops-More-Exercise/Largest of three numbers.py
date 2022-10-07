import sys

print("First number:",end="")
first_number = int(input())
print("Second number:",end="")
second_number = int(input())
print("Third number:",end="")
third_number = int(input())

largest_num = - sys.maxsize

if largest_num < first_number:
    largest_num = first_number
if largest_num < second_number:
    largest_num = second_number
if largest_num < third_number:
    largest_num = third_number

print(largest_num)