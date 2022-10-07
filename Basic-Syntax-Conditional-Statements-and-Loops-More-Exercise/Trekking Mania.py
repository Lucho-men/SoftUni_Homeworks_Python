number_of_groups = int(input())
number_of_climbers_Musala = 0
number_of_climbers_Monblan = 0
number_of_climbers_Kilimanjaro = 0
number_of_climbers_K2 = 0
number_of_climbers_Everest = 0
total_climbers = 0

for i in range(number_of_groups):
    number_of_climbers = int(input())
    total_climbers += number_of_climbers
    if number_of_climbers <= 5:
        number_of_climbers_Musala += number_of_climbers
    elif 6 <= number_of_climbers <= 12:
        number_of_climbers_Monblan += number_of_climbers
    elif 13 <= number_of_climbers <= 25:
        number_of_climbers_Kilimanjaro += number_of_climbers
    elif 26 <= number_of_climbers <= 40:
        number_of_climbers_K2 += number_of_climbers
    elif number_of_climbers >= 41:
        number_of_climbers_Everest += number_of_climbers

print(f"{((number_of_climbers_Musala / total_climbers) * 100):.2f}%")
print(f"{((number_of_climbers_Monblan / total_climbers) * 100):.2f}%")
print(f"{((number_of_climbers_Kilimanjaro / total_climbers) * 100):.2f}%")
print(f"{((number_of_climbers_K2 / total_climbers * 100)):.2f}%")
print(f"{((number_of_climbers_Everest / total_climbers * 100)):.2f}%")