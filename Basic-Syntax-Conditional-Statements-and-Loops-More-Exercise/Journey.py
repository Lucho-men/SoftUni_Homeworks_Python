budget = float(input())
season = input()

destination = ""
type_of_vacation = ""
costs = 0.0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        costs = budget - budget * 0.30
        type_of_vacation = "Camp"
    elif season == "winter":
        costs = budget - budget * 0.70
        type_of_vacation = "Hotel"
elif budget <= 1000 and budget > 100:
    destination = "Balkans"
    if season == "summer":
        costs = budget - budget * 0.40
        type_of_vacation = "Camp"
    elif season == "winter":
        costs = budget - budget * 0.80
        type_of_vacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    costs = budget - budget * 0.90
    type_of_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {budget-costs:0.2f}")

