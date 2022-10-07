name = input()
grade = 1
assesment = 0.0
num_of_fails = 0
sum_of_grades = 0.0
average_grade = 0.0

while grade <= 12:
    if num_of_fails < 2:
        assesment = float(input())
        if assesment < 4.00:
            num_of_fails += 1
            grade -= 1
        else:
            sum_of_grades += assesment
            average_grade = sum_of_grades / grade
    else:
        print(f"{name} has been excluded at {grade} grade")
        break

    if grade == 12:
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
    grade += 1



# name = input()
# grades = 1.0
# sum_grades = 0.0
# excluded = 0
# while grades <= 12:
#     grade = float(input())
#     if grade < 4.00:
#         excluded += 1
#         if excluded > 2:
#
#             break
#        continue
# average = sum_grades / 12

