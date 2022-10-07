n = int(input())
presentation_name = input()
sum_current_assessments = 0.0
total_assesment = 0.0
total_average_assement = 0.0
counter = 0
while presentation_name != "Finish":
    for juri in range(0, n):
        current_assessment = float(input())
        sum_current_assessments += current_assessment
    average_current_assesment = sum_current_assessments / n
    total_assesment += average_current_assesment
    counter += 1
    print(f"{presentation_name} - {average_current_assesment:.2f}.")
    sum_current_assessments = 0
    presentation_name = input()

total_average_assement = total_assesment / counter

print(f"Student's final assessment is {total_average_assement:.2f}.")
