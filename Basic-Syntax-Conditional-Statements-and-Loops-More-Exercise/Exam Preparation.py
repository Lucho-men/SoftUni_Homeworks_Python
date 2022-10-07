limit_of_bad_grades = int(input())
problem_name = input()
number_of_bad_grades = 0
sum_of_grades = 0.0
number_of_grades = 0
last_problem = ""

while problem_name != "Enough":
    grade = int(input())
    if grade <= 4:
        number_of_bad_grades += 1
        if number_of_bad_grades >= limit_of_bad_grades:
            break
    sum_of_grades += grade
    number_of_grades += 1
    last_problem = problem_name
    problem_name = input()

average_score = sum_of_grades / number_of_grades

if problem_name == "Enough":
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_grades}")
    print(f"Last problem: {last_problem}")

if number_of_bad_grades >= limit_of_bad_grades:
    print(f"You need a break, {number_of_bad_grades} poor grades.")
