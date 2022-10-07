line = input()
total_price = 0.0

while line != "NoMoreMoney":
    payment = float(line)
    if payment < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {payment:.2f}")
        line = input()
        total_price += payment

print(f"Total: {total_price:.2f}")

