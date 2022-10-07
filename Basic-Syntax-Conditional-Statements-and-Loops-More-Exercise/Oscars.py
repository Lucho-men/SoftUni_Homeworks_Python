name_of_actor = input()
academy_points = float(input())
number_of_judges = int(input())
total_points = academy_points

for i in range(number_of_judges):
    name_of_judge = input()
    points_from_judge = float(input())
    if total_points <= 1250.5:
        total_points += (points_from_judge * len(name_of_judge) )/ 2
    else:
        break

if total_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {1250.5 - total_points:.1f} more!")