budget = int(input())
season = input()
number_of_fishers = int(input())

price_for_rent = 0.0
discount = 0.0
member_discount = 0.0
total_costs = 0.0

if season == "Spring":
    price_for_rent = 3000
elif season == "Summer" or season == "Autumn":
    price_for_rent = 4200
elif season == "Winter":
    price_for_rent = 2600

if number_of_fishers <= 6:
    discount = 0.10
elif 7 <= number_of_fishers <= 11:
    discount = 0.15
elif number_of_fishers >= 12:
    discount = 0.25

if number_of_fishers % 2 == 0 and season != "Autumn":
    member_discount = 0.05

price_for_rent -= price_for_rent * discount
total_costs = price_for_rent - price_for_rent * member_discount

if budget >= total_costs:
    print(f"Yes! You have {budget - total_costs:0.2f} leva left.")
else:
    print(f"Not enough money! You need {total_costs - budget:0.2f} leva.")

