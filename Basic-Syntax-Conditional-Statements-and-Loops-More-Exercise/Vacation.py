needed_money_for_vacation = float(input())
available_money = float(input())
count_spend = 0
days_past = 0

while count_spend < 5 and available_money < needed_money_for_vacation:
    activity = input()
    sum = float(input())
    if activity == "spend":
        available_money -= sum
        if available_money < 0:
            available_money = 0
        count_spend += 1
    elif activity == "save":
        available_money += sum
        count_spend = 0
    days_past += 1

if count_spend >= 5:
    print(f"You can't save the money.")
    print(f"{days_past}")
else:
    print(f"You saved the money for {days_past} days.")
