type_of_ticket = input()
rows = int(input())
cols = int(input())
price_of_ticket = 0

if type_of_ticket == "Premiere":
    price_of_ticket = 12.00
    print(f"{rows*cols*price_of_ticket:0.2f}")
elif type_of_ticket == "Normal":
    price_of_ticket = 7.50
    print(f"{rows*cols*price_of_ticket:0.2f}")
elif type_of_ticket == "Discount":
    price_of_ticket = 5.00
    print(f"{rows*cols*price_of_ticket:0.2f}")
