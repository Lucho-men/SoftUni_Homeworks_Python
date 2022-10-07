entry = input()
destination = ""
current_ammount = 0
total_ammount = 0

while entry != "End":
    destination = entry
    needed_amount = float(input())
    while total_ammount < needed_amount:
        current_ammount = float(input())
        total_ammount += current_ammount

    if total_ammount >= needed_amount:
        print(f"Going to {destination}!")
        total_ammount = 0
        current_ammount = 0

    entry = input()