fruit = input()
day_day_of_week = input()
quantity = float(input())

price = 0

if fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes":
    if day_day_of_week == "Saturday" or day_day_of_week == "Sunday":
        if fruit == "banana":
            price = 2.70
            print(f"{quantity*price:0.2f}")
        elif fruit == "apple":
            price = 1.25
            print(f"{quantity*price:0.2f}")
        elif fruit == "orange":
            price = 0.90
            print(f"{quantity*price:0.2f}")
        elif fruit == "grapefruit":
            price = 1.60
            print(f"{quantity*price:0.2f}")
        elif fruit == "kiwi":
            price = 3.00
            print(f"{quantity*price:0.2f}")
        elif fruit == "pineapple":
            price = 5.60
            print(f"{quantity*price:0.2f}")
        elif fruit == "grapes":
            price = 4.20
            print(f"{quantity*price:0.2f}")
        else:
            print("error")

    elif day_day_of_week == "Monday" or day_day_of_week == "Tuesday" or day_day_of_week == "Wednesday" or day_day_of_week == "Thursday" or day_day_of_week == "Friday":
        if fruit == "banana":
            price = 2.50
            print(f"{quantity*price:0.2f}")
        elif fruit == "apple":
            price = 1.20
            print(f"{quantity*price:0.2f}")
        elif fruit == "orange":
            price = 0.85
            print(f"{quantity*price:0.2f}")
        elif fruit == "grapefruit":
            price = 1.45
            print(f"{quantity*price:0.2f}")
        elif fruit == "kiwi":
            price = 2.70
            print(f"{quantity*price:0.2f}")
        elif fruit == "pineapple":
            price = 5.50
            print(f"{quantity*price:0.2f}")
        elif fruit == "grapes":
            price = 3.85
            print(f"{quantity*price:0.2f}")
    else:
        print("error")
else:
    print("error")