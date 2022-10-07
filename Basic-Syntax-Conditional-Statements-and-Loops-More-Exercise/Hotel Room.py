month = input()
number_of_nights = int(input())

price_ap_per_night = 0.0
price_st_per_night = 0.0

price_for_whole_period_ap = 0.0
price_for_whole_period_st = 0.0
discount_ap = 0.0
discount_st = 0.0

if month == "May" or month == "October":
    price_ap_per_night = 65
    price_st_per_night = 50

    if number_of_nights > 7 and number_of_nights <= 14:
        discount_st = 0.05
    elif number_of_nights > 14:
        discount_st = 0.30

elif month == "June" or month == "September":
    price_ap_per_night = 68.70
    price_st_per_night = 75.20

    if number_of_nights > 14:
        discount_st = 0.20

elif month == "July" or month == "August":
    price_ap_per_night = 77
    price_st_per_night = 76

if number_of_nights > 14:
    discount_ap = 0.10

discounted_price_per_night_ap = price_ap_per_night - price_ap_per_night * discount_ap
discounted_price_per_night_st = price_st_per_night - price_st_per_night * discount_st

price_for_whole_period_ap = discounted_price_per_night_ap * number_of_nights
price_for_whole_period_st = discounted_price_per_night_st * number_of_nights
ap = str(f"Apartment: {price_for_whole_period_ap:0.2f} lv.")
st = str(f"Studio: {price_for_whole_period_st:0.2f} lv.")
print(ap)
print(st)