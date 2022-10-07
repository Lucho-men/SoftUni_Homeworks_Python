days_of_stay = int(input()) - 1
accommodation = input()
feedback = input()

total_price_for_the_stay = 0.0
price_single_night = 0.0
discount = 0.0
feedback_discount = 0.0

if accommodation == "room for one person":
    price_single_night = 18.00

if accommodation == "apartment":
    price_single_night = 25.00
    if days_of_stay < 10:
        discount = 0.30
    elif 10 <= days_of_stay <= 15:
        discount = 0.35
    else:
        discount = 0.50

if accommodation == "president apartment":
    price_single_night = 35.00
    if days_of_stay < 10:
        discount = 0.10
    elif 10 <= days_of_stay <= 15:
        discount = 0.15
    else:
        discount = 0.20

total_price_for_the_stay = (days_of_stay * price_single_night) - (days_of_stay * price_single_night) * discount

if feedback == "positive":
    feedback_discount = 0.25
    total_price_for_the_stay = total_price_for_the_stay + total_price_for_the_stay * feedback_discount
elif feedback == "negative":
    feedback_discount = 0.10
    total_price_for_the_stay = total_price_for_the_stay - total_price_for_the_stay * feedback_discount

print(f"{total_price_for_the_stay:0.2f}")
