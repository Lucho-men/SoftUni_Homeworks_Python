from math import floor

number_of_tournaments = int(input())
starting_number_of_points = int(input())
current_points = 0
number_of_wins = 0
average_points = 0

for i in range(number_of_tournaments):
    rank = input()
    if rank == "W":
        number_of_wins += 1
        current_points += 2000
    elif rank == "F":
        current_points += 1200
    elif rank == "SF":
        current_points += 720

total_number_of_points = starting_number_of_points + current_points
average_points = current_points / number_of_tournaments
persentage_wins = number_of_wins / number_of_tournaments

print(f"Final points: {total_number_of_points}")
print(f"Average points: {floor(average_points)}")
print(f"{persentage_wins * 100:.2f}%")
