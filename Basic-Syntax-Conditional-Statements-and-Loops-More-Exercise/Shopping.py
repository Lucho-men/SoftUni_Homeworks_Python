budget = int(input())
price = 0
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    else:
        price += int(command)
        if price > budget:
            print("You went in overdraft!")
            break

