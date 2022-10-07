product = input()
city = input()
quantity = float(input())

if city == "Sofia":
    price_coffee = 0.50
    price_water = 0.80
    price_beer = 1.20
    price_sweets = 1.45
    price_peanuts = 1.60
    if product == "coffee":
        print(f"{quantity*price_coffee:0.2f}")
    elif product == "water":
        print(f"{quantity*price_water:0.2f}")
    elif product == "beer":
        print(f"{quantity*price_beer:0.2f}")
    elif product == "sweets":
        print(f"{quantity*price_sweets:0.2f}")
    elif product == "peanuts":
        print(f"{quantity*price_peanuts:0.2f}")

if city == "Plovdiv":
    price_coffee = 0.40
    price_water = 0.70
    price_beer = 1.15
    price_sweets = 1.30
    price_peanuts = 1.50
    if product == "coffee":
        print(f"{quantity*price_coffee:0.2f}")
    elif product == "water":
        print(f"{quantity*price_water:0.2f}")
    elif product == "beer":
        print(f"{quantity*price_beer:0.2f}")
    elif product == "sweets":
        print(f"{quantity*price_sweets:0.2f}")
    elif product == "peanuts":
        print(f"{quantity*price_peanuts:0.2f}")

if city == "Varna":
    price_coffee = 0.45
    price_water = 0.70
    price_beer = 1.10
    price_sweets = 1.35
    price_peanuts = 1.55
    if product == "coffee":
        print(f"{quantity*price_coffee:0.2f}")
    elif product == "water":
        print(f"{quantity*price_water:0.2f}")
    elif product == "beer":
        print(f"{quantity*price_beer:0.2f}")
    elif product == "sweets":
        print(f"{quantity*price_sweets:0.2f}")
    elif product == "peanuts":
        print(f"{quantity*price_peanuts:0.2f}")
